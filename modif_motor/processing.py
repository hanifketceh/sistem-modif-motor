
# Class untuk mewakili satu komponen modifikasi motor
class KomponenModif:

    # Menyimpan nama dan harga komponen
    def __init__(self, nama, harga):
        assert nama.strip() != "", "Nama tidak boleh kosong"
        assert harga >= 0, "Harga tidak boleh negatif"

        self.nama = nama
        self.harga = harga

    # Menampilkan informasi komponen
    def tampilkan(self):
        return f"{self.nama} - Rp{self.harga}"


# Class untuk mengolah daftar komponen modifikasi
class AnalisisModif:

    # Menerima daftar komponen untuk dianalisis
    def __init__(self, data):
        self.data = data

    # Menghitung total harga
    def hitung_total(self):
        total = 0

        for komponen in self.data:
            total += komponen["harga"]

        return total

    # Menghitung rata-rata harga
    def hitung_rata_rata(self):
        if len(self.data) == 0:
            return 0

        return self.hitung_total() / len(self.data)

    # Mencari komponen dengan harga tertinggi
    def cari_termahal(self):
        if len(self.data) == 0:
            return None

        return max(
            self.data,
            key=lambda item: item["harga"]
        )

    # Mengurutkan komponen dari harga terendah
    def urutkan_harga(self):
        return sorted(
            self.data,
            key=lambda item: item["harga"]
        )

    # Memilih komponen yang sesuai anggaran
    def filter_anggaran(self, batas_harga):
        return list(
            filter(
                lambda item: item["harga"] <= batas_harga,
                self.data
            )
        )


# Fungsi untuk menjumlahkan beberapa harga sekaligus
def hitung_total(*harga):
    total = 0

    for nilai in harga:
        total += nilai

    return total


# Pengujian lokal modul processing
if __name__ == "__main__":
    daftar = [
        {"nama": "Knalpot", "harga": 250000},
        {"nama": "Roller CVT", "harga": 75000},
        {"nama": "Lampu LED", "harga": 100000}
    ]

    analisis = AnalisisModif(daftar)

    print("Total:", analisis.hitung_total())
    print("Rata-rata:", analisis.hitung_rata_rata())
    print("Termahal:", analisis.cari_termahal())
    print("Urutan harga:", analisis.urutkan_harga())

    print(
        "Sesuai anggaran:",
        analisis.filter_anggaran(batas_harga=100000)
    )

    print(
        "Total dari *args:",
        hitung_total(250000, 75000, 100000)
    )