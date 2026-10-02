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
