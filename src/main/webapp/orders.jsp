<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.sql.*, com.college_event.web.DBConnection" %>
<%
    if (session.getAttribute("user_id") == null) {
        response.sendRedirect("login.jsp");
        return;
    }
    int userId = (Integer) session.getAttribute("user_id");
%>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Orders - EventSystem</title>
    <link rel="stylesheet" href="css/style.css">
    <style>
        .orders-container {
            max-width: 1000px;
            margin: 4rem auto;
            padding: 0 2rem;
        }
        .order-card {
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .order-details h4 {
            color: var(--accent);
            margin-bottom: 0.5rem;
        }
        .order-details p {
            color: var(--text-muted);
            font-size: 0.95rem;
        }
        .order-status {
            background: rgba(16, 185, 129, 0.2);
            color: #10b981;
            padding: 0.5rem 1rem;
            border-radius: 50px;
            font-weight: 600;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <header>
        <h2>EventSystem</h2>
        <nav class="nav-links">
            <a href="home.jsp">Dashboard</a>
            <a href="events.jsp">Events</a>
            <a href="shop.jsp">Shop</a>
            <a href="orders.jsp">My Orders</a>
            <a href="feedback.jsp">Feedback</a>
            <a href="profile.jsp">Profile</a>
            <a href="LogoutServlet">Logout</a>
        </nav>
    </header>
    <main class="orders-container">
        <h2 style="text-align: center; margin-bottom: 2rem; color: var(--text-main);">Order History</h2>
        
        <%
            try (Connection conn = DBConnection.getConnection()) {
                String sql = "SELECT * FROM orders WHERE user_id = ? ORDER BY created_at DESC";
                PreparedStatement pst = conn.prepareStatement(sql);
                pst.setInt(1, userId);
                ResultSet rs = pst.executeQuery();
                
                boolean hasOrders = false;
                while (rs.next()) {
                    hasOrders = true;
                    int orderId = rs.getInt("id");
                    double amount = rs.getDouble("total_amount");
                    String status = rs.getString("status");
                    String date = rs.getString("created_at");
        %>
            <div class="order-card">
                <div class="order-details">
                    <h4>Order #ORD-2026-<%= orderId %></h4>
                    <p>Total Amount: <strong>$<%= String.format("%.2f", amount) %></strong></p>
                    <p>Date: <%= date %></p>
                </div>
                <div class="order-status"><%= status %></div>
            </div>
        <%
                }
                if (!hasOrders) {
        %>
            <div class="card" style="text-align: center; padding: 3rem;">
                <h3 style="color: var(--text-muted);">You haven't placed any orders yet.</h3>
                <a href="shop.jsp" class="btn" style="margin-top: 1.5rem; display: inline-block;">Visit Shop</a>
            </div>
        <%
                }
            } catch (Exception e) {
                out.println("<p style='color:red;'>Error loading orders: " + e.getMessage() + "</p>");
            }
        %>
    </main>
</body>
</html>
