import os

base_dir = "C:\\web project"

def write_file(path, content):
    full_path = os.path.join(base_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

# Database Connection Class
write_file("src/main/java/com/college_event/web/DBConnection.java", """
package com.college_event.web;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DBConnection {
    private static final String URL = "jdbc:mysql://localhost:3306/college_event";
    private static final String USER = "root"; // Update this with your MySQL username
    private static final String PASSWORD = ""; // Update this with your MySQL password

    public static Connection getConnection() throws SQLException, ClassNotFoundException {
        Class.forName("com.mysql.cj.jdbc.Driver");
        return DriverManager.getConnection(URL, USER, PASSWORD);
    }
}
""")

# Register Servlet
write_file("src/main/java/com/college_event/web/RegisterServlet.java", """
package com.college_event.web;

import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/RegisterServlet")
public class RegisterServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String name = request.getParameter("name");
        String email = request.getParameter("email");
        String password = request.getParameter("password");
        String dept = request.getParameter("department");
        String year = request.getParameter("year");

        try (Connection conn = DBConnection.getConnection()) {
            String sql = "INSERT INTO users (name, email, password, department, year) VALUES (?, ?, ?, ?, ?)";
            PreparedStatement pst = conn.prepareStatement(sql);
            pst.setString(1, name);
            pst.setString(2, email);
            pst.setString(3, password);
            pst.setString(4, dept);
            pst.setString(5, year);
            pst.executeUpdate();
            
            response.sendRedirect("login.jsp?success=registered");
        } catch (Exception e) {
            e.printStackTrace();
            response.sendRedirect("register.jsp?error=true");
        }
    }
}
""")

# Login Servlet
write_file("src/main/java/com/college_event/web/LoginServlet.java", """
package com.college_event.web;

import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet("/LoginServlet")
public class LoginServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String email = request.getParameter("email");
        String password = request.getParameter("password");

        try (Connection conn = DBConnection.getConnection()) {
            String sql = "SELECT * FROM users WHERE email=? AND password=?";
            PreparedStatement pst = conn.prepareStatement(sql);
            pst.setString(1, email);
            pst.setString(2, password);
            ResultSet rs = pst.executeQuery();

            if (rs.next()) {
                HttpSession session = request.getSession();
                session.setAttribute("user_id", rs.getInt("id"));
                session.setAttribute("user_name", rs.getString("name"));
                response.sendRedirect("home.jsp");
            } else {
                response.sendRedirect("login.jsp?error=invalid");
            }
        } catch (Exception e) {
            e.printStackTrace();
            response.sendRedirect("login.jsp?error=exception");
        }
    }
}
""")

# Register JSP
write_file("src/main/webapp/register.jsp", """
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Register - College Event</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header>
        <h2>EventSystem</h2>
        <nav class="nav-links">
            <a href="index.jsp">Home</a>
            <a href="login.jsp">Login</a>
        </nav>
    </header>
    <main class="auth-container">
        <div class="card form-card">
            <h2>Student Registration</h2>
            <form action="RegisterServlet" method="POST" onsubmit="return validateRegisterForm()">
                <div class="form-group">
                    <label>Name</label>
                    <input type="text" name="name" id="name" required class="modern-input">
                </div>
                <div class="form-group">
                    <label>Email</label>
                    <input type="email" name="email" id="email" required class="modern-input">
                </div>
                <div class="form-group">
                    <label>Password</label>
                    <input type="password" name="password" id="password" required class="modern-input">
                </div>
                <div class="form-group">
                    <label>Department</label>
                    <select name="department" id="department" required class="modern-input">
                        <option value="">Select Dept</option>
                        <option value="CS">Computer Science</option>
                        <option value="IT">Information Tech</option>
                        <option value="ECE">ECE</option>
                    </select>
                </div>
                <div class="form-group">
                    <label>Year</label>
                    <select name="year" id="year" required class="modern-input">
                        <option value="">Select Year</option>
                        <option value="1">1st Year</option>
                        <option value="2">2nd Year</option>
                        <option value="3">3rd Year</option>
                        <option value="4">4th Year</option>
                    </select>
                </div>
                <button type="submit" class="btn btn-full">Register</button>
            </form>
        </div>
    </main>
    <script src="js/validation.js"></script>
</body>
</html>
""")

# Login JSP
write_file("src/main/webapp/login.jsp", """
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
""")

# Home JSP (Authenticated)
write_file("src/main/webapp/home.jsp", """
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
    <title>Dashboard - College Event</title>
    <link rel="stylesheet" href="css/style.css">
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
        <section class="hero">
            <h1>Welcome, <%= session.getAttribute("user_name") %>!</h1>
            <p>Your student dashboard.</p>
        </section>
    </main>
</body>
</html>
""")

# Logout Servlet
write_file("src/main/java/com/college_event/web/LogoutServlet.java", """
package com.college_event.web;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet("/LogoutServlet")
public class LogoutServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session = request.getSession(false);
        if (session != null) {
            session.invalidate();
        }
        response.sendRedirect("login.jsp");
    }
}
""")

print("Successfully created Phase 1 Servlets and JSPs.")
