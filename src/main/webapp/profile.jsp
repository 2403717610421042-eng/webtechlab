<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%
    if (session.getAttribute("user_id") == null) {
        response.sendRedirect("login.jsp");
        return;
    }
%>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Student Profile - EventSystem</title>
    <link rel="stylesheet" href="css/style.css">
    <style>
        .profile-card {
            max-width: 600px;
            margin: 4rem auto;
            text-align: left;
        }
        .profile-row {
            display: flex;
            justify-content: space-between;
            padding: 1rem 0;
            border-bottom: 1px solid var(--card-border);
        }
        .profile-row:last-child {
            border-bottom: none;
        }
        .profile-label {
            color: var(--text-muted);
            font-weight: 500;
        }
        .profile-value {
            color: var(--text-main);
            font-weight: 600;
        }
        .avatar-circle {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            background: var(--gradient);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            font-weight: bold;
            margin: 0 auto 2rem;
            color: white;
            box-shadow: 0 4px 15px rgba(14, 165, 233, 0.4);
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
            <a href="profile.jsp">Profile</a>
            <a href="LogoutServlet">Logout</a>
        </nav>
    </header>
    <main>
        <div class="card profile-card">
            <% 
                String name = (String) session.getAttribute("user_name");
                String initial = (name != null && name.length() > 0) ? name.substring(0, 1).toUpperCase() : "?";
            %>
            <div class="avatar-circle">
                <%= initial %>
            </div>
            <h2 style="text-align: center; margin-bottom: 2rem;">Student Profile</h2>
            
            <div class="profile-row">
                <span class="profile-label">Full Name</span>
                <span class="profile-value"><%= name %></span>
            </div>
            
            <div class="profile-row">
                <span class="profile-label">Student ID</span>
                <span class="profile-value">#STD-<%= session.getAttribute("user_id") %></span>
            </div>
            
            <!-- We retrieve the email dynamically if stored in session, or show a placeholder if not -->
            <div class="profile-row">
                <span class="profile-label">Account Type</span>
                <span class="profile-value">Verified Student</span>
            </div>
            
            <div class="profile-row">
                <span class="profile-label">Session Status</span>
                <span class="profile-value" style="color: #10b981;">Active (2m Timeout)</span>
            </div>
            
            <button class="btn btn-full" style="margin-top: 2rem;" onclick="alert('Profile update coming soon!')">Edit Profile</button>
        </div>
    </main>
</body>
</html>
