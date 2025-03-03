<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $valid_username = "admin";
    $valid_password = "12345";

    $username = $_POST['username'];
    $password = $_POST['password'];

    if ($username === $valid_username && $password === $valid_password) {
        echo "success";
    } else {
        echo "error";
    }
}
?>