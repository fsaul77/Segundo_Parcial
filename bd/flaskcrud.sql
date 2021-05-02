-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 02-05-2021 a las 01:58:43
-- Versión del servidor: 10.4.17-MariaDB
-- Versión de PHP: 7.3.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `flaskcrud`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contacts`
--

CREATE TABLE `contacts` (
  `id` int(11) NOT NULL,
  `cc` int(12) NOT NULL,
  `fullname` varchar(250) NOT NULL,
  `lastname` varchar(250) NOT NULL,
  `phone` varchar(250) NOT NULL,
  `email` varchar(250) NOT NULL,
  `semester` int(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `contacts`
--

INSERT INTO `contacts` (`id`, `cc`, `fullname`, `lastname`, `phone`, `email`, `semester`) VALUES
(5, 1127077868, 'Nelson ', 'Figueroa ', '3234638002', 'fsaul77@hotmail.com', 10),
(8, 123435666, 'Camilo', 'Ordoñez', '3249834743', 'camilo@gmail.com', 10),
(10, 123456789, 'Ana', 'Gutierrez', '3245678890', 'Ana@gmail.com', 10),
(12, 2147483647, 'Pedro', 'Portilla', '1291239871', 'pedro@gamil.com', 10),
(13, 12001230, 'Marcos2', 'Alonso2', '12312313', 'marcos@gmail.com', 10),
(14, 129129223, 'Pablo', 'Diaz', '320192123', 'pablo@gmail.com', 10),
(15, 99129123, 'Maria2', 'Ramos2', '1234567886', 'maria@gmail.com', 6),
(26, 109382913, 'Fernando', 'Lopez', '133322423', 'fercho@gmail.com', 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `materias`
--

CREATE TABLE `materias` (
  `id` int(11) NOT NULL,
  `nombre` varchar(250) NOT NULL,
  `semestre` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `materias`
--

INSERT INTO `materias` (`id`, `nombre`, `semestre`) VALUES
(31, 'electiva profesional 2', '10'),
(38, 'electiva profesional 1', '10'),
(40, 'base de datos', '6');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sesiones`
--

CREATE TABLE `sesiones` (
  `id_sesion` int(11) NOT NULL,
  `fecha` varchar(12) NOT NULL,
  `hora_inicio` varchar(12) NOT NULL,
  `hora_fin` varchar(12) NOT NULL,
  `id_materia` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `sesiones`
--

INSERT INTO `sesiones` (`id_sesion`, `fecha`, `hora_inicio`, `hora_fin`, `id_materia`) VALUES
(28, '2021-05-29', '03:14', '05:14', 'base de datos'),
(29, '2021-05-08', '13:25', '14:25', 'base de datos'),
(31, '2021-05-08', '18:00', '19:00', 'programacion avanzada'),
(32, '2021-05-04', '19:02', '20:02', 'electiva profesional 1');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `materias`
--
ALTER TABLE `materias`
  ADD PRIMARY KEY (`id`) USING BTREE;

--
-- Indices de la tabla `sesiones`
--
ALTER TABLE `sesiones`
  ADD PRIMARY KEY (`id_sesion`) USING BTREE;

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `contacts`
--
ALTER TABLE `contacts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT de la tabla `materias`
--
ALTER TABLE `materias`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT de la tabla `sesiones`
--
ALTER TABLE `sesiones`
  MODIFY `id_sesion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
