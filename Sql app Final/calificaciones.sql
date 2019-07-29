-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 27, 2019 at 09:07 PM
-- Server version: 10.3.16-MariaDB
-- PHP Version: 7.1.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `calificaciones`
--

-- --------------------------------------------------------

--
-- Table structure for table `estudiantes`
--

CREATE TABLE `estudiantes` (
  `nombre_estudiante` varchar(30) NOT NULL,
  `apellido_estudiante` varchar(30) NOT NULL,
  `codigo_unicoPK` int(10) NOT NULL,
  `contrasenia_estudiantes` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `estudiantes`
--

INSERT INTO `estudiantes` (`nombre_estudiante`, `apellido_estudiante`, `codigo_unicoPK`, `contrasenia_estudiantes`) VALUES
('Ronny', 'Patricio', 1, 'ronny'),
('Xavier', 'Calle', 2, 'xavier'),
('Kevin', 'Mendez', 3, 'kevin'),
('Maria', 'Rosales', 4, 'maria'),
('Carmita', 'Benitez', 5, 'carmita'),
('Esther', 'Quilumba', 6, 'esther'),
('Andres', 'Pillo', 7, 'andres'),
('Carla', 'Chala', 8, 'carla'),
('Luis', 'Peralta', 9, 'luis'),
('Sofia', 'La papa fria', 10, 'sofia'),
('Luisito', 'Rey', 11, 'luisito'),
('Mariela', 'Alcala', 12, 'mariela');

-- --------------------------------------------------------

--
-- Table structure for table `notas`
--

CREATE TABLE `notas` (
  `codigo_unicoFK` int(10) DEFAULT NULL,
  `nota1` decimal(10,0) DEFAULT NULL,
  `nota2` decimal(10,0) DEFAULT NULL,
  `nota3` decimal(10,0) DEFAULT NULL,
  `promedio` decimal(10,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `notas`
--

INSERT INTO `notas` (`codigo_unicoFK`, `nota1`, `nota2`, `nota3`, `promedio`) VALUES
(1, '10', '10', '8', '9'),
(2, '10', '10', '9', '10'),
(3, '8', '7', '3', '6'),
(4, '3', '5', '6', '5'),
(5, '7', '8', '9', '8'),
(6, '4', '5', '10', '6'),
(7, '10', '10', '7', '9'),
(8, '9', '8', '7', '8'),
(9, '6', '5', '10', '7'),
(10, '10', '10', '10', '10'),
(11, '6', '10', '9', '8'),
(12, '9', '7', '8', '8');

-- --------------------------------------------------------

--
-- Table structure for table `profesor`
--

CREATE TABLE `profesor` (
  `nombre_profesor` varchar(30) NOT NULL,
  `apellido_profesor` varchar(30) NOT NULL,
  `contrasenia_profesor` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `profesor`
--

INSERT INTO `profesor` (`nombre_profesor`, `apellido_profesor`, `contrasenia_profesor`) VALUES
('profesor', 'chevere', '123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD PRIMARY KEY (`codigo_unicoPK`);

--
-- Indexes for table `notas`
--
ALTER TABLE `notas`
  ADD KEY `notas_ibfk_1` (`codigo_unicoFK`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `notas`
--
ALTER TABLE `notas`
  ADD CONSTRAINT `notas_ibfk_1` FOREIGN KEY (`codigo_unicoFK`) REFERENCES `estudiantes` (`codigo_unicoPK`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
