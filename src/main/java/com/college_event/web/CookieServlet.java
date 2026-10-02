package com.college_event.web;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/CookieServlet")
public class CookieServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        
        int visitCount = 1;
        Cookie[] cookies = request.getCookies();
        if (cookies != null) {
            for (Cookie c : cookies) {
                if (c.getName().equals("visitCount")) {
                    visitCount = Integer.parseInt(c.getValue()) + 1;
                }
            }
        }
        
        Cookie visitCookie = new Cookie("visitCount", String.valueOf(visitCount));
        visitCookie.setMaxAge(60 * 60 * 24); // 1 day
        response.addCookie(visitCookie);
        
        out.println("<html><head><title>Cookie Demo</title><link rel='stylesheet' href='css/style.css'></head><body>");
        out.println("<div class='auth-container' style='text-align:center; padding: 50px;'><div class='card'>");
        out.println("<h2>Cookie Experiment</h2>");
        out.println("<p>You have visited this page <strong style='color:#0ea5e9; font-size:1.5rem;'>" + visitCount + "</strong> times.</p>");
        out.println("<a href='index.jsp' class='btn'>Back to Home</a>");
        out.println("</div></div></body></html>");
    }
}
