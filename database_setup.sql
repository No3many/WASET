CREATE DATABASE IF NOT EXISTS waset;
USE waset;

-- جدول المستخدمين
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('Producer', 'Importer') NOT NULL
);

-- جدول المزادات (ده اللي زميلك هيشتغل عليه بعدين)
CREATE TABLE IF NOT EXISTS auctions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    start_price DECIMAL(10, 2) NOT NULL,
    current_price DECIMAL(10, 2) DEFAULT 0.00,
    end_time DATETIME NOT NULL,
    producer_id INT,
    status ENUM('Active', 'Closed', 'Paid') DEFAULT 'Active',
    FOREIGN KEY (producer_id) REFERENCES users(id)
);