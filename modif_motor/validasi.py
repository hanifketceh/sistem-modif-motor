
# Fungsi untuk memeriksa nama komponen modifikasi
def validasi_nama(nama):
    # Nama tidak boleh kosong
    if nama.strip() == "":
        raise ValueError("Nama komponen tidak boleh kosong")

    return nama.strip()


# Fungsi untuk memeriksa harga komponen
def validasi_harga(harga):
    # Mengubah harga menjadi angka
    try:
        harga = int(harga)
    except ValueError:
        raise ValueError("Harga harus berupa angka")

    # Harga tidak boleh negatif
    if harga < 0:
        raise ValueError("Harga tidak boleh negatif")

    return harga


# Fungsi untuk memeriksa seluruh data komponen
def validasi_data(nama, harga):
    # Memeriksa nama dan harga sebelum data digunakan
    nama = validasi_nama(nama)
    harga = validasi_harga(harga)

    return nama, harga


# Pengujian sederhana saat file dijalankan langsung
if __name__ == "__main__":
    print(validasi_data("Knalpot", 250000))
