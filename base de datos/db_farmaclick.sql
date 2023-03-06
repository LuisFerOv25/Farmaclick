-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 06-03-2023 a las 04:39:55
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `db_farmaclick`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE `categoria` (
  `id_categoria` int(11) NOT NULL,
  `nombre` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `categoria`
--

INSERT INTO `categoria` (`id_categoria`, `nombre`) VALUES
(1, 'cuidado personal'),
(2, 'dermacosmetico'),
(3, 'nutricionales'),
(4, 'bebe'),
(5, 'medicamentos');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `id_producto` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `descripcion` varchar(400) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `precio` double NOT NULL,
  `proveedor` varchar(45) NOT NULL,
  `fecha_vencimiento` date NOT NULL,
  `imagen` text NOT NULL,
  `categoria` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`id_producto`, `nombre`, `descripcion`, `cantidad`, `precio`, `proveedor`, `fecha_vencimiento`, `imagen`, `categoria`) VALUES
(3, 'talco', 'NaN', 5, 500, 'rexona', '2023-11-12', 'Entity Relationship Diagram.jpg', 4),
(8, 'maquillaje', 'NaN', 5, 5000, 'Nivea', '2023-12-15', 'EXPO ETICA.docx', 2),
(9, 'vitamina B', 'NaN', 7, 58000, 'Colpatria', '2026-11-12', 'carrera.xlsx', 3),
(10, 'tretinol', 'NaN', 5, 5799, 'axa', '2024-11-09', 'Entity Relationship Diagram.jpg', 5),
(11, 'desodorante', 'NaN', 20, 6000, 'NaN', '2023-11-12', 'martillb.blend', 1),
(12, 'Paracetamol', 'Alivia dolores de cabeza y fiebre', 50, 5.99, 'Laboratorios XYZ', '2024-06-30', 'Tabletas', 1),
(13, 'Ibuprofeno', 'Reduce la inflamación y el dolor', 75, 7.99, 'Laboratorios ABC', '2023-12-31', 'Cápsulas', 1),
(14, 'Acetaminofén', 'Alivia dolores leves y moderados', 100, 4.99, 'Laboratorios DEF', '2025-02-28', 'Tabletas', 1),
(15, 'Amoxicilina', 'Antibiótico para infecciones bacterianas', 25, 15.99, 'Laboratorios XYZ', '2022-10-31', 'Cápsulas', 2),
(16, 'Clindamicina', 'Antibiótico para infecciones de la piel y dentales', 30, 12.99, 'Laboratorios ABC', '2023-06-30', 'Cápsulas', 2),
(17, 'Fluconazol', 'Antifúngico para infecciones por hongos', 20, 8.99, 'Laboratorios GHI', '2024-04-30', 'Tabletas', 2),
(18, 'Omeprazol', 'Reduce la producción de ácido en el estómago', 60, 9.99, 'Laboratorios XYZ', '2023-08-31', 'Cápsulas', 3),
(19, 'Ranitidina', 'Alivia la acidez estomacal y úlceras', 40, 6.99, 'Laboratorios ABC', '2024-02-28', 'Tabletas', 3),
(20, 'Loperamida', 'Alivia la diarrea aguda', 50, 3.99, 'Laboratorios DEF', '2022-12-31', 'Cápsulas', 4),
(21, 'Metoclopramida', 'Alivia las náuseas y los vómitos', 35, 5.99, 'Laboratorios GHI', '2025-01-31', 'Tabletas', 4),
(22, 'aaaa', 'aaaa', 44, 666, 'axa', '2023-12-10', 'cdvdgdg', 1),
(23, 'crema 0', 'NaN', 5, 50000, 'Nivea', '2023-12-10', 'cohetee.jpg', 4),
(24, 'leche', 'nan', 8, 80000, 'colanta', '2025-11-10', 'coheteee.png', 4),
(25, 'leche ', 'vvvv', 55, 555555, 'vfdv', '2025-01-01', 'tarro.png', 4),
(26, 'leche2', 'bdgf', 6, 6000, 'sgfg', '2023-11-10', 'cohete.jpg', 4),
(27, 'gotas', 'NaN', 30, 5000, 'nivea', '2024-11-10', 'tarrgdfdgfo.png', 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `tipo_user` int(11) NOT NULL,
  `nombre` varchar(60) NOT NULL,
  `apellido` varchar(60) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `direccion` varchar(60) NOT NULL,
  `telefono` char(12) NOT NULL,
  `genero` varchar(20) NOT NULL,
  `password` text NOT NULL,
  `create_at` varchar(100) NOT NULL,
  `imagen` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `tipo_user`, `nombre`, `apellido`, `correo`, `direccion`, `telefono`, `genero`, `password`, `create_at`, `imagen`) VALUES
