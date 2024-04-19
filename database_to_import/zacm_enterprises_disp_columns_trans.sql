CREATE DATABASE  IF NOT EXISTS `zacm_enterprises` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `zacm_enterprises`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: zacm_enterprises
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `disp_columns_trans`
--

DROP TABLE IF EXISTS `disp_columns_trans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `disp_columns_trans` (
  `a` varchar(45) NOT NULL,
  `b` varchar(45) NOT NULL,
  `c` varchar(45) NOT NULL,
  `d` varchar(45) NOT NULL,
  `e` varchar(45) NOT NULL,
  `f` varchar(45) NOT NULL,
  `g` varchar(45) NOT NULL,
  PRIMARY KEY (`a`),
  UNIQUE KEY `a_UNIQUE` (`a`),
  UNIQUE KEY `b_UNIQUE` (`b`),
  UNIQUE KEY `c_UNIQUE` (`c`),
  UNIQUE KEY `d_UNIQUE` (`d`),
  UNIQUE KEY `f_UNIQUE` (`f`),
  UNIQUE KEY `e_UNIQUE` (`e`),
  UNIQUE KEY `g_UNIQUE` (`g`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `disp_columns_trans`
--

LOCK TABLES `disp_columns_trans` WRITE;
/*!40000 ALTER TABLE `disp_columns_trans` DISABLE KEYS */;
INSERT INTO `disp_columns_trans` VALUES ('TRANS_ID','ITEM_ID','DEPT_ID','ITEM_NAME','ITEM_PRICE','SOLD_NO.','UNITS_LEFT');
/*!40000 ALTER TABLE `disp_columns_trans` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-19 18:18:56
