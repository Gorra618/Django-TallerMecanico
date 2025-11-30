CREATE DATABASE IF NOT EXISTS Django_TM
    DEFAULT CHARACTER SET = 'utf8mb4';

USE Django_TM;


CREATE TABLE IF NOT EXISTS auth_user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    password VARCHAR(128) NOT NULL,
    last_login DATETIME NULL,
    is_superuser TINYINT(1) NOT NULL,
    username VARCHAR(150) NOT NULL UNIQUE,
    first_name VARCHAR(150) NOT NULL,
    last_name VARCHAR(150) NOT NULL,
    email VARCHAR(254) NOT NULL,
    is_staff TINYINT(1) NOT NULL,
    is_active TINYINT(1) NOT NULL,
    date_joined DATETIME NOT NULL
);

CREATE TABLE IF NOT EXISTS APP_perfiles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    bio TEXT NULL,
    avatar VARCHAR(255) NULL,
    FOREIGN KEY (user_id) REFERENCES auth_user (id)
);

CREATE TABLE IF NOT EXISTS APP_cotizacion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente VARCHAR(255) NOT NULL,
    vehiculo VARCHAR(255) NOT NULL,
    descripcion TEXT NOT NULL,
    fecha DATE NOT NULL,
    unidades INT NOT NULL DEFAULT 1, 
    precio DECIMAL(10, 2) NOT NULL DEFAULT 0.00, 
    total DECIMAL(10, 2) NOT NULL DEFAULT 0.00 
);

CREATE TABLE IF NOT EXISTS APP_presupuesto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cotizacion_id INT NOT NULL,
    aprobado TINYINT(1) NOT NULL DEFAULT 0,
    fecha_aprobacion DATE NULL,
    monto DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    actualizado DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
);

CREATE TABLE IF NOT EXISTS APP_servicio (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT NOT NULL,
    precio DECIMAL(10, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS APP_cotizacion_servicios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cotizacion_id INT NOT NULL,
    servicio_id INT NOT NULL,
    cantidad INT NOT NULL,
    FOREIGN KEY (cotizacion_id) REFERENCES APP_cotizacion (id),
    FOREIGN KEY (servicio_id) REFERENCES APP_servicio (id)
);

INSERT INTO APP_cotizacion (cliente, vehiculo, descripcion, fecha, total)
VALUES ('Juan Pérez', 'Toyota Corolla', 'Cambio de aceite y filtros', '2025-11-30', 150.00);

INSERT INTO APP_presupuesto (cotizacion_id, aprobado, fecha_aprobacion, monto, actualizado)
VALUES (1, 1, '2025-11-30', 150.00, NOW());