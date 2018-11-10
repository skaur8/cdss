-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: cdss
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `optical_disorder`
--

DROP TABLE IF EXISTS `optical_disorder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `optical_disorder` (
  `s_no` int(5) DEFAULT NULL,
  `disorder` varchar(50) DEFAULT NULL,
  `symptoms` varchar(50) DEFAULT NULL,
  `medication` varchar(50) DEFAULT NULL,
  `Age_Start` int(10) DEFAULT NULL,
  `Age_End` int(10) DEFAULT NULL,
  `Medical_History` varchar(50) DEFAULT NULL,
  `Severity` int(5) DEFAULT NULL,
  `Gender` varchar(7) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `optical_disorder`
--

LOCK TABLES `optical_disorder` WRITE;
/*!40000 ALTER TABLE `optical_disorder` DISABLE KEYS */;
INSERT INTO `optical_disorder` VALUES (1,'Eye Strain','Weary Eyes','Sleep and Rest',19,40,NULL,NULL,NULL),(1,'Eye Strain','Strain','Sleep and Rest',19,40,NULL,NULL,NULL),(2,'Red Eyes','Blood Shot Eyes','Eye Drops and Rest',NULL,NULL,'Tuberculosis/Syphilis',NULL,NULL),(2,'Red Eyes','Irritation','Eye Drops and Rest',NULL,NULL,'Arthritis',NULL,NULL),(2,'Red Eyes','Infection','Eye Drops and Rest',NULL,NULL,'Hypertension',NULL,NULL),(2,'Red Eyes','Pink eye','Eye Drops and Rest',NULL,NULL,NULL,NULL,NULL),(3,'Night Blindness','Partial Blindness','Vitamin A Supplements',NULL,NULL,'Vitamin A deficiency',NULL,NULL),(3,'Night Blindness','Cataract','Vitamin A Supplements',NULL,NULL,'Vitamin A deficiency',NULL,NULL),(3,'Night Blindness','Near Sightedness','Vitamin A Supplements',NULL,NULL,'Vitamin A deficiency',NULL,NULL),(3,'Night Blindness','Keratoconus','Vitamin A Supplements',NULL,NULL,'Vitamin A deficiency',NULL,NULL),(4,'Lazy Eye','Under development of one eye','Corrective glasses',NULL,NULL,'Nearsightedness/Farsightedness',NULL,NULL),(4,'Lazy Eye','Slower movement of one eye','Contacts or Eye Patches',NULL,NULL,'Astigmatism',NULL,NULL),(17,'Strabismus','Eyes don`t line up while focusing on one object','Vision Therapy',NULL,NULL,'Down Syndrome',NULL,NULL),(5,'Nystagmus/Cross Eyes','Jiggling of eyes on it`s own','Corrective surgery',NULL,NULL,'Brain disease/Head Injury',NULL,NULL),(8,'Presbyopia','unable to clearly view small text/objects','LASIK/Reading glasses/Contact Lenses',35,100,'Diabetes/Multiple Sclerosis',NULL,NULL),(9,'Floaters','Tiny spots/specks floating across vision','LASER treatment to disrupt the floaters',45,100,'Cataract surgery/Diabetes',NULL,NULL),(9,'Floaters','Dark curtain like vision','Surgery to remove the vitreous',45,100,'Cataract surgery/Diabetes',NULL,NULL),(10,'Dry Eyes','Extreme Dryness','Eye drops/Eye plugs',NULL,NULL,'Rheumatoid Arthritis',NULL,NULL),(10,'Dry Eyes','BUrning sensation','In-home humidifier/Testosterone eyelid cream',NULL,NULL,'Rheumatoid Arthritis',NULL,NULL),(11,'Excess Tearing','Sensitive to changes in light/wind/temperature','Sunglasses',NULL,NULL,'Conjunctivitis',NULL,NULL),(11,'Excess Tearing','Blocked tear duct/Infection','Eye drops',NULL,NULL,'Conjunctivitis',NULL,NULL),(12,'Cataract','Cloudy Vision','Cataract Surgery',40,100,'Diabetes',NULL,NULL),(12,'Cataract','Glary and halo visions in dark','Cataract Surgery',40,100,'Obesity/Hypertension',NULL,NULL),(13,'Glaucoma','High pressure in optic nerves/injury to eye','Eye drops/Surgery',40,100,'Diabetes',NULL,NULL),(13,'Glaucoma','Blocked blood vessels','Eye drops/Surgery',40,100,'Diabetes',NULL,NULL),(13,'Glaucoma','INflammatory disorders of eye','Eye drops/Surgery',40,100,'Diabetes',NULL,NULL),(14,'Macular degeneration','Breakdown of small portion of retina(macula)','Macular degeneration treatment',60,100,'Hypertension/obesity',NULL,NULL),(15,'Diabetic reneopathy','Damage to blood vessels due to diabetes','Photocoagulation',20,64,'Hypertension/diabetes/Higher Cholestrol',NULL,NULL),(16,'Conjuctivitis','Sclera covering inflammation','Wash hands properly/Eyedrops',NULL,NULL,NULL,NULL,NULL),(16,'Conjuctivitis','Redness/Tearing/Itching','Wash hands properly/Eyedrops',NULL,NULL,NULL,NULL,NULL),(16,'Conjuctivitis','Feeling of presence of some object in eye','Wash hands properly/Eyedrops',NULL,NULL,NULL,NULL,NULL),(7,'Uveitis','Inflammation of uvea','Steroid drops/injection/pills',1,100,'Rheumatoid Arthritis',NULL,NULL),(7,'Uveitis','Blurred vision, Eye sensitivity','Steroid drops/injection/pills',1,100,'Rheumatoid Arthritis',NULL,NULL),(6,'Colour Blindness','Unable to recognize color/shades','Contacts/Glasses with filters',5,102,'Accident/Genetics',NULL,NULL);
/*!40000 ALTER TABLE `optical_disorder` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-09 22:49:55
