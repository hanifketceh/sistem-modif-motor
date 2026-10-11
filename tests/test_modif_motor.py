
import unittest

from modif_motor.validasi import (
    validasi_nama,
    validasi_harga,
    validasi_data
)

from modif_motor.processing import (
    KomponenModif,
    AnalisisModif
)


class TestModifMotor(unittest.TestCase):

    def setUp(self):
        # Data contoh untuk menguji analisis biaya
        self.data = [
            {"nama": "Knalpot", "harga": 250000},
            {"nama": "Roller CVT", "harga": 75000},
            {"nama": "Lampu LED", "harga": 100000}
        ]

        self.analisis = AnalisisModif(self.data)

    # Pengujian validasi
    def test_nama_valid(self):
        self.assertEqual(validasi_nama("Knalpot"), "Knalpot")

    def test_nama_kosong(self):
        with self.assertRaises(ValueError):
            validasi_nama("   ")

    def test_harga_valid(self):
        self.assertEqual(validasi_harga("250000"), 250000)

    def test_harga_negatif(self):
        with self.assertRaises(ValueError):
            validasi_harga(-5000)

    def test_harga_bukan_angka(self):
        with self.assertRaises(ValueError):
            validasi_harga("mahal")

    def test_validasi_data(self):
        nama, harga = validasi_data("Lampu LED", "100000")
        self.assertEqual(nama, "Lampu LED")
        self.assertEqual(harga, 100000)

    # Pengujian class KomponenModif
    def test_komponen_tampilkan(self):
        komponen = KomponenModif("Knalpot", 250000)
        self.assertEqual(
            komponen.tampilkan(),
            "Knalpot - Rp250000"
        )

    # Pengujian analisis biaya
    def test_hitung_total(self):
        self.assertEqual(self.analisis.hitung_total(), 425000)

    def test_hitung_rata_rata(self):
        self.assertAlmostEqual(
            self.analisis.hitung_rata_rata(),
            425000 / 3
        )

    def test_cari_termahal(self):
        hasil = self.analisis.cari_termahal()
        self.assertEqual(hasil["nama"], "Knalpot")
        self.assertEqual(hasil["harga"], 250000)

    def test_urutkan_harga(self):
        hasil = self.analisis.urutkan_harga()
        harga = [item["harga"] for item in hasil]

        self.assertEqual(harga, [75000, 100000, 250000])

    def test_filter_anggaran(self):
        hasil = self.analisis.filter_anggaran(batas_harga=100000)
        nama = [item["nama"] for item in hasil]

        self.assertEqual(nama, ["Roller CVT", "Lampu LED"])


if __name__ == "__main__":
    unittest.main()