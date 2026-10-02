import os

base_dir = "C:\\web project"

def write_file(path, content):
    full_path = os.path.join(base_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

# Active Users Listener
write_file("src/main/java/com/college_event/web/ActiveUsersListener.java", """
package com.college_event.web;

import javax.servlet.annotation.WebListener;
import javax.servlet.http.HttpSessionEvent;
import javax.servlet.http.HttpSessionListener;

@WebListener
public class ActiveUsersListener implements HttpSessionListener {
    private static int activeSessions = 0;

    public void sessionCreated(HttpSessionEvent se) {
        activeSessions++;
        se.getSession().getServletContext().setAttribute("activeUsers", activeSessions);
    }

    public void sessionDestroyed(HttpSessionEvent se) {
        if(activeSessions > 0) activeSessions--;
        se.getSession().getServletContext().setAttribute("activeUsers", activeSessions);
    }
}
""")

# Cookie Servlet
write_file("src/main/java/com/college_event/web/CookieServlet.java", """
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
""")

print("Successfully created Phase 6 (Cookies & Listeners).")
