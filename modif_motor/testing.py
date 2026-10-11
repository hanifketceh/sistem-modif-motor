
# Pengujian sederhana untuk fungsi dan class Sistem Modif Motor

import unittest

from modif_motor.validasi import validasi_nama, validasi_harga
from modif_motor.processing import KomponenModif, AnalisisModif


class TestFungsiModifMotor(unittest.TestCase):

    def test_validasi_nama(self):
        self.assertEqual(validasi_nama("Knalpot"), "Knalpot")

    def test_validasi_harga(self):
        self.assertEqual(validasi_harga("75000"), 75000)

    def test_komponen_modif(self):
        komponen = KomponenModif("Lampu LED", 100000)
        self.assertEqual(
            komponen.tampilkan(),
            "Lampu LED - Rp100000"
        )

    def test_total_biaya(self):
        data = [
            {"nama": "Knalpot", "harga": 250000},
            {"nama": "Roller CVT", "harga": 75000},
            {"nama": "Lampu LED", "harga": 100000}
        ]

        analisis = AnalisisModif(data)
        self.assertEqual(analisis.hitung_total(), 425000)


if __name__ == "__main__":
    unittest.main()