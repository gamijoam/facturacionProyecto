-- --------------------------------------------------------
-- Host:                         localhost
-- Versión del servidor:         11.6.2-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.8.0.6908
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para inventario
CREATE DATABASE IF NOT EXISTS `inventario` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_uca1400_ai_ci */;
USE `inventario`;

-- Volcando estructura para tabla inventario.alertas
CREATE TABLE IF NOT EXISTS `alertas` (
  `id_alerta` int(11) NOT NULL AUTO_INCREMENT,
  `id_producto` int(11) DEFAULT NULL,
  `mensaje` text DEFAULT NULL,
  `fecha_alerta` datetime DEFAULT NULL,
  PRIMARY KEY (`id_alerta`),
  CONSTRAINT `FK_alertas_alertas` FOREIGN KEY (`id_alerta`) REFERENCES `alertas` (`id_alerta`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla inventario.categorias
CREATE TABLE IF NOT EXISTS `categorias` (
  `id_categoria` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT '0',
  `descripcion` text DEFAULT NULL,
  PRIMARY KEY (`id_categoria`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla inventario.detalle_venta
CREATE TABLE IF NOT EXISTS `detalle_venta` (
  `id_detalle` int(11) NOT NULL AUTO_INCREMENT,
  `id_venta` int(11) DEFAULT NULL,
  `id_producto` int(11) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `precio_unitario` decimal(10,2) DEFAULT NULL,
  `subtotal` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id_detalle`),
  KEY `FK_detalle_venta_ventas` (`id_venta`),
  KEY `FK_detalle_venta_productos` (`id_producto`),
  CONSTRAINT `FK_detalle_venta_productos` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id_productos`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_detalle_venta_ventas` FOREIGN KEY (`id_venta`) REFERENCES `ventas` (`id_venta`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla inventario.movimientos
CREATE TABLE IF NOT EXISTS `movimientos` (
  `id_movimiento` int(11) NOT NULL AUTO_INCREMENT,
  `id_producto` int(11) DEFAULT 0,
  `tipo_movimiento` enum('entrada','salida') DEFAULT NULL,
  `cantidad` int(11) DEFAULT 0,
  `fecha_movimiento` datetime DEFAULT NULL,
  `id_usuario` int(11) DEFAULT 0,
  `comentario` text DEFAULT NULL,
  PRIMARY KEY (`id_movimiento`),
  KEY `FK_movimientos_productos` (`id_producto`),
  KEY `FK_movimientos_usuarios` (`id_usuario`),
  CONSTRAINT `FK_movimientos_productos` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id_productos`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_movimientos_usuarios` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla inventario.productos
CREATE TABLE IF NOT EXISTS `productos` (
  `id_productos` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT '0',
  `descripcion` text DEFAULT NULL,
  `codigo_barras` varchar(50) DEFAULT '0',
  `precio_compra` decimal(10,2) DEFAULT 0.00,
  `stock_actual` decimal(10,2) DEFAULT 0.00,
  `stock_minimo` int(11) DEFAULT 0,
  `id_categoria` int(11) DEFAULT 0,
  `id_proveedor` int(11) DEFAULT 0,
  `fecha_creacion` datetime DEFAULT NULL,
  `fecha_actualizacion` datetime DEFAULT NULL,
  PRIMARY KEY (`id_productos`),
  KEY `FK_productos_categorias` (`id_categoria`),
  KEY `FK_productos_proveedores` (`id_proveedor`),
  CONSTRAINT `FK_productos_categorias` FOREIGN KEY (`id_categoria`) REFERENCES `categorias` (`id_categoria`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_productos_proveedores` FOREIGN KEY (`id_proveedor`) REFERENCES `proveedores` (`id_proveedores`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla inventario.proveedores
CREATE TABLE IF NOT EXISTS `proveedores` (
  `id_proveedores` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT '0',
  `telefono` varchar(20) DEFAULT '0',
  `email` varchar(100) DEFAULT '0',
  `direccion` text DEFAULT NULL,
  PRIMARY KEY (`id_proveedores`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla inventario.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT '0',
  `email` varchar(100) DEFAULT '0',
  `contrasena` varchar(225) DEFAULT '0',
  `rol` enum('admin','empleado') DEFAULT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla inventario.ventas
CREATE TABLE IF NOT EXISTS `ventas` (
  `id_venta` int(11) NOT NULL AUTO_INCREMENT,
  `fecha_venta` datetime DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL,
  `id_usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_venta`),
  CONSTRAINT `FK_ventas_usuarios` FOREIGN KEY (`id_venta`) REFERENCES `usuarios` (`id_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- La exportación de datos fue deseleccionada.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
