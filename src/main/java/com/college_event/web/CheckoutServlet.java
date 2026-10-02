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

@WebServlet("/CheckoutServlet")
public class CheckoutServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session = request.getSession(false);
        if (session == null || session.getAttribute("user_id") == null) {
            response.sendRedirect("login.jsp?redirect=cart");
            return;
        }

        int userId = (Integer) session.getAttribute("user_id");
        double total = Double.parseDouble(request.getParameter("total"));

        try (Connection conn = DBConnection.getConnection()) {
            String sql = "INSERT INTO orders (user_id, total_amount) VALUES (?, ?)";
            PreparedStatement pst = conn.prepareStatement(sql);
            pst.setInt(1, userId);
            pst.setDouble(2, total);
            pst.executeUpdate();
            
            session.removeAttribute("cart");
            response.sendRedirect("ordersuccess.jsp");
        } catch (Exception e) {
            e.printStackTrace();
            response.sendRedirect("cart.jsp?error=exception");
        }
    }
}
