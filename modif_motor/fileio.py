
# Lokasi file data dan laporan
FILE_DATA = "data/modifikasi.txt"
FILE_LAPORAN = "laporan/laporan_modifikasi.txt"


# Membuat file data pertama kali
def buat_file():
    try:
        with open(FILE_DATA, "x") as file:
            file.write("Knalpot|250000\n")
            file.write("Roller CVT|75000\n")
            file.write("Lampu LED|100000\n")

        print("File data berhasil dibuat.")

    except FileExistsError:
        print("File data sudah tersedia.")


# Menambahkan komponen baru ke file
def simpan_data(nama, harga):
    with open(FILE_DATA, "a") as file:
        file.write(f"{nama}|{harga}\n")


# Membaca data dan melewati baris yang rusak
def baca_data():
    daftar_data = []

    try:
        with open(FILE_DATA, "r") as file:
            for baris in file:
                try:
                    nama, harga = baris.strip().split("|")
                    harga = int(harga)

                    if nama.strip() == "" or harga < 0:
                        continue

                    data = {
                        "nama": nama,
                        "harga": harga
                    }

                    daftar_data.append(data)

                except ValueError:
                    # Lewati baris yang formatnya tidak benar
                    continue

    except FileNotFoundError:
        print("File data belum tersedia.")

    return daftar_data


# Membuat laporan dengan informasi tambahan
def buat_laporan(data, **kwargs):
    try:
        with open(FILE_LAPORAN, "w") as file:
            file.write("LAPORAN MODIFIKASI MOTOR\n")
            file.write("=======================\n")

            # Menulis informasi tambahan laporan
            for nama_info, isi_info in kwargs.items():
                file.write(f"{nama_info}: {isi_info}\n")

            file.write("\nDAFTAR KOMPONEN\n")

            total = 0

            # Menulis komponen satu per satu
            for komponen in data:
                nama = komponen["nama"]
                harga = komponen["harga"]

                file.write(f"{nama} - Rp{harga}\n")
                total += harga

            file.write(f"\nTotal biaya: Rp{total}\n")

        print("Laporan berhasil disimpan.")

    except OSError:
        print("Laporan gagal disimpan.")


# Pengujian lokal fileio.py
if __name__ == "__main__":
    buat_file()

    daftar = baca_data()

    buat_laporan(
        daftar,
        jenis_motor="Motor matic",
        keterangan="Contoh laporan modifikasi"
    )

    print("Data berhasil dibaca:", daftar)