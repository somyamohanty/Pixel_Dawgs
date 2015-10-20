-- phpMyAdmin SQL Dump
-- version 3.5.3
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Oct 20, 2015 at 12:15 AM
-- Server version: 5.5.28-log
-- PHP Version: 5.3.8

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `svk38`
--

-- --------------------------------------------------------

--
-- Table structure for table `image`
--

CREATE TABLE IF NOT EXISTS `image` (
  `ind` int(11) NOT NULL AUTO_INCREMENT,
  `imgid` bigint(50) NOT NULL,
  `tag1` varchar(50) DEFAULT NULL,
  `tag2` varchar(50) DEFAULT NULL,
  `tag3` varchar(50) DEFAULT NULL,
  `tag4` varchar(50) DEFAULT NULL,
  `tag5` varchar(50) DEFAULT NULL,
  `tag1c` varchar(50) DEFAULT NULL,
  `tag2c` varchar(50) DEFAULT NULL,
  `tag3c` varchar(50) DEFAULT NULL,
  `tag4c` varchar(50) DEFAULT NULL,
  `tag5c` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ind`),
  KEY `index` (`ind`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `image`
--

INSERT INTO `image` (`ind`, `imgid`, `tag1`, `tag2`, `tag3`, `tag4`, `tag5`, `tag1c`, `tag2c`, `tag3c`, `tag4c`, `tag5c`) VALUES
(1, 2409783581, 'askdkjn', 'jjnfd', 'wjkdf', 'faliwjbb', 'WKJDFN', '294:258,', '185:287,152:275,', '301:310,238:316,', '288:351,290:358,310:334,227:286,232:279,', '316:479,41:416,26:268,165:464,'),
(2, 144613684, 'askdkjn', 'jjnfd', 'wjkdf', 'faliwjbb', 'WKJDFN', '80:150,', '227:174,112:352,93:220,', '243:60,114:340,', '85:438,26:372,72:67,139:304,54:429,49:426,85:333,2', ''),
(3, 146525965, 'a', 'b', 'c', 'd', 'e', '200:204,216:251,225:225,', '205:345,180:209,', '207:373,', '', '192:431,'),
(4, 443651623, NULL, NULL, NULL, NULL, NULL, '369:169,303:166,', '111:42,', '61:238,', '342:370,', ''),
(5, 54914084, 'awjsdf', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
