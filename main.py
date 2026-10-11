
# Mengimpor fungsi dari package buatan sendiri
from modif_motor.validasi import validasi_data
from modif_motor.fileio import (
    buat_file,
    simpan_data,
    baca_data,
    buat_laporan
)
from modif_motor.processing import AnalisisModif


# Menampilkan menu utama
def tampilkan_menu():
    print("\n=== SISTEM MODIF MOTOR ===")
    print("1. Tambah komponen")
    print("2. Lihat daftar komponen")
    print("3. Analisis biaya modifikasi")
    print("4. Buat laporan")
    print("5. Keluar")


# Menambahkan komponen baru
def tambah_komponen():
    try:
        nama = input("Nama komponen: ")
        harga = input("Harga komponen: ")

        nama, harga = validasi_data(nama, harga)
        simpan_data(nama, harga)

        print("Komponen berhasil ditambahkan.")

    except ValueError as error:
        print("Data tidak valid:", error)

    except OSError:
        print("Data gagal disimpan.")


# Menampilkan daftar komponen
def tampilkan_data():
    daftar = baca_data()

    if len(daftar) == 0:
        print("Belum ada data komponen.")
        return

    print("\n=== DAFTAR KOMPONEN ===")

    for nomor, komponen in enumerate(daftar, start=1):
        print(
            f"{nomor}. {komponen['nama']} "
            f"- Rp{komponen['harga']}"
        )


# Mengolah dan menganalisis biaya modifikasi
def analisis_biaya():
    daftar = baca_data()

    if len(daftar) == 0:
        print("Belum ada data untuk dianalisis.")
        return

    analisis = AnalisisModif(daftar)

    print("\n=== ANALISIS BIAYA ===")
    print("Total biaya: Rp", analisis.hitung_total())
    print("Rata-rata harga: Rp", analisis.hitung_rata_rata())
    print("Komponen termahal:", analisis.cari_termahal())

    print("\nUrutan harga termurah:")
    for komponen in analisis.urutkan_harga():
        print(komponen["nama"], "- Rp", komponen["harga"])

    try:
        batas = int(input("\nMasukkan batas anggaran: "))

        if batas < 0:
            raise ValueError("Anggaran tidak boleh negatif.")

        hasil = analisis.filter_anggaran(
            batas_harga=batas
        )

        print("\nKomponen sesuai anggaran:")
        if len(hasil) == 0:
            print("Tidak ada komponen yang sesuai anggaran.")
        else:
            for komponen in hasil:
                print(komponen["nama"], "- Rp", komponen["harga"])

    except ValueError as error:
        print("Input anggaran tidak valid:", error)


# Membuat laporan dari seluruh data
def tampilkan_laporan():
    daftar = baca_data()

    buat_laporan(
        daftar,
        jenis_motor="Motor matic",
        keterangan="Laporan biaya modifikasi"
    )


# Menjalankan program utama
def main():
    buat_file()

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_komponen()

        elif pilihan == "2":
            tampilkan_data()

        elif pilihan == "3":
            analisis_biaya()

        elif pilihan == "4":
            tampilkan_laporan()

        elif pilihan == "5":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak tersedia.")


# Menjalankan program saat main.py dibuka langsung
if __name__ == "__main__":
    main()