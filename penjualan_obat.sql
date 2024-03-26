-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 28, 2024 at 01:35 AM
-- Server version: 8.0.30
-- PHP Version: 8.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `penjualan_obat`
--

-- --------------------------------------------------------

--
-- Table structure for table `diskon`
--

CREATE TABLE `diskon` (
  `id_diskon` int NOT NULL,
  `nama_diskon` varchar(100) DEFAULT NULL,
  `persentase_diskon` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `diskon`
--

INSERT INTO `diskon` (`id_diskon`, `nama_diskon`, `persentase_diskon`) VALUES
(1, 'Akhir Tahun', 5),
(2, 'Ramadhan', 10),
(3, 'Flash Sale', 15),
(4, 'Cuci Gudang', 20);

-- --------------------------------------------------------

--
-- Table structure for table `jenis_obat`
--

CREATE TABLE `jenis_obat` (
  `id_jenis_obat` int NOT NULL,
  `nama_jenis_obat` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `jenis_obat`
--

INSERT INTO `jenis_obat` (`id_jenis_obat`, `nama_jenis_obat`) VALUES
(1, 'Obat Bebas'),
(2, 'Obat Bebas Terbatas'),
(3, 'Obat Keras'),
(4, 'Obat Golongan Narkotika'),
(5, 'Obat Fitofarmaka'),
(6, 'Obat Herbal Terstandar'),
(7, 'Jamu');

-- --------------------------------------------------------

--
-- Table structure for table `obat`
--

CREATE TABLE `obat` (
  `id_obat` int NOT NULL,
  `nama_obat` varchar(100) DEFAULT NULL,
  `harga` decimal(20,2) DEFAULT NULL,
  `stok` int DEFAULT NULL,
  `id_jenis_obat` int DEFAULT NULL,
  `id_diskon` int DEFAULT NULL,
  `id_satuan` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `obat`
--

INSERT INTO `obat` (`id_obat`, `nama_obat`, `harga`, `stok`, `id_jenis_obat`, `id_diskon`, `id_satuan`) VALUES
(1, 'Xanax', '172544.00', 78, 4, 1, 3),
(2, 'Viagra', '152738.00', 61, 3, 3, 1),
(3, 'Zoloft', '422046.00', 20, 3, 1, 1),
(4, 'Ativan', '241515.00', 64, 1, 1, 3),
(5, 'Adderall', '206639.00', 94, 2, 2, 3),
(6, 'Ambien', '150204.00', 99, 3, 1, 1),
(7, 'Ritalin', '44144.00', 18, 1, 2, 1),
(8, 'Paxil', '34952.00', 64, 5, 2, 3),
(9, 'Lipitor', '138084.00', 50, 5, 3, 2),
(10, 'Tylenol', '237391.00', 7, 3, 1, 1),
(11, 'Valium', '103976.00', 26, 3, 2, 3),
(12, 'Nexium', '212954.00', 33, 7, 4, 3),
(13, 'Celebrex', '288656.00', 50, 4, 4, 3),
(14, 'Cialis', '123682.00', 44, 2, 1, 1),
(15, 'Advil', '466129.00', 88, 5, 2, 3),
(16, 'Prozac', '14621.00', 29, 2, 2, 3),
(17, 'Claritin', '410021.00', 58, 1, 3, 1),
(18, 'Vicodin', '177981.00', 69, 3, 1, 3),
(19, 'Benadryl', '162332.00', 70, 2, 1, 1),
(20, 'Allegra', '5514.00', 67, 2, 2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `pelanggan`
--

CREATE TABLE `pelanggan` (
  `id_pelanggan` int NOT NULL,
  `nama_pelanggan` varchar(100) DEFAULT NULL,
  `no_telepon` varchar(36) DEFAULT NULL,
  `alamat` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `pelanggan`
--

INSERT INTO `pelanggan` (`id_pelanggan`, `nama_pelanggan`, `no_telepon`, `alamat`) VALUES
(1, 'Alanna McVicker', '+7 552 169 9339', '64284 Oakridge Way'),
(2, 'Charlotta Windridge', '+1 203 907 2368', '89813 Clyde Gallagher Hill'),
(3, 'Orsa Crenshaw', '+86 534 963 4560', '27801 Ilene Alley'),
(4, 'Vernon Vedishchev', '+66 290 696 8640', '3 Hoffman Street'),
(5, 'Ernest Havik', '+63 871 329 0344', '70 Schlimgen Court'),
(6, 'Rogers Gaucher', '+7 991 295 3134', '56 Brown Crossing'),
(7, 'Osborn Tutill', '+33 128 731 5773', '4 Fulton Point'),
(8, 'Adriana Vallentin', '+46 139 454 8729', '316 Utah Pass'),
(9, 'Sammie Blemen', '+1 772 989 3166', '22 Service Street'),
(10, 'Jsandye Chester', '+62 998 227 7320', '4 Fairview Point');

-- --------------------------------------------------------

--
-- Table structure for table `satuan`
--

CREATE TABLE `satuan` (
  `id_satuan` int NOT NULL,
  `nama_satuan` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `satuan`
--

INSERT INTO `satuan` (`id_satuan`, `nama_satuan`) VALUES
(1, 'kaplet'),
(2, 'pak'),
(3, 'dus');

-- --------------------------------------------------------

--
-- Table structure for table `transaksi`
--

CREATE TABLE `transaksi` (
  `id_transaksi` int NOT NULL,
  `id_pelanggan` int DEFAULT NULL,
  `tanggal` date DEFAULT NULL,
  `total_harga` decimal(20,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `transaksi`
--

INSERT INTO `transaksi` (`id_transaksi`, `id_pelanggan`, `tanggal`, `total_harga`) VALUES
(1, 7, '2023-12-08', '277775.00'),
(2, 9, '2024-01-03', '94465.00'),
(3, 9, '2023-07-02', '435566.00'),
(4, 4, '2023-06-09', '39312.00'),
(5, 1, '2023-07-25', '366577.00'),
(6, 9, '2023-12-28', '10928.00'),
(7, 8, '2023-06-27', '100997.00'),
(8, 5, '2023-11-20', '499475.00'),
(9, 8, '2023-11-11', '381804.00'),
(10, 8, '2023-08-20', '333374.00'),
(11, 8, '2023-07-20', '415575.00'),
(12, 9, '2023-03-31', '25955.00'),
(13, 10, '2023-08-13', '397060.00'),
(14, 3, '2023-09-21', '193453.00'),
(15, 8, '2023-05-07', '117451.00'),
(16, 9, '2023-10-22', '407323.00'),
(17, 4, '2023-07-20', '303396.00'),
(18, 2, '2023-04-25', '342827.00'),
(19, 9, '2023-12-10', '178911.00'),
(20, 5, '2023-07-23', '164719.00'),
(21, 9, '2023-09-28', '320249.00'),
(22, 8, '2023-02-23', '391605.00'),
(23, 5, '2023-12-29', '42683.00'),
(24, 6, '2023-05-15', '303474.00'),
(25, 1, '2023-06-14', '481549.00'),
(26, 8, '2023-08-28', '251740.00'),
(27, 9, '2023-08-31', '35620.00'),
(28, 10, '2023-06-25', '269979.00'),
(29, 9, '2023-08-16', '203337.00'),
(30, 5, '2023-11-09', '352763.00'),
(31, 9, '2023-02-24', '318399.00'),
(32, 5, '2024-01-17', '211194.00'),
(33, 4, '2023-07-29', '210060.00'),
(34, 3, '2023-03-19', '48844.00'),
(35, 4, '2024-01-31', '39068.00'),
(36, 6, '2023-11-06', '81174.00'),
(37, 6, '2023-11-11', '249971.00'),
(38, 7, '2023-06-08', '301703.00'),
(39, 7, '2023-04-01', '13202.00'),
(40, 8, '2023-03-26', '452507.00'),
(41, 6, '2023-10-13', '442205.00'),
(42, 5, '2023-12-17', '306538.00'),
(43, 9, '2023-09-04', '480440.00'),
(44, 3, '2023-10-24', '289507.00'),
(45, 3, '2023-03-05', '425633.00'),
(46, 7, '2023-09-16', '168148.00'),
(47, 10, '2023-05-11', '242887.00'),
(48, 7, '2023-09-26', '192680.00'),
(49, 8, '2023-03-15', '330181.00'),
(50, 9, '2023-10-12', '403932.00'),
(51, 2, '2023-03-28', '173708.00'),
(52, 1, '2023-10-31', '339459.00'),
(53, 7, '2023-12-23', '198971.00'),
(54, 5, '2023-10-30', '353056.00'),
(55, 1, '2023-09-21', '35520.00'),
(56, 9, '2023-11-20', '358811.00'),
(57, 3, '2023-12-21', '234645.00'),
(58, 8, '2023-12-15', '205437.00'),
(59, 7, '2024-02-08', '391855.00'),
(60, 2, '2024-01-31', '381337.00'),
(61, 4, '2023-04-23', '304927.00'),
(62, 10, '2023-06-21', '101484.00'),
(63, 2, '2024-01-04', '484728.00'),
(64, 5, '2023-07-03', '271567.00'),
(65, 1, '2023-12-23', '194088.00'),
(66, 7, '2023-11-19', '418152.00'),
(67, 7, '2023-05-13', '227170.00'),
(68, 2, '2023-05-20', '445809.00'),
(69, 10, '2024-02-13', '385134.00'),
(70, 5, '2023-12-17', '180498.00'),
(71, 9, '2023-03-15', '36338.00'),
(72, 3, '2024-01-03', '40636.00'),
(73, 9, '2023-07-04', '463848.00'),
(74, 5, '2023-03-15', '426271.00'),
(75, 10, '2023-08-25', '475726.00'),
(76, 10, '2023-12-18', '470573.00'),
(77, 3, '2023-02-28', '201755.00'),
(78, 10, '2023-03-06', '262092.00'),
(79, 5, '2023-06-29', '37847.00'),
(80, 10, '2023-11-20', '436445.00'),
(81, 5, '2023-02-20', '112775.00'),
(82, 4, '2023-12-11', '482640.00'),
(83, 7, '2023-04-08', '446743.00'),
(84, 4, '2023-06-15', '159855.00'),
(85, 2, '2023-09-24', '286054.00'),
(86, 7, '2024-01-11', '407589.00'),
(87, 6, '2023-04-06', '410673.00'),
(88, 5, '2023-06-17', '478836.00'),
(89, 10, '2024-01-24', '163737.00'),
(90, 2, '2023-03-17', '198727.00'),
(91, 2, '2023-06-29', '94021.00'),
(92, 8, '2023-11-21', '420310.00'),
(93, 8, '2023-05-05', '217174.00'),
(94, 1, '2023-04-14', '90285.00'),
(95, 6, '2023-11-27', '401469.00'),
(96, 7, '2023-05-27', '406343.00'),
(97, 3, '2023-10-24', '105060.00'),
(98, 7, '2023-05-30', '264560.00'),
(99, 6, '2023-06-06', '384777.00'),
(100, 6, '2023-04-30', '268696.00');

-- --------------------------------------------------------

--
-- Table structure for table `transaksi_detail`
--

CREATE TABLE `transaksi_detail` (
  `id_transaksi` int DEFAULT NULL,
  `id_obat` int DEFAULT NULL,
  `jumlah_obat` int DEFAULT NULL,
  `harga_obat` decimal(20,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `transaksi_detail`
--

INSERT INTO `transaksi_detail` (`id_transaksi`, `id_obat`, `jumlah_obat`, `harga_obat`) VALUES
(1, 2, 5, '278875.00'),
(1, 8, 1, '71403.00'),
(2, 5, 5, '87280.00'),
(2, 14, 6, '311481.00'),
(3, 17, 5, '183344.00'),
(3, 11, 4, '269535.00'),
(4, 1, 2, '483401.00'),
(4, 7, 2, '325672.00'),
(5, 16, 5, '176813.00'),
(5, 13, 2, '457794.00'),
(6, 9, 2, '127873.00'),
(6, 3, 3, '291980.00'),
(7, 7, 1, '146659.00'),
(7, 19, 4, '250082.00'),
(8, 20, 5, '485196.00'),
(8, 17, 5, '313596.00'),
(9, 9, 2, '56711.00'),
(9, 17, 4, '19265.00'),
(10, 10, 2, '410471.00'),
(10, 18, 2, '215633.00'),
(11, 5, 3, '164830.00'),
(11, 13, 6, '255745.00'),
(12, 10, 5, '321118.00'),
(12, 11, 5, '13999.00'),
(13, 20, 2, '427745.00'),
(13, 6, 2, '71247.00'),
(14, 4, 4, '223305.00'),
(14, 13, 3, '500922.00'),
(15, 5, 6, '457480.00'),
(15, 9, 3, '318565.00'),
(16, 19, 6, '170835.00'),
(16, 16, 1, '317726.00'),
(17, 3, 1, '252450.00'),
(17, 1, 2, '374041.00'),
(18, 10, 4, '308220.00'),
(18, 8, 1, '297997.00'),
(19, 3, 1, '486777.00'),
(19, 14, 6, '221849.00'),
(20, 3, 2, '116654.00'),
(20, 14, 2, '441491.00'),
(21, 16, 3, '371569.00'),
(21, 17, 5, '223508.00'),
(22, 20, 1, '448553.00'),
(22, 12, 5, '152773.00'),
(23, 15, 2, '344395.00'),
(23, 19, 4, '246636.00'),
(24, 18, 2, '44803.00'),
(24, 4, 3, '305161.00'),
(25, 8, 3, '582625.00'),
(25, 4, 6, '547235.00'),
(26, 8, 6, '522780.00'),
(26, 13, 1, '522119.00'),
(27, 1, 1, '379068.00'),
(27, 18, 5, '185656.00'),
(28, 10, 6, '144873.00'),
(28, 3, 1, '486191.00'),
(29, 7, 2, '352267.00'),
(29, 18, 5, '232732.00'),
(30, 12, 1, '580596.00'),
(30, 7, 4, '63507.00'),
(31, 1, 6, '502223.00'),
(31, 10, 5, '555998.00'),
(32, 4, 6, '399625.00'),
(32, 4, 6, '275937.00'),
(33, 11, 3, '153633.00'),
(33, 3, 1, '566885.00'),
(34, 16, 2, '279387.00'),
(34, 3, 2, '446577.00'),
(35, 12, 2, '534002.00'),
(35, 5, 4, '182619.00'),
(36, 10, 1, '389280.00'),
(36, 7, 6, '179428.00'),
(37, 12, 4, '199911.00'),
(37, 19, 3, '96737.00'),
(38, 7, 6, '374061.00'),
(38, 17, 1, '548027.00'),
(39, 2, 4, '236647.00'),
(39, 6, 3, '449808.00'),
(40, 16, 5, '274238.00'),
(40, 18, 1, '250447.00'),
(41, 14, 4, '295298.00'),
(41, 4, 5, '222356.00'),
(42, 11, 4, '134390.00'),
(42, 11, 3, '461433.00'),
(43, 11, 2, '389433.00'),
(43, 9, 1, '333357.00'),
(44, 12, 3, '121383.00'),
(44, 13, 1, '169838.00'),
(45, 4, 5, '50092.00'),
(45, 9, 4, '544160.00'),
(46, 6, 6, '320875.00'),
(46, 7, 4, '488366.00'),
(47, 20, 1, '261203.00'),
(47, 4, 1, '139630.00'),
(48, 7, 6, '502387.00'),
(48, 10, 1, '370051.00'),
(49, 5, 4, '426312.00'),
(49, 13, 6, '530136.00'),
(50, 12, 6, '272467.00'),
(50, 19, 5, '68318.00'),
(51, 19, 1, '539805.00'),
(51, 9, 4, '162217.00'),
(52, 15, 5, '325507.00'),
(52, 2, 6, '597013.00'),
(53, 4, 1, '205065.00'),
(53, 4, 5, '91055.00'),
(54, 15, 1, '315633.00'),
(54, 13, 3, '120409.00'),
(55, 17, 1, '283656.00'),
(55, 3, 4, '219075.00'),
(56, 12, 1, '442564.00'),
(56, 14, 4, '178809.00'),
(57, 17, 4, '438515.00'),
(57, 1, 6, '451909.00'),
(58, 2, 6, '585495.00'),
(58, 20, 2, '362098.00'),
(59, 20, 6, '399767.00'),
(59, 6, 1, '256849.00'),
(60, 17, 1, '435172.00'),
(60, 11, 3, '314329.00'),
(61, 14, 6, '275179.00'),
(61, 12, 5, '321771.00'),
(62, 12, 5, '335151.00'),
(62, 7, 3, '595943.00'),
(63, 6, 3, '47216.00'),
(63, 17, 1, '329331.00'),
(64, 11, 5, '440668.00'),
(64, 6, 6, '545763.00'),
(65, 9, 4, '321793.00'),
(65, 2, 6, '210931.00'),
(66, 16, 6, '152038.00'),
(66, 20, 3, '384487.00'),
(67, 19, 1, '41111.00'),
(67, 9, 2, '397732.00'),
(68, 18, 5, '125007.00'),
(68, 1, 2, '320198.00'),
(69, 16, 5, '37859.00'),
(69, 11, 1, '227571.00'),
(70, 10, 6, '17633.00'),
(70, 1, 6, '84303.00'),
(71, 16, 1, '519700.00'),
(71, 20, 1, '132172.00'),
(72, 19, 4, '239891.00'),
(72, 5, 6, '192910.00'),
(73, 15, 4, '392797.00'),
(73, 10, 5, '493516.00'),
(74, 15, 5, '592751.00'),
(74, 1, 4, '300521.00'),
(75, 16, 2, '87527.00'),
(75, 8, 5, '161696.00'),
(76, 19, 2, '287795.00'),
(76, 13, 1, '401502.00'),
(77, 17, 4, '524846.00'),
(77, 19, 4, '254975.00'),
(78, 16, 6, '363140.00'),
(78, 12, 5, '179536.00'),
(79, 9, 4, '586777.00'),
(79, 20, 2, '362222.00'),
(80, 15, 2, '459342.00'),
(80, 8, 1, '12446.00'),
(81, 18, 1, '481555.00'),
(81, 18, 3, '171210.00'),
(82, 11, 4, '198339.00'),
(82, 20, 5, '227445.00'),
(83, 5, 5, '463061.00'),
(83, 17, 6, '51221.00'),
(84, 5, 1, '310484.00'),
(84, 8, 6, '322552.00'),
(85, 17, 5, '409520.00'),
(85, 12, 1, '372428.00'),
(86, 15, 6, '489046.00'),
(86, 7, 2, '597510.00'),
(87, 4, 2, '468594.00'),
(87, 3, 3, '62862.00'),
(88, 9, 2, '330581.00'),
(88, 14, 1, '133422.00'),
(89, 18, 4, '375838.00'),
(89, 12, 3, '57931.00'),
(90, 6, 5, '536056.00'),
(90, 10, 4, '462376.00'),
(91, 17, 5, '74376.00'),
(91, 8, 4, '547520.00'),
(92, 9, 5, '403110.00'),
(92, 8, 4, '131302.00'),
(93, 9, 5, '465469.00'),
(93, 11, 4, '509669.00'),
(94, 4, 4, '231657.00'),
(94, 6, 1, '573599.00'),
(95, 15, 5, '468540.00'),
(95, 2, 4, '398122.00'),
(96, 14, 4, '176572.00'),
(96, 18, 6, '193126.00'),
(97, 4, 6, '282499.00'),
(97, 5, 1, '222702.00'),
(98, 11, 6, '327353.00'),
(98, 8, 6, '596437.00'),
(99, 6, 5, '565248.00'),
(99, 20, 3, '452657.00'),
(100, 7, 5, '390660.00'),
(100, 1, 4, '526382.00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `diskon`
--
ALTER TABLE `diskon`
  ADD PRIMARY KEY (`id_diskon`);

--
-- Indexes for table `jenis_obat`
--
ALTER TABLE `jenis_obat`
  ADD PRIMARY KEY (`id_jenis_obat`);

--
-- Indexes for table `obat`
--
ALTER TABLE `obat`
  ADD PRIMARY KEY (`id_obat`),
  ADD KEY `id_jenis_obat` (`id_jenis_obat`),
  ADD KEY `id_diskon` (`id_diskon`),
  ADD KEY `id_satuan` (`id_satuan`);

--
-- Indexes for table `pelanggan`
--
ALTER TABLE `pelanggan`
  ADD PRIMARY KEY (`id_pelanggan`);

--
-- Indexes for table `satuan`
--
ALTER TABLE `satuan`
  ADD PRIMARY KEY (`id_satuan`);

--
-- Indexes for table `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`id_transaksi`),
  ADD KEY `id_pelanggan` (`id_pelanggan`);

--
-- Indexes for table `transaksi_detail`
--
ALTER TABLE `transaksi_detail`
  ADD KEY `id_transaksi` (`id_transaksi`),
  ADD KEY `id_obat` (`id_obat`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `diskon`
--
ALTER TABLE `diskon`
  MODIFY `id_diskon` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `jenis_obat`
--
ALTER TABLE `jenis_obat`
  MODIFY `id_jenis_obat` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `obat`
--
ALTER TABLE `obat`
  MODIFY `id_obat` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `pelanggan`
--
ALTER TABLE `pelanggan`
  MODIFY `id_pelanggan` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `satuan`
--
ALTER TABLE `satuan`
  MODIFY `id_satuan` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `transaksi`
--
ALTER TABLE `transaksi`
  MODIFY `id_transaksi` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=102;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `obat`
--
ALTER TABLE `obat`
  ADD CONSTRAINT `obat_ibfk_1` FOREIGN KEY (`id_jenis_obat`) REFERENCES `jenis_obat` (`id_jenis_obat`),
  ADD CONSTRAINT `obat_ibfk_2` FOREIGN KEY (`id_diskon`) REFERENCES `diskon` (`id_diskon`),
  ADD CONSTRAINT `obat_ibfk_3` FOREIGN KEY (`id_satuan`) REFERENCES `satuan` (`id_satuan`);

--
-- Constraints for table `transaksi`
--
ALTER TABLE `transaksi`
  ADD CONSTRAINT `transaksi_ibfk_1` FOREIGN KEY (`id_pelanggan`) REFERENCES `pelanggan` (`id_pelanggan`);

--
-- Constraints for table `transaksi_detail`
--
ALTER TABLE `transaksi_detail`
  ADD CONSTRAINT `transaksi_detail_ibfk_1` FOREIGN KEY (`id_transaksi`) REFERENCES `transaksi` (`id_transaksi`),
  ADD CONSTRAINT `transaksi_detail_ibfk_2` FOREIGN KEY (`id_obat`) REFERENCES `obat` (`id_obat`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
