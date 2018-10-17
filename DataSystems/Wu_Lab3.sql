CREATE DATABASE ACME;

USE ACME;

CREATE TABLE `ACME`.`employee` (
    `EmplID` INT NOT NULL AUTO_INCREMENT,
    `EmplFname` VARCHAR(25) NOT NULL,
    `EmplLname` VARCHAR(25) NOT NULL,
    `EmplOffice` VARCHAR(5) NOT NULL,
    `EmplPhone` VARCHAR(25) NULL,
    `EmplDept` INT NULL,
    PRIMARY KEY (`EmplID`)
);

CREATE TABLE `ACME`.`department` (
    `DeptId` int(11) NOT NULL,
    `DeptName` varchar(25) NOT NULL,
    `DeptOffice` varchar(5) NOT NULL,
    `DeptPhone` varchar(25) DEFAULT NULL,
    `DeptSupervisor` int(11) DEFAULT NULL,
    PRIMARY KEY (`DeptId`)
);

CREATE TABLE `ACME`.`project` (
    `ProjectId` INT NOT NULL AUTO_INCREMENT,
    `ProjectClient` VARCHAR(15) NOT NULL,
    `ProjectLead` INT NULL,
    `ProjectContactPhone` VARCHAR(25) NULL,
    PRIMARY KEY (`Projectid`)
);

INSERT INTO employee (EmplFname, EmplLname, EmplOffice, EmplPhone, EmplDept) VALUES
    ('Farmer', 'John', 'B728', '(613)123-1234', 1),
    ('Farmer', 'Smith', 'B729', '(613)123-1239', 2),
    ('Farmer', 'Jones', 'B727', '(613)123-1237', 3),
    ('OldMan', 'Farmer', 'B726', '(613)123-1236', 4),
    ('Old', 'McDonald', 'B725', '(613)123-1235', 5);

INSERT INTO department (DeptId, DeptName, DeptOffice, DeptPhone, DeptSupervisor) VALUES
    (1, 'Cows', 'A728', '(613)111-1234', 1),
    (2, 'Chikens', 'A729', '(613)111-1239', 2),
    (3, 'Goats', 'A727', '(613)111-1237', 3),
    (4, 'Sheep', 'A726', '(613)111-1236', 4),
    (5, 'Pigs', 'A725', '(613)111-1235', 5);

INSERT INTO project (ProjectId, ProjectClient, ProjectLead, ProjectContactPhone) VALUES
    (1, 'Cows_R_Us', 1, '(613)121-1234'),
    (2, 'Chickens4Ever', 2, '(613)121-1239'),
    (3, 'GoatsForBoats', 3, '(613)121-1237'),
    (4, 'SteveFoundation', 4, '(613)121-1236'),
    (5, 'Bacon Factory', 5, '(613)121-1235');
