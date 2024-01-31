CREATE DATABASE  IF NOT EXISTS `zoomanagementsystem` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `zoomanagementsystem`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: zoomanagementsystem
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
-- Table structure for table `zoo_area_info`
--

DROP TABLE IF EXISTS `zoo_area_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `zoo_area_info` (
  `Area_ID` int NOT NULL AUTO_INCREMENT,
  `Area_Name` varchar(255) NOT NULL,
  `Area_Type` varchar(255) NOT NULL,
  `Capacity` int NOT NULL,
  `Current_Count` int NOT NULL,
  PRIMARY KEY (`Area_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zoo_area_info`
--

LOCK TABLES `zoo_area_info` WRITE;
/*!40000 ALTER TABLE `zoo_area_info` DISABLE KEYS */;
INSERT INTO `zoo_area_info` VALUES (1,'熊猫馆','室内',10,3),(2,'狮子园','室外',15,5),(3,'草原区','室外',20,8),(4,'长颈鹿馆','室内',12,4),(5,'虎山','室外',18,6),(6,'熊猫馆','室内',10,3),(7,'狮子园','室外',15,5),(8,'草原区','室外',20,8),(9,'长颈鹿馆','室内',12,4),(10,'虎山','室外',18,6),(11,'熊猫馆','室内',10,3),(12,'狮子园','室外',15,5),(13,'草原区','室外',20,8),(14,'长颈鹿馆','室内',12,4),(15,'虎山','室外',18,6),(16,'熊猫馆','室内',10,3),(17,'狮子园','室外',15,5),(18,'草原区','室外',20,8),(19,'长颈鹿馆','室内',12,4),(20,'虎山','室外',18,6);
/*!40000 ALTER TABLE `zoo_area_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-09  0:06:06
