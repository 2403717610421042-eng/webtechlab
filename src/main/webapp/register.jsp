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
