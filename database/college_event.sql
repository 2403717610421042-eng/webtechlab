-- MySQL Script for College Event Registration System

CREATE DATABASE IF NOT EXISTS college_event;
USE college_event;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    department VARCHAR(100),
    year VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    event_name VARCHAR(200) NOT NULL,
    event_date DATETIME NOT NULL,
    venue VARCHAR(200) NOT NULL,
    max_members INT NOT NULL,
    registered_members INT DEFAULT 0
);

CREATE TABLE IF NOT EXISTS event_registrations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    event_id INT NOT NULL,
    registration_number VARCHAR(100) NOT NULL,
    registered_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (event_id) REFERENCES events(id)
);

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    image_url VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    status VARCHAR(50) DEFAULT 'COMPLETED',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Insert Sample Events
INSERT INTO events (event_name, event_date, venue, max_members, registered_members) VALUES
('Tech Fest 2026', '2026-11-15 10:00:00', 'Main Auditorium', 500, 0),
('CodeFest', '2026-11-20 09:00:00', 'CS Lab 1', 100, 0),
('Cultural Fest', '2026-12-05 17:00:00', 'Open Ground', 1000, 0);

-- Insert Sample Products
INSERT INTO products (name, description, price, image_url) VALUES
('College T-Shirt', 'Premium cotton college t-shirt', 15.99, 'tshirt.png'),
('Event Hoodie', 'Warm hoodie with event logo', 35.00, 'hoodie.png'),
('ID Card Holder', 'Stylish lanyard and holder', 5.50, 'idholder.png');
