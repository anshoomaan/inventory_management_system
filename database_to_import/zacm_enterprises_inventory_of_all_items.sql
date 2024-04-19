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
-- Table structure for table `inventory_of_all_items`
--

DROP TABLE IF EXISTS `inventory_of_all_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory_of_all_items` (
  `ITEM_ID` int NOT NULL AUTO_INCREMENT,
  `DEPT_ID` varchar(5) NOT NULL,
  `ITEM_NAME` varchar(45) NOT NULL,
  `ITEM_PRICE` int NOT NULL,
  `QUANTITY` int NOT NULL,
  `STATUS` varchar(3) NOT NULL,
  PRIMARY KEY (`ITEM_ID`),
  UNIQUE KEY `ITEM_ID_UNIQUE` (`ITEM_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=107 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory_of_all_items`
--

LOCK TABLES `inventory_of_all_items` WRITE;
/*!40000 ALTER TABLE `inventory_of_all_items` DISABLE KEYS */;
INSERT INTO `inventory_of_all_items` VALUES (1,'31#01','Laptop',50000,100,'IN'),(2,'31#02','Cake',7500,60,'IN'),(3,'31#03','Shirt',500,900,'IN'),(4,'31#01','T.V',10000,0,'OUT'),(5,'31#02','Chips',10,0,'OUT'),(6,'31#03','Pent',500,0,'OUT'),(7,'31#01','Rice Cooke',606,0,'OUT'),(8,'31#02','Cereal',810,57,'IN'),(9,'31#03','Baseball C',871,0,'OUT'),(10,'31#01','Smart Pani',858,61,'IN'),(11,'31#01','Electric G',903,85,'IN'),(12,'31#01','Meat Therm',888,97,'IN'),(13,'31#01','Toaster',985,66,'IN'),(14,'31#03','Overalls',817,0,'OUT'),(15,'31#01','Air Purifi',625,0,'OUT'),(16,'31#03','Snapback',898,76,'IN'),(17,'31#02','Muffins',741,0,'OUT'),(18,'31#01','Smart Food',777,74,'IN'),(19,'31#03','Tuxedo',992,0,'OUT'),(20,'31#02','Curry',530,0,'OUT'),(21,'31#02','Creme Brul',572,70,'IN'),(22,'31#01','Electric K',883,83,'IN'),(23,'31#01','Smart Ice ',805,0,'OUT'),(24,'31#03','Hair Clip',603,0,'OUT'),(25,'31#03','Cargo Pant',507,81,'IN'),(26,'31#02','Fish and C',810,72,'IN'),(27,'31#01','Smart Toas',934,0,'OUT'),(28,'31#01','Stand Mixe',977,0,'OUT'),(29,'31#01','Electric G',934,0,'OUT'),(30,'31#01','Toaster Ov',955,63,'IN'),(31,'31#01','Smart Oven',746,81,'IN'),(32,'31#03','Jeans',614,96,'IN'),(33,'31#03','Wrap Dress',921,57,'IN'),(34,'31#02','Meringue',770,0,'OUT'),(35,'31#03','Swimsuit',728,78,'IN'),(36,'31#03','Parka',684,0,'OUT'),(37,'31#02','Tapenade',640,94,'IN'),(38,'31#03','Corduroys',564,62,'IN'),(39,'31#02','Churros',664,0,'OUT'),(40,'31#01','Smart Pani',672,65,'IN'),(41,'31#02','Croissant',669,0,'OUT'),(42,'31#01','Smart Food',992,0,'OUT'),(43,'31#03','Jacket',635,0,'OUT'),(44,'31#03','Button-up ',583,0,'OUT'),(45,'31#03','Hair Tie',584,73,'IN'),(46,'31#03','Necktie',897,0,'OUT'),(47,'31#01','Seltzer Ma',507,0,'OUT'),(48,'31#01','Smart Air ',570,0,'OUT'),(49,'31#03','Wrap Dress',776,0,'OUT'),(50,'31#02','Pita Bread',783,0,'OUT'),(51,'31#03','Parka',888,0,'OUT'),(52,'31#03','Sweat Vest',958,0,'OUT'),(53,'31#03','Cargo Pant',876,97,'IN'),(54,'31#01','Induction ',793,50,'IN'),(55,'31#03','Parka',762,0,'OUT'),(56,'31#03','Shorts',842,59,'IN'),(57,'31#02','Ciabatta',888,56,'IN'),(58,'31#03','Blazer',652,0,'OUT'),(59,'31#03','Robe',706,0,'OUT'),(60,'31#02','Empanadas',983,0,'OUT'),(61,'31#01','Smart Dish',731,0,'OUT'),(62,'31#03','Tank Top',710,72,'IN'),(63,'31#03','Belt',967,0,'OUT'),(64,'31#01','Smart Elec',980,0,'OUT'),(65,'31#02','Escargot',858,0,'OUT'),(66,'31#03','Formal Wea',787,57,'IN'),(67,'31#02','Biscotti',710,0,'OUT'),(68,'31#02','Mousse',821,0,'OUT'),(69,'31#02','Sushi',681,0,'OUT'),(70,'31#01','Blender',626,0,'OUT'),(71,'31#01','Smart Grai',629,0,'OUT'),(72,'31#01','Electric S',756,67,'IN'),(73,'31#01','Smart Food',878,69,'IN'),(74,'31#02','Muffins',892,0,'OUT'),(75,'31#02','Crepes',789,0,'OUT'),(76,'31#02','Pumpernick',604,70,'IN'),(77,'31#03','Robe',910,89,'IN'),(78,'31#01','Food Slice',545,72,'IN'),(79,'31#02','Wings',719,73,'IN'),(80,'31#03','Gloves',860,0,'OUT'),(81,'31#01','Bread Make',647,79,'IN'),(82,'31#03','Capris',941,64,'IN'),(83,'31#03','Biker Jack',556,0,'OUT'),(84,'31#03','Ascot Tie',777,65,'IN'),(85,'31#01','Smart Blen',711,100,'IN'),(86,'31#02','Tzatziki',560,0,'OUT'),(87,'31#02','Salsa',862,0,'OUT'),(88,'31#02','Tzatziki',994,0,'OUT'),(89,'31#02','Pita Bread',985,65,'IN'),(90,'31#03','Wrap Dress',787,80,'IN'),(91,'31#01','Stand Mixe',578,0,'OUT'),(92,'31#03','Fur Coat',919,89,'IN'),(93,'31#03','Sweat Vest',566,91,'IN'),(94,'31#01','Kitchen Sc',510,93,'IN'),(95,'31#03','Beanie',609,0,'OUT'),(96,'31#01','Blender',563,0,'OUT'),(97,'31#02','Truffles',652,94,'IN'),(98,'31#02','Gingerbrea',756,0,'OUT'),(99,'31#03','Hair Clip',812,58,'IN'),(100,'31#02','Nachos',724,84,'IN'),(101,'31#03','Pencil Ski',602,95,'IN'),(102,'31#02','Pita Bread',824,0,'OUT'),(103,'31#02','Churros',759,0,'OUT'),(104,'31#03','Jeans',633,68,'IN'),(105,'31#01','Smart Popc',845,0,'OUT'),(106,'31#02','Pita Bread',729,73,'IN');
/*!40000 ALTER TABLE `inventory_of_all_items` ENABLE KEYS */;
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
