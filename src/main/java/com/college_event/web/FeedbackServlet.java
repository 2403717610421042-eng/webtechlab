package com.college_event.web;

import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet("/FeedbackServlet")
public class FeedbackServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session = request.getSession();
        if (session.getAttribute("user_id") == null) {
            response.sendRedirect("login.jsp");
            return;
        }

        int userId = (Integer) session.getAttribute("user_id");
        String category = request.getParameter("category");
        int rating = Integer.parseInt(request.getParameter("rating"));
        String message = request.getParameter("message");

        try (Connection conn = DBConnection.getConnection()) {
            String sql = "INSERT INTO feedback (user_id, category, rating, message) VALUES (?, ?, ?, ?)";
            PreparedStatement pst = conn.prepareStatement(sql);
            pst.setInt(1, userId);
            pst.setString(2, category);
            pst.setInt(3, rating);
            pst.setString(4, message);
            
            pst.executeUpdate();
            
            // Redirect back with a success message (could be passed via session attribute)
            response.sendRedirect("home.jsp?feedback=success");
        } catch (Exception e) {
            e.printStackTrace();
            response.sendRedirect("feedback.jsp?error=1");
        }
    }
}
