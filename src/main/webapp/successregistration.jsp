<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%
    if (session.getAttribute("user_id") == null || session.getAttribute("last_reg_number") == null) {
        response.sendRedirect("events.jsp");
        return;
    }
%>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Registration Success</title>
    <link rel="stylesheet" href="css/style.css">
    <script>
        window.onload = function() {
            alert("Event Registration Successful!");
        }
    </script>
</head>
<body>
    <header>
        <h2>EventSystem</h2>
        <nav class="nav-links">
            <a href="home.jsp">Dashboard</a>
            <a href="events.jsp">Events</a>
        </nav>
    </header>
    <main class="auth-container">
        <div class="card form-card" style="text-align: center;">
            <h2>Registration Successful!</h2>
            <p>Your Registration Number is:</p>
            <h3 style="color: var(--accent);"><%= session.getAttribute("last_reg_number") %></h3>
            <p>Please keep this number safe.</p>
            <button class="btn" onclick="location.href='events.jsp'">Back to Events</button>
        </div>
    </main>
</body>
</html>
