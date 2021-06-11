-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 06, 2021 at 06:14 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `jalan_kuy`
--

-- --------------------------------------------------------

--
-- Table structure for table `pembelian`
--

CREATE TABLE `pembelian` (
  `id_pembelian` int(10) NOT NULL,
  `id_pengguna` int(10) NOT NULL,
  `id_tiket` int(10) NOT NULL,
  `nama_lengkap` varchar(50) NOT NULL,
  `alamat` text NOT NULL,
  `tempat_wisata` varchar(50) NOT NULL,
  `jumlah_tiket` varchar(30) NOT NULL,
  `tanggal_kunjungan` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pembelian`
--

INSERT INTO `pembelian` (`id_pembelian`, `id_pengguna`, `id_tiket`, `nama_lengkap`, `alamat`, `tempat_wisata`, `jumlah_tiket`, `tanggal_kunjungan`) VALUES
(1, 3, 7, 'Miller Arvein Morris', 'Jl.Otto Iskandardinata, Klanceng, Ajung, Jember', 'Kebun Botani', '3', '17 Februari 2020'),
(2, 10, 6, 'Serena Anora Maheswara', 'Jl.Moh.Yamin, Kedungpiring, Tegal Besar, Kaliwates,Jember', 'Mumbul Garden', '2', '6 Mei 2020'),
(3, 7, 1, 'Regina Arunika', 'Jl.A.Yani, Panti, Jember', 'Perkebunan Teh Gunung Gambir', '2', '18 Juli 2020'),
(4, 5, 8, 'Rosseanne Cooper', 'Jl.Manggar No.62, Gebang, Kecamatan Patrang, Jember', 'Dira Park', '1', '8 Agustus 2020'),
(5, 8, 4, 'Jenny Kartadinata', 'Perum Grand Puri Bunga Nirwana, Sumbersari, Jember', 'Taman Galaxy', '4', '10 Agustus 2020'),
(6, 2, 5, 'Roger Ann Paul', 'Jl.Mastrip, Sumbersari, Jember', 'Wisata Agro Glantangan', '5', '12 September 2020'),
(12, 9, 6, 'Acacia Tredayorka', 'Jl.Bangka II', 'Mumbul Garden', '3', '6 Mei 2020');

-- --------------------------------------------------------

--
-- Table structure for table `pengguna`
--

CREATE TABLE `pengguna` (
  `id_pengguna` int(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  `username` varchar(20) NOT NULL,
  `nama_depan` varchar(50) NOT NULL,
  `nama_belakang` varchar(50) NOT NULL,
  `jenis_kelamin` varchar(20) NOT NULL,
  `password` varchar(50) NOT NULL,
  `no_telepon` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pengguna`
--

INSERT INTO `pengguna` (`id_pengguna`, `email`, `username`, `nama_depan`, `nama_belakang`, `jenis_kelamin`, `password`, `no_telepon`) VALUES
(1, 'mariasanders95@gmail.com', 'mariaa95', 'maria', 'sanders', 'perempuan', 'Marr4', '089627458145'),
(2, 'paulroger63@gmail.com', 'rogers63', 'roger', 'paul', 'laki-laki', 'Roo9', '085673452128'),
(3, 'millermorris72@gmail.com', 'morris72', 'morris', 'miller', 'laki-laki', 'Morelerr', '081336726834'),
(4, 'bellchrishaydon12@gmail.com', 'chrishaydon12', 'chrishaydon', 'bell', 'laki-laki', 'Shaydon12', '085836829742'),
(5, 'cooperrossie48@gmail.com', 'ross48', 'rossie', 'cooper', 'perempuan', 'Rosseanne', '082763659083'),
(6, 'jenardigslaya088@gmail.com', 'jenardigs8', 'jenardi', 'suralaya', 'laki-laki', 'jenong008', '082334123765'),
(7, 'arunikaregs27@gmail.com', 'reginaar27', 'regina', 'arunika', 'perempuan', 'Reggyka', '085478239001'),
(8, 'jennykard96@gmail.com', 'jenny96', 'jenny', 'kartadinata', 'perempuan', 'Jennyme', '089765009281'),
(9, 'tredayork66@gmail.com', 'acacia66', 'acacia', 'tredayorka', 'perempuan', 'Ciacynn', '081256890021'),
(10, 'anorasseren90@gmail.com', 'serenora90', 'serena', 'anora', 'perempuan', 'Mesere9', '085439902341'),
(11, 'thetigrainside01@gmail.com', 'tigrawrr10', 'Tigra', 'Danuwila', 'laki-laki', 'Tenten10', '082101010136');

-- --------------------------------------------------------

--
-- Table structure for table `tiket`
--

CREATE TABLE `tiket` (
  `id_tiket` int(10) NOT NULL,
  `nama_tiket` varchar(50) NOT NULL,
  `harga_tiket` varchar(30) NOT NULL,
  `lokasi` text NOT NULL,
  `stok` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tiket`
--

INSERT INTO `tiket` (`id_tiket`, `nama_tiket`, `harga_tiket`, `lokasi`, `stok`) VALUES
(1, 'Perkebunan Teh Gunung Gambir', '10000', 'Gelang, Sumberbaru, Kabupaten Jember', '50'),
(2, 'Kawasan Puncak Dan Pemandian Rembangan', '8000', 'Kemuning Lor, Arjasa, Kabupaten Jember', '50'),
(3, 'Taman Nasional Meru Betiri', '10000', 'Andongrejo, Tempurejo, Kabupaten Jember', '50'),
(4, 'Taman Galaxy', '10000', 'Kecamatan Tempurejo, Kabupaten Jember', '50'),
(5, 'Wisata Agro Glantangan', '125000', 'Pondokrejo, Tempurejo, Kabupaten Jember', '50'),
(6, 'Mumbul Garden', '12500', 'Lengkong, Mumbulsari, Kabupaten Jember', '50'),
(7, 'Kebun Botani', '20000', 'Krajan, Sukorambi, Kabupaten Jember', '50'),
(8, 'Dira Park', '15000', 'Andongsari, Ambulu, Kabupaten Jember', '50'),
(9, 'Tiara Jember Park Waterboom', '25000', 'Krajan Barat, Sumbersari, Kabupaten Jember', '50'),
(10, 'Pemandian Kebon Agung', '7500', 'Kebon Agung, Kaliwates, Kabupaten Jember', '50');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `pembelian`
--
ALTER TABLE `pembelian`
  ADD PRIMARY KEY (`id_pembelian`),
  ADD KEY `id_pengguna` (`id_pengguna`),
  ADD KEY `id_tiket` (`id_tiket`);

--
-- Indexes for table `pengguna`
--
ALTER TABLE `pengguna`
  ADD PRIMARY KEY (`id_pengguna`);

--
-- Indexes for table `tiket`
--
ALTER TABLE `tiket`
  ADD PRIMARY KEY (`id_tiket`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pembelian`
--
ALTER TABLE `pembelian`
  MODIFY `id_pembelian` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `pengguna`
--
ALTER TABLE `pengguna`
  MODIFY `id_pengguna` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `pembelian`
--
ALTER TABLE `pembelian`
  ADD CONSTRAINT `pembelian_ibfk_1` FOREIGN KEY (`id_pengguna`) REFERENCES `pengguna` (`id_pengguna`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `pembelian_ibfk_2` FOREIGN KEY (`id_tiket`) REFERENCES `tiket` (`id_tiket`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
