import os

base_dir = "C:\\web project"

def write_file(path, content):
    full_path = os.path.join(base_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

# CSS
write_file("src/main/webapp/css/style.css", """
:root {
    --bg-color: #0f172a;
    --card-bg: rgba(30, 41, 59, 0.7);
    --text-main: #f8fafc;
    --text-muted: #94a3b8;
    --accent: #0ea5e9;
    --accent-hover: #0284c7;
    --gradient: linear-gradient(135deg, #3b82f6, #8b5cf6);
}

body {
    margin: 0;
    font-family: 'Inter', sans-serif;
    background-color: var(--bg-color);
    color: var(--text-main);
}

header {
    background: var(--card-bg);
    backdrop-filter: blur(10px);
    padding: 1rem 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(255,255,255,0.1);
}

.nav-links a {
    color: var(--text-main);
    text-decoration: none;
    margin-left: 1.5rem;
    transition: color 0.3s;
}

.nav-links a:hover {
    color: var(--accent);
}

.hero {
    text-align: center;
    padding: 5rem 2rem;
    background: var(--gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.btn {
    background: var(--accent);
    color: white;
    padding: 0.75rem 1.5rem;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-size: 1rem;
    transition: background 0.3s, transform 0.2s;
}

.btn:hover {
    background: var(--accent-hover);
    transform: translateY(-2px);
}

.card {
    background: var(--card-bg);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1rem;
    backdrop-filter: blur(10px);
}

/* Slider */
.slider-container {
    width: 80%;
    margin: auto;
    overflow: hidden;
    position: relative;
    border-radius: 12px;
}
.slide { display: none; padding: 3rem; text-align: center; background: var(--card-bg); }
.slide.active { display: block; }
""")

# JS
write_file("src/main/webapp/js/script.js", """
document.addEventListener("DOMContentLoaded", () => {
    let slides = document.querySelectorAll(".slide");
    if(slides.length > 0) {
        let current = 0;
        slides[current].classList.add("active");
        setInterval(() => {
            slides[current].classList.remove("active");
            current = (current + 1) % slides.length;
            slides[current].classList.add("active");
        }, 3000);
    }
});
""")

write_file("src/main/webapp/js/validation.js", """
function validateForm() {
    let name = document.getElementById("name").value;
    if(name === "") {
        alert("Name cannot be empty");
        return false;
    }
    return true;
}
""")

# HTML/JSP
write_file("src/main/webapp/index.jsp", """
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
""")

# Web.xml
write_file("src/main/webapp/WEB-INF/web.xml", """
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee" version="4.0">
    <session-config>
        <session-timeout>2</session-timeout>
    </session-config>
</web-app>
""")

print("Successfully created starter files.")
