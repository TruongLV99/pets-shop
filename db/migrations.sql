-- Bảng users (Thông tin người dùng)
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) DEFAULT NULL,
    phone_number VARCHAR(20) DEFAULT NULL,
    type TINYINT DEFAULT 1,
    status TINYINT DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Bảng users (Thông tin người dùng)
CREATE TABLE IF NOT EXISTS customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Bảng pets (Thông tin thú cưng)
CREATE TABLE IF NOT EXISTS pets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    pet_no VARCHAR(100) DEFAULT NULL,
    name VARCHAR(100) NOT NULL,
    breed VARCHAR(100),
    birth_date DATE DEFAULT NULL,
    color VARCHAR(50) DEFAULT NULL,
    weight VARCHAR(100) DEFAULT 0,
    height VARCHAR(100) DEFAULT 0,
    length VARCHAR(100) DEFAULT 0,
    special_features TEXT DEFAULT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Bảng health (Sức khỏe và chăm sóc)
CREATE TABLE IF NOT EXISTS health (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pet_id INT NOT NULL,
    vaccination_date DATE DEFAULT NULL,
    vaccine_name VARCHAR(100) DEFAULT NULL,
    health_check_date DATE,
    health_condition TEXT DEFAULT NULL,
    FOREIGN KEY (pet_id) REFERENCES pets(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Bảng feeding (Chế độ ăn uống)
CREATE TABLE IF NOT EXISTS feeding (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pet_id INT NOT NULL,
    feeding_date DATE,
    feeding_time TIME,
    food_type VARCHAR(100),
    quantity VARCHAR(100) DEFAULT NULL,
    FOREIGN KEY (pet_id) REFERENCES pets(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Bảng exercise (Hoạt động thể chất)
CREATE TABLE IF NOT EXISTS exercise (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pet_id INT NOT NULL,
    exercise_date DATE,
    exercise_time TIME,
    activity_type VARCHAR(100),
    duration VARCHAR(100) DEFAULT NULL,
    FOREIGN KEY (pet_id) REFERENCES pets(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Bảng expense (Quản lý chi phí)
CREATE TABLE IF NOT EXISTS expense (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    pet_id INT NOT NULL,
    expense_date DATE,
    expense_type VARCHAR(100),
    amount DECIMAL(10,2) DEFAULT 0, -- Lưu số tiền chi trả
    description TEXT DEFAULT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE,
    FOREIGN KEY (pet_id) REFERENCES pets(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Bảng appointment (Lịch hẹn)
CREATE TABLE IF NOT EXISTS appointment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    pet_id INT NOT NULL,
    appointment_date DATE,
    appointment_time TIME,
    purpose VARCHAR(100) DEFAULT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE,
    FOREIGN KEY (pet_id) REFERENCES pets(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);