-- Erstelle Datenbank
CREATE DATABASE tex10_goals;
USE tex10_goals;

-- Tabelle für Firmenziele
CREATE TABLE company_goals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    department VARCHAR(100) NOT NULL,
    statement TEXT NOT NULL,
    success_criteria TEXT NOT NULL,
    rating TINYINT CHECK (rating BETWEEN 1 AND 10),
    assessment TEXT,
    last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Tabelle für Benutzer
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- Tabelle für die Zielhistorie
CREATE TABLE company_goals_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    goal_id INT NOT NULL,
    old_rating TINYINT CHECK (old_rating BETWEEN 1 AND 10),
    new_rating TINYINT CHECK (new_rating BETWEEN 1 AND 10),
    change_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    comment TEXT,
    modified_by INT,
    FOREIGN KEY (goal_id) REFERENCES company_goals(id) ON DELETE CASCADE,
    FOREIGN KEY (modified_by) REFERENCES users(id) ON DELETE SET NULL
);

-- Tabelle für Zielkommentare
CREATE TABLE goal_comments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    goal_id INT NOT NULL,
    user_id INT,
    comment_text TEXT,
    comment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (goal_id) REFERENCES company_goals(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL
);
