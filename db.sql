-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Mar 16, 2019 at 10:23 AM
-- Server version: 5.6.38
-- PHP Version: 7.2.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `prediksi_harga_banten`
--

-- --------------------------------------------------------

--
-- Table structure for table `jenis_banten`
--

CREATE TABLE `jenis_banten` (
  `id` int(11) NOT NULL,
  `nama` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `lokasi`
--

CREATE TABLE `lokasi` (
  `id` int(11) NOT NULL,
  `nama` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `rahinan`
--

CREATE TABLE `rahinan` (
  `id` int(11) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `bobot` decimal(3,3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `rahinan`
--

INSERT INTO `rahinan` (`id`, `nama`, `bobot`) VALUES
(1, 'Tidak ada rahinan', '0.400');

-- --------------------------------------------------------

--
-- Table structure for table `tanggal_rahinan`
--

CREATE TABLE `tanggal_rahinan` (
  `id_rahinan` int(11) NOT NULL,
  `tanggal` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `transaksi`
--

CREATE TABLE `transaksi` (
  `id` int(11) NOT NULL,
  `tanggal` date NOT NULL,
  `total_harga` decimal(3,3) NOT NULL,
  `id_lokasi` int(11) NOT NULL,
  `id_jenis_banten` int(11) NOT NULL,
  `id_rahinan` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `jenis_banten`
--
ALTER TABLE `jenis_banten`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `lokasi`
--
ALTER TABLE `lokasi`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rahinan`
--
ALTER TABLE `rahinan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tanggal_rahinan`
--
ALTER TABLE `tanggal_rahinan`
  ADD KEY `id_rahinan` (`id_rahinan`);

--
-- Indexes for table `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_jenis_banten` (`id_jenis_banten`),
  ADD KEY `id_lokasi` (`id_lokasi`),
  ADD KEY `id_rahinan` (`id_rahinan`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `jenis_banten`
--
ALTER TABLE `jenis_banten`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `lokasi`
--
ALTER TABLE `lokasi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `rahinan`
--
ALTER TABLE `rahinan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `transaksi`
--
ALTER TABLE `transaksi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tanggal_rahinan`
--
ALTER TABLE `tanggal_rahinan`
  ADD CONSTRAINT `tanggal_rahinan_ibfk_1` FOREIGN KEY (`id_rahinan`) REFERENCES `rahinan` (`id`);

--
-- Constraints for table `transaksi`
--
ALTER TABLE `transaksi`
  ADD CONSTRAINT `transaksi_ibfk_1` FOREIGN KEY (`id_jenis_banten`) REFERENCES `jenis_banten` (`id`),
  ADD CONSTRAINT `transaksi_ibfk_2` FOREIGN KEY (`id_lokasi`) REFERENCES `lokasi` (`id`),
  ADD CONSTRAINT `transaksi_ibfk_3` FOREIGN KEY (`id_rahinan`) REFERENCES `rahinan` (`id`);

