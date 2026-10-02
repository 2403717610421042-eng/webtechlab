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
