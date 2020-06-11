CREATE DATABASE  IF NOT EXISTS `castlevania_inventory_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `castlevania_inventory_db`;
-- MySQL dump 10.13  Distrib 8.0.20, for Linux (x86_64)
--
-- Host: localhost    Database: castlevania_inventory_db
-- ------------------------------------------------------
-- Server version	8.0.20-0ubuntu0.19.10.1

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
-- Table structure for table `ITEMS`
--

DROP TABLE IF EXISTS `ITEMS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ITEMS` (
  `ENTITY_ID` char(36) NOT NULL,
  `NAME` varchar(50) DEFAULT 'NAMELESS',
  `CATEGORY` varchar(50) DEFAULT 'STANDARD',
  `ITEM_TYPE` varchar(50) DEFAULT 'UNIQUE',
  `DESCRIPTION` varchar(1000) DEFAULT 'WITHOUT DESCRIPTION',
  `ATTRIBUTES` varchar(50) DEFAULT 'NONE',
  `CONSUME_MP` int DEFAULT '0',
  `CONSUME_HEART` int DEFAULT '0',
  `STATISTICS_HP` int DEFAULT '0',
  `STATISTICS_MP` int DEFAULT '0',
  `STATISTICS_HEART` int DEFAULT '0',
  `STATISTICS_STR` int DEFAULT '0',
  `STATISTICS_ATT` int DEFAULT '0',
  `STATISTICS_GOLD` int DEFAULT '0',
  `STATISTICS_CON` int DEFAULT '0',
  `STATISTICS_DEF` int DEFAULT '0',
  `STATISTICS_MAX_HT` int DEFAULT '0',
  `STATISTICS_INT` int DEFAULT '0',
  `STATISTICS_LCK` int DEFAULT '0',
  `STATISTICS_MAX_HP` int DEFAULT '0',
  `SELL` float DEFAULT '0',
  `FOUND_AT` varchar(100) DEFAULT 'NONE',
  `DROPPED_BY` varchar(100) DEFAULT 'NONE',
  `EFFECT` varchar(1000) DEFAULT 'WITHOUT EFFECT',
  `IMAGE` mediumblob NOT NULL,
  `ANIMATION` mediumblob NOT NULL,
  `SPECIAL_ANIMATION` mediumblob NOT NULL,
  PRIMARY KEY (`ENTITY_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ITEMS`
--

LOCK TABLES `ITEMS` WRITE;
/*!40000 ALTER TABLE `ITEMS` DISABLE KEYS */;
/*!40000 ALTER TABLE `ITEMS` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-09 16:09:16