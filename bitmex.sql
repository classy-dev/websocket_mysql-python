/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.3.15-MariaDB : Database - bixmex
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`bixmex` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `bixmex`;

/*Table structure for table `liquidations` */

DROP TABLE IF EXISTS `liquidations`;

CREATE TABLE `liquidations` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `action` varchar(255) DEFAULT NULL,
  `orderid` varchar(255) DEFAULT NULL,
  `symbol` varchar(50) DEFAULT NULL,
  `side` varchar(255) DEFAULT NULL,
  `price` double(15,3) DEFAULT NULL,
  `leavesQty` double(15,3) DEFAULT NULL,
  `timestamps` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `liquidations` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
