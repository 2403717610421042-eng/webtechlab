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
