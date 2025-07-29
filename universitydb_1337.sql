-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 10, 2024 at 05:05 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `universitydb`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `Getavg` (IN `dept_id` INT)   BEGIN 
SELECT AVG(Age) AS AverageAge 
FROM Student 
WHERE DepartmentID = dept_id;

END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `CourseID` int(11) NOT NULL,
  `CourseName` varchar(100) DEFAULT NULL,
  `Credits` int(11) DEFAULT NULL,
  `DepartmentID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`CourseID`, `CourseName`, `Credits`, `DepartmentID`) VALUES
(1, 'DBMS Lab', 4, 1),
(2, 'Linear Algebra', 3, 2),
(3, 'Quantum Physics', 4, 3),
(4, 'Molecular Biology', 3, 4),
(5, 'Organic Chemistry', 4, 5);

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `DepartmentID` int(11) NOT NULL,
  `DeptName` varchar(100) DEFAULT NULL,
  `HeadID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`DepartmentID`, `DeptName`, `HeadID`) VALUES
(1, 'Computer Science', 2),
(2, 'Mathematics', 4),
(3, 'Physics', 1),
(4, 'Biology', 3),
(5, 'Chemistry', 5);

-- --------------------------------------------------------

--
-- Table structure for table `enrollment`
--

CREATE TABLE `enrollment` (
  `StudentID` int(11) NOT NULL,
  `CourseID` int(11) NOT NULL,
  `Grade` varchar(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `enrollment`
--

INSERT INTO `enrollment` (`StudentID`, `CourseID`, `Grade`) VALUES
(1, 1, 'B'),
(2, 1, 'B'),
(3, 2, 'A'),
(4, 3, 'B'),
(5, 4, 'A');

-- --------------------------------------------------------

--
-- Table structure for table `faculty`
--

CREATE TABLE `faculty` (
  `FacultyID` int(11) NOT NULL,
  `Name` varchar(100) DEFAULT NULL,
  `Age` int(11) DEFAULT NULL,
  `Designation` varchar(50) DEFAULT NULL,
  `Salary` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `faculty`
--

INSERT INTO `faculty` (`FacultyID`, `Name`, `Age`, `Designation`, `Salary`) VALUES
(1, 'Dr. John Smith', 45, 'Associate Professor', 75000.00),
(2, 'Dr. Emily Wong', 50, 'Professor', 90000.00),
(3, 'Prof. Michael Lee', 38, 'Assistant Professor', 60000.00),
(4, 'Dr. Sarah Johnson', 55, 'Professor', 95000.00),
(5, 'Prof. David Kim', 42, 'Associate Professor', 78000.00);

--
-- Triggers `faculty`
--
DELIMITER $$
CREATE TRIGGER `UpdateSalaryOnPromotionToProf` BEFORE UPDATE ON `faculty` FOR EACH ROW BEGIN
    IF OLD.Designation != 'Professor' AND NEW.Designation = 'Professor' THEN
        SET NEW.Salary = NEW.Salary * 1.1;
    END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `StudentID` int(11) NOT NULL,
  `Name` varchar(100) DEFAULT NULL,
  `Age` int(11) DEFAULT NULL,
  `Sex` varchar(10) DEFAULT NULL,
  `DepartmentID` int(11) DEFAULT NULL,
  `PhoneNumber` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`StudentID`, `Name`, `Age`, `Sex`, `DepartmentID`, `PhoneNumber`) VALUES
(1, 'Alex Chen', 20, 'Male', 1, NULL),
(2, 'Emma Rodriguez', 22, 'Female', 1, NULL),
(3, 'Ryan Patel', 21, 'Male', 2, NULL),
(4, 'Sophia Kim', 19, 'Female', 3, NULL),
(5, 'Daniel Wu', 23, 'Male', 4, NULL);

-- --------------------------------------------------------

--
-- Stand-in structure for view `topstudents`
-- (See below for the actual view)
--
CREATE TABLE `topstudents` (
`Name` varchar(100)
,`CourseName` varchar(100)
);

-- --------------------------------------------------------

--
-- Structure for view `topstudents`
--
DROP TABLE IF EXISTS `topstudents`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `topstudents`  AS SELECT DISTINCT `student`.`Name` AS `Name`, `course`.`CourseName` AS `CourseName` FROM ((`student` join `enrollment` on(`student`.`StudentID` = `enrollment`.`StudentID`)) join `course` on(`enrollment`.`CourseID` = `course`.`CourseID`)) WHERE `enrollment`.`Grade` = 'A' ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`CourseID`),
  ADD KEY `DepartmentID` (`DepartmentID`);

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`DepartmentID`),
  ADD KEY `HeadID` (`HeadID`);

--
-- Indexes for table `enrollment`
--
ALTER TABLE `enrollment`
  ADD PRIMARY KEY (`StudentID`,`CourseID`),
  ADD KEY `CourseID` (`CourseID`);

--
-- Indexes for table `faculty`
--
ALTER TABLE `faculty`
  ADD PRIMARY KEY (`FacultyID`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`StudentID`),
  ADD KEY `DepartmentID` (`DepartmentID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `course`
--
ALTER TABLE `course`
  ADD CONSTRAINT `course_ibfk_1` FOREIGN KEY (`DepartmentID`) REFERENCES `department` (`DepartmentID`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `department`
--
ALTER TABLE `department`
  ADD CONSTRAINT `department_ibfk_1` FOREIGN KEY (`HeadID`) REFERENCES `faculty` (`FacultyID`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `enrollment`
--
ALTER TABLE `enrollment`
  ADD CONSTRAINT `enrollment_ibfk_1` FOREIGN KEY (`StudentID`) REFERENCES `student` (`StudentID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `enrollment_ibfk_2` FOREIGN KEY (`CourseID`) REFERENCES `course` (`CourseID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `student`
--
ALTER TABLE `student`
  ADD CONSTRAINT `student_ibfk_1` FOREIGN KEY (`DepartmentID`) REFERENCES `department` (`DepartmentID`) ON DELETE SET NULL ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
