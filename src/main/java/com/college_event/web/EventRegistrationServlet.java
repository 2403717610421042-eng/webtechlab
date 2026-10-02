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
