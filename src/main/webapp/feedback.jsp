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
    <title>Submit Feedback - EventSystem</title>
    <link rel="stylesheet" href="css/style.css">
    <style>
        .feedback-card {
            max-width: 600px;
            margin: 3rem auto;
            text-align: left;
        }
        .feedback-card h2 {
            text-align: center;
            margin-bottom: 2rem;
            color: var(--accent);
        }
        textarea.modern-input {
            resize: vertical;
            min-height: 120px;
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
            <a href="feedback.jsp">Feedback</a>
            <a href="profile.jsp">Profile</a>
            <a href="LogoutServlet">Logout</a>
        </nav>
    </header>
    <main>
        <div class="card feedback-card">
            <h2>Student Feedback</h2>
            <p style="text-align: center; color: var(--text-muted); margin-bottom: 2rem;">Help us improve the college event experience!</p>
            
            <form action="FeedbackServlet" method="POST">
                <div class="form-group">
                    <label>Category</label>
                    <select name="category" class="modern-input" required>
                        <option value="">Select Category</option>
                        <option value="Events">Events & Management</option>
                        <option value="Website">Website & Portal</option>
                        <option value="Merchandise">Merchandise & Shop</option>
                        <option value="Other">Other Suggestions</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label>Rating (1-5)</label>
                    <select name="rating" class="modern-input" required>
                        <option value="5">⭐⭐⭐⭐⭐ (Excellent)</option>
                        <option value="4">⭐⭐⭐⭐ (Good)</option>
                        <option value="3">⭐⭐⭐ (Average)</option>
                        <option value="2">⭐⭐ (Poor)</option>
                        <option value="1">⭐ (Terrible)</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label>Your Feedback / Message</label>
                    <textarea name="message" class="modern-input" placeholder="Type your message here..." required></textarea>
                </div>
                
                <button type="submit" class="btn btn-full">Submit Feedback</button>
            </form>
        </div>
    </main>
</body>
</html>
