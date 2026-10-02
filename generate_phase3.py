import os

base_dir = "C:\\web project"

def write_file(path, content):
    full_path = os.path.join(base_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

# Shop JSP
write_file("src/main/webapp/shop.jsp", """
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.sql.*, com.college_event.web.DBConnection" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Event Shop</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header>
        <h2>EventSystem</h2>
        <nav class="nav-links">
            <a href="index.jsp">Home</a>
            <a href="events.jsp">Events</a>
            <a href="shop.jsp">Shop</a>
            <a href="cart.jsp">Cart</a>
        </nav>
    </header>
    <main>
        <section class="hero" style="padding: 2rem;">
            <h1>Event Shop</h1>
            <p>Get your official college merchandise here!</p>
        </section>
        <section class="events-grid" style="display: flex; flex-wrap: wrap; justify-content: center;">
            <%
                try (Connection conn = DBConnection.getConnection()) {
                    String sql = "SELECT * FROM products";
                    PreparedStatement pst = conn.prepareStatement(sql);
                    ResultSet rs = pst.executeQuery();
                    while(rs.next()) {
                        int id = rs.getInt("id");
                        String name = rs.getString("name");
                        String desc = rs.getString("description");
                        double price = rs.getDouble("price");
            %>
            <div class="card event-card" style="width: 250px;">
                <h3><%= name %></h3>
                <p><%= desc %></p>
                <h4 style="color: var(--accent);">$<%= price %></h4>
                <form action="AddToCartServlet" method="POST">
                    <input type="hidden" name="product_id" value="<%= id %>">
                    <input type="hidden" name="product_name" value="<%= name %>">
                    <input type="hidden" name="price" value="<%= price %>">
                    <button type="submit" class="btn">Add to Cart</button>
                </form>
            </div>
            <%
                    }
                } catch(Exception e) {
                    out.println("<p>Error loading products.</p>");
                }
            %>
        </section>
    </main>
</body>
</html>
""")

# Add To Cart Servlet
write_file("src/main/java/com/college_event/web/AddToCartServlet.java", """
package com.college_event.web;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet("/AddToCartServlet")
public class AddToCartServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session = request.getSession(true);
        List<Map<String, String>> cart = (List<Map<String, String>>) session.getAttribute("cart");
        if (cart == null) {
            cart = new ArrayList<>();
        }

        Map<String, String> item = new HashMap<>();
        item.put("id", request.getParameter("product_id"));
        item.put("name", request.getParameter("product_name"));
        item.put("price", request.getParameter("price"));

        cart.add(item);
        session.setAttribute("cart", cart);

        response.sendRedirect("cart.jsp");
    }
}
""")

# Cart JSP
write_file("src/main/webapp/cart.jsp", """
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.util.*" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Shopping Cart</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header>
        <h2>EventSystem</h2>
        <nav class="nav-links">
            <a href="shop.jsp">Shop</a>
        </nav>
    </header>
    <main class="auth-container" style="max-width: 600px; margin: auto; padding-top: 2rem;">
        <div class="card">
            <h2>Your Cart</h2>
            <%
                List<Map<String, String>> cart = (List<Map<String, String>>) session.getAttribute("cart");
                double total = 0.0;
                if(cart != null && !cart.isEmpty()) {
                    out.println("<ul style='list-style: none; padding: 0;'>");
                    for(Map<String, String> item : cart) {
                        double price = Double.parseDouble(item.get("price"));
                        total += price;
                        out.println("<li style='padding: 10px; border-bottom: 1px solid #333;'>" + item.get("name") + " - $" + price + "</li>");
                    }
                    out.println("</ul>");
                    out.println("<h3>Total: $" + total + "</h3>");
            %>
            <form action="CheckoutServlet" method="POST" style="margin-top: 1rem;">
                <input type="hidden" name="total" value="<%= total %>">
                <button type="submit" class="btn btn-full">Checkout</button>
            </form>
            <%
                } else {
                    out.println("<p>Your cart is empty.</p>");
                }
            %>
        </div>
    </main>
</body>
</html>
""")

# Checkout Servlet
write_file("src/main/java/com/college_event/web/CheckoutServlet.java", """
package com.college_event.web;

import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet("/CheckoutServlet")
public class CheckoutServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session = request.getSession(false);
        if (session == null || session.getAttribute("user_id") == null) {
            response.sendRedirect("login.jsp?redirect=cart");
            return;
        }

        int userId = (Integer) session.getAttribute("user_id");
        double total = Double.parseDouble(request.getParameter("total"));

        try (Connection conn = DBConnection.getConnection()) {
            String sql = "INSERT INTO orders (user_id, total_amount) VALUES (?, ?)";
            PreparedStatement pst = conn.prepareStatement(sql);
            pst.setInt(1, userId);
            pst.setDouble(2, total);
            pst.executeUpdate();
            
            session.removeAttribute("cart");
            response.sendRedirect("ordersuccess.jsp");
        } catch (Exception e) {
            e.printStackTrace();
            response.sendRedirect("cart.jsp?error=exception");
        }
    }
}
""")

# Order Success JSP
write_file("src/main/webapp/ordersuccess.jsp", """
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Order Success</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header>
        <h2>EventSystem</h2>
        <nav class="nav-links">
            <a href="shop.jsp">Shop</a>
            <a href="home.jsp">Dashboard</a>
        </nav>
    </header>
    <main class="auth-container">
        <div class="card form-card" style="text-align: center;">
            <h2>Order Placed Successfully!</h2>
            <p>Thank you for purchasing college merchandise.</p>
            <button class="btn" onclick="location.href='shop.jsp'">Back to Shop</button>
        </div>
    </main>
</body>
</html>
""")

print("Successfully created Phase 3 (Ecommerce).")
