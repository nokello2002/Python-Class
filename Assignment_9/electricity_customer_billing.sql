-- MySQL dump 10.13  Distrib 8.0.24, for Win64 (x86_64)
--
-- Host: localhost    Database: electricity
-- ------------------------------------------------------
-- Server version	8.0.24

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
-- Table structure for table `customer_billing`
--

DROP TABLE IF EXISTS `customer_billing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer_billing` (
  `Billing_Month` int DEFAULT NULL,
  `Billing_Year` int DEFAULT NULL,
  `CustomerID` int DEFAULT NULL,
  `Units_Utilized` float DEFAULT NULL,
  `Unit_Price` float DEFAULT NULL,
  `Item_Price` float DEFAULT NULL,
  `Discount_Rate` float DEFAULT NULL,
  `Discount` float DEFAULT NULL,
  `Discounted_Amount` float DEFAULT NULL,
  `State_VAT` float DEFAULT NULL,
  `Nominal_VAT` float DEFAULT NULL,
  `Total_Cost` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_billing`
--

LOCK TABLES `customer_billing` WRITE;
/*!40000 ALTER TABLE `customer_billing` DISABLE KEYS */;
INSERT INTO `customer_billing` VALUES (1,2021,1,521,15,7815,0.07,547.05,7267.95,726.795,290.718,8285.46),(2,2021,1,450,15,6750,0.03,202.5,6547.5,654.75,261.9,7464.15),(1,2021,2,685,23,15755,0.09,1417.95,14337,2150.56,573.482,17061.1);
/*!40000 ALTER TABLE `customer_billing` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-14 16:57:29
