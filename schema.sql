CREATE DATABASE IF NOT EXISTS expense_tracker;
USE expense_tracker;

CREATE TABLE User (
    UserId INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Password VARCHAR(255) NOT NULL,
    Currency VARCHAR(10) DEFAULT 'INR',
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE Category (
    CategoryId INT PRIMARY KEY AUTO_INCREMENT,
    CategoryName VARCHAR(100) NOT NULL,
    CategoryType ENUM('Income', 'Expense') NOT NULL
);


CREATE TABLE Income (
    IncomeId INT PRIMARY KEY AUTO_INCREMENT,
    UserId INT NOT NULL,
    Amount DECIMAL(10,2) NOT NULL,
    Date DATE NOT NULL,
    Source VARCHAR(100) NOT NULL,
    Description TEXT,
    FOREIGN KEY (UserId) REFERENCES User(UserId) ON DELETE CASCADE
);


CREATE TABLE Expense (
    ExpenseId INT PRIMARY KEY AUTO_INCREMENT,
    UserId INT NOT NULL,
    CategoryId INT NOT NULL,
    Amount DECIMAL(10,2) NOT NULL,
    Date DATE NOT NULL,
    RecurringFlag BOOLEAN DEFAULT FALSE,
    Description TEXT,
    FOREIGN KEY (UserId) REFERENCES User(UserId) ON DELETE CASCADE,
    FOREIGN KEY (CategoryId) REFERENCES Category(CategoryId) ON DELETE CASCADE
);


CREATE TABLE Budget (
    BudgetId INT PRIMARY KEY AUTO_INCREMENT,
    UserId INT NOT NULL,
    CategoryId INT NOT NULL,
    BudgetLimit DECIMAL(10,2) NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL,
    CurrentAmount DECIMAL(15,2) DEFAULT 0,
    FOREIGN KEY (UserId) REFERENCES User(UserId) ON DELETE CASCADE,
    FOREIGN KEY (CategoryId) REFERENCES Category(CategoryId) ON DELETE CASCADE
);


CREATE TABLE Goals (
    GoalId INT PRIMARY KEY AUTO_INCREMENT,
    UserId INT NOT NULL,
    GoalName VARCHAR(255) NOT NULL,
    TargetAmount DECIMAL(15,2) NOT NULL,
    CurrentAmount DECIMAL(15,2) DEFAULT 0,
    StartDate DATETIME NOT NULL,
    EndDate DATETIME,
    Status ENUM('Active', 'Completed', 'Abandoned') DEFAULT 'Active',
    FOREIGN KEY (UserId) REFERENCES User(UserId) ON DELETE CASCADE
);


CREATE TABLE Reports (
    ReportId INT PRIMARY KEY AUTO_INCREMENT,
    UserId INT NOT NULL,
    ReportType ENUM('Expense', 'Income', 'Budget', 'Goal', 'Custom') NOT NULL,
    GeneratedDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    ReportData JSON,  -- Store report parameters and/or summarized data
    FOREIGN KEY (UserId) REFERENCES User(UserId) ON DELETE CASCADE
);


CREATE TABLE Notifications (
    NotificationId INT PRIMARY KEY AUTO_INCREMENT,
    UserId INT NOT NULL,
    Message TEXT NOT NULL,
    Date DATETIME DEFAULT CURRENT_TIMESTAMP,
    IsRead BOOLEAN DEFAULT FALSE,
    Type ENUM('BudgetAlert', 'GoalAchievement', 'Reminder', 'System') NOT NULL,
    RelatedEntityId INT NULL,  -- Can reference a budget, goal, etc.
    RelatedEntityType VARCHAR(50) NULL,  -- 'Budget', 'Goal', etc.
    FOREIGN KEY (UserId) REFERENCES User(UserId) ON DELETE CASCADE
);


CREATE TABLE SearchFilters (
    FilterId INT PRIMARY KEY AUTO_INCREMENT,
    UserId INT NOT NULL,
    FilterName VARCHAR(255) NOT NULL,
    FilterCriteria JSON NOT NULL,  -- Store complex filter criteria
    DateSaved DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (UserId) REFERENCES User(UserId) ON DELETE CASCADE
);