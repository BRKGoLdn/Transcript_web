-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 27 Haz 2023, 13:12:17
-- Sunucu sürümü: 10.4.28-MariaDB
-- PHP Sürümü: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `sis_transcript`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `courses`
--

CREATE TABLE `courses` (
  `id` int(11) NOT NULL,
  `school_id` int(255) NOT NULL,
  `course_id` int(255) NOT NULL,
  `academic_year` int(255) NOT NULL,
  `grade` int(255) NOT NULL,
  `course_name` varchar(255) NOT NULL,
  `credits` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `data`
--

CREATE TABLE `data` (
  `id` int(11) NOT NULL,
  `student_id` int(255) NOT NULL,
  `student_name` varchar(255) NOT NULL,
  `ayear_id` int(255) NOT NULL,
  `ayear` int(255) NOT NULL,
  `grade_id` int(255) NOT NULL,
  `grade` int(255) NOT NULL,
  `course_id` int(255) NOT NULL,
  `course_name` varchar(255) NOT NULL,
  `year_total` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `scale`
--

CREATE TABLE `scale` (
  `min` int(255) NOT NULL,
  `max` int(255) NOT NULL,
  `letter` varchar(255) NOT NULL,
  `GPA` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `schools`
--

CREATE TABLE `schools` (
  `school_id` int(255) NOT NULL,
  `school_name` varchar(255) NOT NULL,
  `country` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `schools`
--

INSERT INTO `schools` (`school_id`, `school_name`, `country`) VALUES
(1, 'Salahaldin International School', 'Egypt');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `students`
--

CREATE TABLE `students` (
  `id` int(11) NOT NULL,
  `student_id` int(255) NOT NULL,
  `student_name` varchar(255) NOT NULL,
  `birth_date` date NOT NULL,
  `gender` varchar(255) NOT NULL,
  `nationality` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Tablo döküm verisi `students`
--

INSERT INTO `students` (`id`, `student_id`, `student_name`, `birth_date`, `gender`, `nationality`) VALUES
(1, 2952, 'Arda Abdullah Tuncer', '2007-04-24', 'Male', 'Turkish'),
(2, 2157, 'Halil Sedat Yilmaz', '1007-08-23', 'Male', 'Turkish'),
(3, 2556, 'Bekir Berk Altunbas', '2008-01-14', 'Male', 'Turkish');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `surname` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `users`
--

INSERT INTO `users` (`id`, `email`, `name`, `surname`, `password`, `role`) VALUES
(1, 'arda.ab.tuncer@gmail.com', 'Arda Abdullah ', 'Tuncer', 'Arda123\r\n', 'Admin'),
(2, 'hsedaty@gmail.com', 'Halil Sedat', 'Yilmaz', 'Sedat123', 'Admin'),
(3, 'bekirberkaltunbas21@gmail.com', 'Bekir Berk', 'Altunbas', 'Bekir123', 'User');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `courses`
--
ALTER TABLE `courses`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `data`
--
ALTER TABLE `data`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `schools`
--
ALTER TABLE `schools`
  ADD PRIMARY KEY (`school_id`);

--
-- Tablo için indeksler `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `courses`
--
ALTER TABLE `courses`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Tablo için AUTO_INCREMENT değeri `data`
--
ALTER TABLE `data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Tablo için AUTO_INCREMENT değeri `schools`
--
ALTER TABLE `schools`
  MODIFY `school_id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Tablo için AUTO_INCREMENT değeri `students`
--
ALTER TABLE `students`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Tablo için AUTO_INCREMENT değeri `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