(1, 2, 'luis', 'oviedo', 'nan', 'luis45@gmail.com', '5555555555', 'M', 'sha256$AANyD2VAgb3FNw0H$79da655b19df5350b2240ca36eec09170b6c0a26824a41ac2e9a82a1ce60b9b0', '2023-02-16', ''),
(2, 2, 'momica', 'juarez', 'moinica@g.com', 'fngj', '3444444', 'F', 'sha256$0gGcYyslBhaaer6d$c0284b1bf5b8bbe4715b9d086a4c16c9a02f8ea85d69111a296b4a08e9984a9f', '2023-2-16', ''),
(3, 1, 'julia', 'norma', 'mz234', 'k@g.com', '3211111111', 'F', '', '', ''),
(6, 1, 'carlos', 'narvaez', 'gfh@g.com', 'sgdfhf', '1111222222', 'Male', 'sha256$ssWPEvpNE6A80zQF$908f23c351fec204110c6cae84ed389c52764fefa327d0d6671290d305c23515', '2023-2-17', ''),
(7, 2, 'juan', 'cordoba', 'juanc@gmail.com', 'bgfht5', '321555555', 'Masculino', 'sha256$zWsELssmlWg2xtym$46708311343c9f68edb241eb97011ccd956e9cafb5870d4caab0cd133a54d402', '2023-2-21', ''),
(8, 2, 'maria', 'lozano', 'mariloz@gmail.com', 'MZ44 CS45 ', '3214456789', 'F', 'sha256$MDRicZZFZN2grnnU$01d80ba5fdb6a3f00d3314c3b60060f9960d9dd266b4c59f3fe720bfff0981ef', '2023-2-22', ''),
(9, 1, 'Matias', 'Santos', 'matiasgf56@gmail.com', 'Calle 345', '3215676543', 'Male', 'sha256$85xrTbQ7ba8JVQTI$7b02312b9a6844f63208eb2f9a90ff9e9b97ad383d411eaffc4c348a51df597a', '2023-2-22', ''),
(10, 2, 'judas', 'gomez', 'judasgom@gmail.com', 'calle 467', '3278655555', 'M', 'sha256$0O0DyI1oBoyuaNgO$6f82badab0351f0f33aaf6b27f35c984b156bb253d64087c49117f13ae8d6a65', '2023-2-22', ''),
(11, 1, 'soledad', 'aspiro', 'soledad45@gmail.com', 'calle 567', '3214567877', 'F', 'sha256$c8HnKPqjv4H0ysVz$c3fea86fdd6e5b8f09778e1ae33ba0fed29e207e6ec3cd3c6f339b4693643694', '2023-2-22', ''),
(12, 0, 'Pérez', 'juanperez@example.com', 'Calle 123', '1234567890', 'M', 'secreto123', '10/11/23', '', ''),
(13, 0, 'García', 'mariagarcia@example.com', 'Avenida 456', '0987654321', 'F', 'contraseña123', '10/11/23', '', ''),
(14, 0, 'Martínez', 'pedromartinez@example.com', 'Plaza 789', '1122334455', 'M', 'password123', '10/11/23', '', ''),
(15, 0, 'López', 'analo@example.com', 'Calle 987', '5544332211', 'F', 'contraseña123', '10/11/23', '', ''),
(16, 0, 'Hernández', 'miguelhernandez@example.com', 'Avenida 654', '6677889900', 'M', 'secreto123', '10/11/23', '', ''),
(17, 0, 'Ruiz', 'sofiaruiz@example.com', 'Plaza 321', '4433221100', 'F', 'password123', '10/11/23', '', ''),
(18, 0, 'Sánchez', 'luciasanchez@example.com', 'Calle 456', '9988776655', 'F', 'contraseña123', '10/11/23', '', ''),
(19, 0, 'Gómez', 'jorgegomez@example.com', 'Avenida 789', '1122334455', 'M', 'secreto123', '10/11/23', '', ''),
(20, 0, 'Fernández', 'luisfernandez@example.com', 'Plaza 123', '6677889900', 'M', 'password123', '10/11/23', '', ''),
(21, 0, 'Díaz', 'carladiaz@example.com', 'Calle 456', '5544332211', 'F', 'contraseña123', '10/11/23', '', ''),
(22, 1, 'pedro', 'orso', 'gddfh@g.com', 'vsdfdf', '2222222222', 'M', 'sha256$IcfWO2jQZb9i0Hp6$d4f924785fc1f29de728686de06040e3978f3a1cc8cc546dab9b828b16acdc83', '2023-3-5', ''),
(23, 1, 'matias', 'gosefo', 'matias45@gmail.com', 'ma3435', '3211111111', 'M', 'sha256$aNLRfHl7pu10gEKK$6bb48f331be437cf6ccd33cd3c48842a9abbdbd9ee5e5b3b773e73cb50dd9703', '2023-3-5', NULL),
(24, 1, 'josefina', 'ordoñez', 'josefina45@gmail.com', 'mz234-545', '3211111111', 'F', 'sha256$2uZzsc9yVimbEzyk$0a209c9824f8f63bf85081f93c35daa92a2d180bf57eae0a47a88c0f426c3851', '2023-3-5', 'tarrgdfdgfgdgfo.png'),
(25, 2, 'juliana', 'perez', 'julivsg56@gmail.com', 'mz13334', 'julisf5@g.co', 'M', 'sha256$hwqWGzkGrpmkBiLv$e36b689f26f8652b40b1269a3b8f302654ce51a1390486095bd7d64ca18ba8e3', '2023-3-5', NULL),
(26, 1, 'julio', 'perez', 'julioper@gmail.com', 'vfg45', '322111111', 'M', 'sha256$x2jDpMZPhRDUydMp$43a4a6e042069f7decca825ca502aed6a81b4580e2392b08eee47d888e39f620', '2023-3-5', 'app/static/uploads/user.png'),
(27, 1, 'nathalie', 'ursuga', 'nathal45@gmail.com', 'vdgbf45', '3008887777', 'F', 'sha256$ljDp4ehfUN5BjVcU$1e8a4542a7571522c8184d2d87d1ea10d3be90bac7d28f3074ef0798b76b59ba', '2023-3-5', NULL),
(28, 1, 'carlos', 'torres', 'carlosang@g.com', 'angola344', '3211111111', 'M', 'sha256$zYcT04Ank0JRGcv8$a383783285d10d7d407d5207e503f16e6b5d69a63009b98a855493110b75816b', '2023-3-5', 'app/static/uploadsuffsver.png'),
(29, 1, 'antonela', 'perez', 'antonel@g.com', 'fsfs1243', '3211111111', 'F', 'sha256$dVdZfDOX4e8yX2oh$9320e94cf0dec3bb2ea94d1e9df00d0fc831bf550419aec341c730c06b4f4da6', '2023-3-5', 'uffsdgfgver.png'),
(30, 1, 'perla', 'gomez', 'perla45@gmail.com', 'antorres', '3211111111', 'F', 'sha256$kvEtzksMzvFNoOAG$9013752c30f24681bcf8b2159c32d771830b7323e6a7dee043f3cce5b185c395', '2023-3-5', 'perlita.png'),
(31, 1, 'joseus', 'gomez', 'joseus45@g.com', 'mad234', '1111111111', 'M', 'sha256$sv7cLW3lFxqSHJKg$b93a5b94ca27fc884a2f3ba802e0ede7b3da4601cd6f9d105e581424671fa70e', '2023-3-5', NULL),
(32, 1, 'maria', 'loza', 'marialoza5@g.com', 'fsf34', '3166666668', 'F', 'sha256$UxMcKSMnSqPdp3ks$ce2162641439426acb256298802da376f9b8a344bf361d49473edbb050f47731', '2023-3-5', 'app/static/uploadsmaia.png'),
(33, 1, 'luna', 'cesleste', 'lunacel45@gmail.com', 'mz3466', '3124445678', 'F', 'sha256$wcTIWg5v3SgY6Apf$c9ee743a1702ba77f4b55b81aacd01c8866a15c1986611e3419853625ece61f8', '2023-3-5', 'app/static/uploads/lunacel.png');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`id_categoria`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`id_producto`),
  ADD KEY `categoria` (`categoria`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `categoria`
--
ALTER TABLE `categoria`
  MODIFY `id_categoria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
  MODIFY `id_producto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `producto`
--
ALTER TABLE `producto`
  ADD CONSTRAINT `producto_ibfk_1` FOREIGN KEY (`categoria`) REFERENCES `categoria` (`id_categoria`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
