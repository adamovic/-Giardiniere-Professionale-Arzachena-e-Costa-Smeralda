-- Database setup for Giardiniere Pro website
-- Run this script in MySQL/XAMPP to create the database

CREATE DATABASE IF NOT EXISTS giardinaggio_db 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

-- Create a user for the application (optional, you can use root)
CREATE USER IF NOT EXISTS 'giardiniere'@'localhost' IDENTIFIED BY 'your_password_here';
GRANT ALL PRIVILEGES ON giardinaggio_db.* TO 'giardiniere'@'localhost';
FLUSH PRIVILEGES;

-- Use the database
USE giardinaggio_db;

-- Tables will be created automatically by Django migrations
-- Run: python manage.py makemigrations
-- Then: python manage.py migrate
