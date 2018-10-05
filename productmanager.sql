-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 05 Paź 2018, 10:49
-- Wersja serwera: 10.1.30-MariaDB
-- Wersja PHP: 7.2.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `productmanager`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `category`
--

CREATE TABLE `category` (
  `id` int(10) NOT NULL,
  `name` varchar(100) COLLATE utf8_polish_ci NOT NULL,
  `parent` int(10) NOT NULL DEFAULT '1',
  `tags` text COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `category`
--

INSERT INTO `category` (`id`, `name`, `parent`, `tags`) VALUES
(1, 'Stoły', 1, 'stoły, stoliki, kawowe, jadalnia'),
(2, 'Biurka', 2, 'biurka, pokojowe, biurowe, dziecięce'),
(3, 'Stoliki kawowe', 1, 'stoliki, kawowe'),
(4, 'Biurka biurowe', 2, 'biurka, biurowe'),
(5, 'Biurka dziecięce', 2, 'biurka, dziecięce'),
(6, 'Białe', 3, 'białe'),
(7, 'Szare', 3, 'szare'),
(8, 'Szafy', 8, 'szafy'),
(9, 'Norweskie', 4, 'norwerskie, biurko');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `news`
--

CREATE TABLE `news` (
  `id` int(10) NOT NULL,
  `header` varchar(100) COLLATE utf8_polish_ci NOT NULL,
  `content` text COLLATE utf8_polish_ci NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `news`
--

INSERT INTO `news` (`id`, `header`, `content`, `date`) VALUES
(1, 'Najnowszy news!', '<p>To jest nowy news</p>\r\n<p>Jest nowszy niż wszystko inne\r\ni służy do <b>testów</b>.... Na przykład czy przenosi do nowej linii :) Także piszemy cokolwiek aby przekroczyć zakres</p>\r\n<p><img src=\':/logo/logo\' width=\'300\'/></p>', '2018-09-26 07:29:46');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `products`
--

CREATE TABLE `products` (
  `id` int(10) NOT NULL,
  `name` varchar(200) COLLATE utf8_polish_ci NOT NULL,
  `description` varchar(410) COLLATE utf8_polish_ci NOT NULL,
  `description_long` text COLLATE utf8_polish_ci NOT NULL,
  `priceNetto` float NOT NULL,
  `priceBrutto` float NOT NULL,
  `category` varchar(40) COLLATE utf8_polish_ci NOT NULL,
  `pic` varchar(100) COLLATE utf8_polish_ci NOT NULL,
  `new` tinyint(1) NOT NULL DEFAULT '0',
  `prom` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `products`
--

INSERT INTO `products` (`id`, `name`, `description`, `description_long`, `priceNetto`, `priceBrutto`, `category`, `pic`, `new`, `prom`) VALUES
(1, 'Stolik kawowy - metalowe nogi', 'Stolik w kolorze srakim', '', 208.12, 255.99, ';1;3;', ':/stol/stolmetal', 1, 0),
(2, 'abc', '012345678A0 012345678A0 012345678A0 012345678A0 012345678A0 012345678A0 012345678A0 012345678A0 012345678A0 012345678A0 012345678A0 012345678A0 012345678A0 012345678A0 012345678A0 012345678A0 012345678A0 012345678A0 012345678A0 012345678A0 012345678A0 012345678A0 012345678A0 012345678A0 012345678A0 012345678A0 012345678A0 012345678A0 012345678A0 012345678A0 012345678A0 012345678A0 012345678A0 012345678A0 01', '', 208.12, 255.99, ';1;3;', ':/stol/stolmetal', 0, 0),
(3, 'cde', 'Stolik w kolorze srakim', '', 208.12, 255.99, ';1;3;', ':/stol/stolmetal', 0, 1),
(4, 'lipa', 'Stolik w kolorze srakim', '', 208.12, 255.99, ';1;3;', ':/stol/stolmetal', 0, 0),
(5, 'A', 'Stolik w kolorze srakim', '', 208.12, 255.99, ';1;', ':/stol/stolmetal', 0, 0),
(6, 'B', 'Stolik w kolorze srakim', '', 208.12, 255.99, ';1;', ':/stol/stolmetal', 0, 0),
(7, 'C', 'Stolik w kolorze srakim', '', 208.12, 255.99, ';1;', ':/stol/stolmetal', 0, 0),
(8, 'D', 'Stolik w kolorze srakim', '', 208.12, 255.99, ';1;', ':/stol/stolmetal', 0, 0),
(9, 'E', 'Stolik w kolorze srakim', '', 208.12, 255.99, ';1;', ':/stol/stolmetal', 0, 0),
(10, 'F', 'Stolik w kolorze srakim', '', 208.12, 255.99, ';1;', ':/stol/stolmetal', 0, 0),
(11, 'G', 'Stolik w kolorze srakim', '', 208.12, 255.99, ';1;', ':/stol/stolmetal', 0, 0);

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`id`),
  ADD KEY `parent` (`parent`);

--
-- Indeksy dla tabeli `news`
--
ALTER TABLE `news`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT dla tabeli `category`
--
ALTER TABLE `category`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT dla tabeli `news`
--
ALTER TABLE `news`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT dla tabeli `products`
--
ALTER TABLE `products`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `category`
--
ALTER TABLE `category`
  ADD CONSTRAINT `category_ibfk_1` FOREIGN KEY (`parent`) REFERENCES `category` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
