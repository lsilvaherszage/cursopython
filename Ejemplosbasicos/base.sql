/*
SQLyog Ultimate v8.61 
MySQL - 5.7.31 : Database - personal
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

USE `personal2`;

/*Table structure for table `alumnos` */

DROP TABLE IF EXISTS `alumnos`;

CREATE TABLE `alumnos` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Apellido` char(30) DEFAULT NULL,
  `Nombres` char(50) DEFAULT NULL,
  `fechanac` date DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

/*Data for the table `alumnos` */

insert  into `alumnos`(`Id`,`Apellido`,`Nombres`,`fechanac`) values (1,'Zabala','Gonzalo','1970-05-11'),(2,'Lopez','Clara','1980-05-23'),(3,'Perez','María','0000-00-00'),(4,'Martinez','Jorge','1990-09-22'),(5,'Gutierrez','Juan Carlos','1960-11-02'),(6,'Gutierrez','Juan Carlos','1960-11-02');

/*Table structure for table `notas` */

DROP TABLE IF EXISTS `notas`;

CREATE TABLE `notas` (
  `idAlu` int(11) DEFAULT NULL,
  `idMat` int(11) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `nota` int(2) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

/*Data for the table `notas` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
