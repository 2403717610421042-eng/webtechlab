import os

base_dir = "C:\\web project"

def write_file(path, content):
    full_path = os.path.join(base_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

# Event Registration Servlet
write_file("src/main/java/com/college_event/web/EventRegistrationServlet.java", """
package com.college_event.web;

import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.Random;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet("/EventRegistrationServlet")
public class EventRegistrationServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session = request.getSession(false);
        if (session == null || session.getAttribute("user_id") == null) {
            response.sendRedirect("login.jsp");
            return;
        }

        int userId = (Integer) session.getAttribute("user_id");
        String eventIdStr = request.getParameter("event_id");

        if (eventIdStr == null) {
            response.sendRedirect("events.jsp?error=invalid_event");
            return;
        }

        int eventId = Integer.parseInt(eventIdStr);
        String regNumber = "CER-2026-" + (new Random().nextInt(900000) + 100000);

        try (Connection conn = DBConnection.getConnection()) {
            // Check if already registered
            String checkSql = "SELECT * FROM event_registrations WHERE user_id=? AND event_id=?";
            PreparedStatement checkPst = conn.prepareStatement(checkSql);
            checkPst.setInt(1, userId);
            checkPst.setInt(2, eventId);
            ResultSet rs = checkPst.executeQuery();
            if (rs.next()) {
                response.sendRedirect("events.jsp?error=already_registered");
                return;
            }

            // Register
            String sql = "INSERT INTO event_registrations (user_id, event_id, registration_number) VALUES (?, ?, ?)";
            PreparedStatement pst = conn.prepareStatement(sql);
            pst.setInt(1, userId);
            pst.setInt(2, eventId);
            pst.setString(3, regNumber);
            pst.executeUpdate();

            // Update registered members count
            String updateSql = "UPDATE events SET registered_members = registered_members + 1 WHERE id=?";
            PreparedStatement updatePst = conn.prepareStatement(updateSql);
            updatePst.setInt(1, eventId);
            updatePst.executeUpdate();

            session.setAttribute("last_reg_number", regNumber);
            response.sendRedirect("successregistration.jsp");
        } catch (Exception e) {
            e.printStackTrace();
            response.sendRedirect("events.jsp?error=exception");
        }
    }
}
""")

# Events JSP
write_file("src/main/webapp/events.jsp", """
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
""")

# Success Registration JSP
write_file("src/main/webapp/successregistration.jsp", """
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
""")

print("Successfully created Phase 2 (Events).")
