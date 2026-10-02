<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>College Event Registration System</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header>
        <h2>EventSystem</h2>
        <nav class="nav-links">
            <a href="index.jsp">Home</a>
            <a href="events.jsp">Events</a>
            <a href="shop.jsp">Shop</a>
            <a href="login.jsp">Login</a>
        </nav>
    </header>
    
    <main>
        <section class="hero">
            <h1>College Event Registration System</h1>
            <p>Discover. Register. Participate.</p>
            <button class="btn" onclick="location.href='events.jsp'">Explore Events</button>
        </section>

        <section class="slider-container">
            <div class="slide active">
                <h3>Tech Fest 2026</h3>
                <p>Join the biggest tech event of the year.</p>
            </div>
            <div class="slide">
                <h3>Cultural Fest</h3>
                <p>Showcase your talents and celebrate.</p>
            </div>
        </section>
    </main>
    <script src="js/script.js"></script>
</body>
</html>
