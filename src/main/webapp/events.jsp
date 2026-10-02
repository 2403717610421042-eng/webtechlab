<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.sql.*, com.college_event.web.DBConnection" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Events - College Event</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header>
        <h2>EventSystem</h2>
        <nav class="nav-links">
            <a href="index.jsp">Home</a>
            <a href="events.jsp">Events</a>
            <% if(session.getAttribute("user_id") != null) { %>
                <a href="home.jsp">Dashboard</a>
                <a href="LogoutServlet">Logout</a>
            <% } else { %>
                <a href="login.jsp">Login</a>
            <% } %>
        </nav>
    </header>
    <main>
        <section class="hero" style="padding: 2rem;">
            <h1>Upcoming Events</h1>
        </section>
        <section class="events-grid" style="display: flex; flex-wrap: wrap; justify-content: center;">
            <%
                try (Connection conn = DBConnection.getConnection()) {
                    String sql = "SELECT * FROM events";
                    PreparedStatement pst = conn.prepareStatement(sql);
                    ResultSet rs = pst.executeQuery();
                    while(rs.next()) {
                        int id = rs.getInt("id");
                        String name = rs.getString("event_name");
                        String date = rs.getString("event_date");
                        String venue = rs.getString("venue");
                        int max = rs.getInt("max_members");
                        int registered = rs.getInt("registered_members");
            %>
            <div class="card event-card" style="width: 300px;">
                <h3><%= name %></h3>
                <p>Date: <%= date %></p>
                <p>Venue: <%= venue %></p>
                <p>Seats: <%= registered %> / <%= max %></p>
                <form action="EventRegistrationServlet" method="POST">
                    <input type="hidden" name="event_id" value="<%= id %>">
                    <button type="submit" class="btn" onclick="return confirm('Are you sure you want to register for this event?');">Register Now</button>
                </form>
            </div>
            <%
                    }
                } catch(Exception e) {
                    out.println("<p>Error loading events.</p>");
                }
            %>
        </section>
    </main>
</body>
</html>
