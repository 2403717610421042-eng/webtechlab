<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login - College Event</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header>
        <h2>EventSystem</h2>
        <nav class="nav-links">
            <a href="index.jsp">Home</a>
            <a href="register.jsp">Register</a>
        </nav>
    </header>
    <main class="auth-container">
        <div class="card form-card">
            <h2>Login</h2>
            <% if(request.getParameter("error") != null) { %>
                <p style="color: #ef4444;">Invalid credentials. Try again.</p>
            <% } %>
            <% if(request.getParameter("success") != null) { %>
                <p style="color: #22c55e;">Registration successful! Please login.</p>
            <% } %>
            <form action="LoginServlet" method="POST">
                <div class="form-group">
                    <label>Email</label>
                    <input type="email" name="email" required class="modern-input">
                </div>
                <div class="form-group">
                    <label>Password</label>
                    <input type="password" name="password" required class="modern-input">
                </div>
                <button type="submit" class="btn btn-full">Login</button>
            </form>
        </div>
    </main>
</body>
</html>
