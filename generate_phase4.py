import os

base_dir = "C:\\web project"

def write_file(path, content):
    full_path = os.path.join(base_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

# AJAX Registration JSP
write_file("src/main/webapp/ajax-registration.jsp", """
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AJAX Registration</title>
    <link rel="stylesheet" href="css/style.css">
    <script>
        function checkEmailAvailability() {
            var email = document.getElementById("email").value;
            var message = document.getElementById("emailMessage");
            if(email === "") {
                message.innerHTML = "";
                return;
            }
            
            var xhr = new XMLHttpRequest();
            xhr.open("POST", "php/validate_registration.php", true);
            xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
            xhr.onreadystatechange = function() {
                if(xhr.readyState == 4 && xhr.status == 200) {
                    var response = JSON.parse(xhr.responseText);
                    if(response.available) {
                        message.innerHTML = "<span style='color: #22c55e;'>Email is available</span>";
                    } else {
                        message.innerHTML = "<span style='color: #ef4444;'>Email already registered</span>";
                    }
                }
            };
            xhr.send("email=" + encodeURIComponent(email));
        }
    </script>
</head>
<body>
    <header>
        <h2>EventSystem</h2>
        <nav class="nav-links">
            <a href="index.jsp">Home</a>
        </nav>
    </header>
    <main class="auth-container">
        <div class="card form-card">
            <h2>AJAX Registration Validation</h2>
            <p>Type an email to see AJAX & PHP in action without refreshing.</p>
            <form>
                <div class="form-group">
                    <label>Email</label>
                    <input type="email" id="email" class="modern-input" onkeyup="checkEmailAvailability()">
                    <div id="emailMessage" style="margin-top: 5px; font-size: 0.9em;"></div>
                </div>
            </form>
        </div>
    </main>
</body>
</html>
""")

# PHP Validation script
write_file("php/validate_registration.php", """
<?php
header('Content-Type: application/json');

// This is a simple mock for the lab experiment. 
// In a real application, you would query the MySQL database here.

$existingEmails = array("test@college.edu", "admin@college.edu", "student@college.edu");

if (isset($_POST['email'])) {
    $email = $_POST['email'];
    if (in_array($email, $existingEmails)) {
        echo json_encode(array("available" => false));
    } else {
        echo json_encode(array("available" => true));
    }
} else {
    echo json_encode(array("error" => "No email provided"));
}
?>
""")

print("Successfully created Phase 4 (AJAX & PHP).")
