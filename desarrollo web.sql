-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: desarrollo_web1
-- ------------------------------------------------------
-- Server version	8.0.41

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
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos` (
  `id_producto` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `stock` int NOT NULL,
  PRIMARY KEY (`id_producto`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES (1,'teclado modificado',10.00,9),(3,'memoria ',8.00,15),(4,'USB',7.00,25),(5,'Monitor de 17\"editado',100.00,50),(11,'mochila lenovo',25.00,3);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `idusuarios` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`idusuarios`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'carmen','carmen123@gmail.com','scrypt:32768:8:1$uzJKn8jiLOOAbIqN$2ef3e1ce7bf8b1268fb7123ceae96f80eb08cc076e9090a430471125deb4abf0991d54fcd4e4e8194f8fd2efc4979b2beb67cff87706bb3664d205b446519083'),(2,'susana','susana1@gmail.com','scrypt:32768:8:1$a6B5uKjiCfodVJCb$a825ebbd3fcd521d6b1f0dfaf5ecc13d7367a1d210d5b1f3c26885f9f4184d3e8101be501846394327b266a513ed08d63327be8ba068fe325e89d862258ee7c5'),(3,'carmen','carmen1@gmail.com','scrypt:32768:8:1$Gk2Su76vPh1IaXno$7600a6c5dbe430cad286b8748ab2b92fda1b915ff22e79f0ff9fe307ef60c93c20f75a2c882d9da15b89c09d5a9544830f2ff5303352f290ee6227d41a71f8a0'),(6,'jessica','jessica1@gmail.com','scrypt:32768:8:1$ndU3IuYKQpHOmyQo$cfcf386c4815d4b7afa293c4b88fd6b514221bfba851b5abda2dfff2a632ab4c3ce7a6f078876e33b6dfe02238dc5ac057c28d939918515b51b45dc7f415201b'),(7,'maria','maria1@gmail.com','scrypt:32768:8:1$bDwNNEL9P9loUoYr$cb2c7276232e1f661e16a1fc8f9790bdd05e1750e21b62413d85665a41fbef6eb3dfb14a653209db4cc399c8da9d04ab3099309b21d042686a3877a7232c9456'),(8,'susana','susana1@gmail.com','scrypt:32768:8:1$O6qfxEuncskArsCD$92d120d5e1eb7eae18934c67e95b2b2b5d67529e20a7481d4dc04cf156f88bd6d3feed2cf75f882de53c788bb10a4d30fc008c7298280581a1b6e458360f99ea'),(9,'cristian','cristian1@gmail.com','scrypt:32768:8:1$u9XqZsUvWpeSQyd6$565346eb4c2b118098b85eae262bb762ef31973ee68d48e8a4683b0a4874719a9dd5373ac295a3bd2ee4ef0527d27436a176d93fc377309f77bca7ead87e990f'),(10,'susana','susana1@gmail.com','scrypt:32768:8:1$z1eac1X22DBHo8P3$7a237a1e7d55cc8d303df8adbeeffef8f593dc98c641913f570c8f0c41db753368fb960674ec07117cb10276c8e2a7e32e9766424d41df83984ef6992ed7423c'),(11,'carmen','carmen@gmail.com','scrypt:32768:8:1$Uu9SCd3090TbvIrO$8d31d521017be9eb1a50c4a04a56d0f2f88b807c6ea883b286d960149f2f2e7752deebf805cc973b3728b4ceffd83328d9da039fadb74a89c5c1168176372b7c'),(12,'juan','juan1@gmail.com','scrypt:32768:8:1$5CJ0F7SYLXemzWA8$a1fe5fc598d85fce21198d5d1f71c4b51d7c8e9cc27913c3c58d232c6f2d8583991a2cd71ba87438e220635d182843d91f63099df9910079bde55c8b9d8f4d7a'),(13,'pedro','pero@gmail.com','scrypt:32768:8:1$V6PFgTfCGpEITBIj$9b7d988bf1e7ef4fffcd6fb6aa9f7e8a63960642efc52b6c8364a9a0362a17e3349bcfe552345fd43281f0c72d235fe978646ccb15a8876880e1f8636451af1f'),(14,'cristofer','cristofer@gmail.com','scrypt:32768:8:1$9WepLs1d7zHx18KQ$c60b6e362609c3f04d4f92dda33ab16ae187755f4eb1cb5f2e5f08b6f1f9cdf365971aa355010a755938850e31bf96d85fc2c9936cc8850f146761018fca8ddc'),(15,'irlanda','irlanda@gmail.com','scrypt:32768:8:1$F6TpitYG56gpAKNa$0fb1265eed75e9aa4c9bcd8b25a0a175b12da270fd832e9eeb29f86b2f262aebb9cc2adeda48a174cf5db804bde6e5dc574f23e78427c1ad1dfd3477aaaf60c2'),(16,'karina','karina@gmail.com','scrypt:32768:8:1$HyVWWLB2zsrMqWKr$278450f7d21e68bef2e9264c840659dd7d27620248375ca59f623153dc513db43360d36fefc4d6e33cef387b4e418cafeb2cc3214fa6ae06661f490abf692047'),(17,'zoila','zoila@gmail.com','scrypt:32768:8:1$twzhHGEqu9kBvZ4P$95eeecba384a8a5e28ec8a45d844399bdcdf3e3c64c74af98b9d383f0b2977988e67167e1eea8bee8af1e8ebf0abca02d5090f0952e5f447a2637664c34a4f4b'),(18,'carmen','carmens@gmail.com','scrypt:32768:8:1$daSVSagyVIYQXzfF$513b4498f61ab21c05b19cc9237c74c6271dafc228e76fdeed03e0255187c1951ca3b052a5e04d0d29faaf705853e9e09a5cf2c3a27a215beb95b5491a0857b1');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-02 18:23:40
