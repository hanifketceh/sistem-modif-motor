# Sistem Modif Motor

## Deskripsi

Sistem Modif Motor adalah program berbasis Python untuk mengelola daftar komponen modifikasi motor dan menghitung biaya modifikasi.

## Fitur

* Menambahkan komponen modifikasi.
* Menyimpan data ke file teks.
* Menampilkan daftar komponen.
* Menghitung total dan rata-rata biaya.
* Menampilkan komponen termahal.
* Mengurutkan komponen berdasarkan harga.
* Memfilter komponen berdasarkan anggaran.
* Membuat laporan biaya modifikasi.
* Menguji fungsi menggunakan `unittest`.

## Struktur Proyek

* `main.py`: program utama.
* `modif_motor/validasi.py`: validasi input.
* `modif_motor/processing.py`: class dan pengolahan data.
* `modif_motor/fileio.py`: pengelolaan file data dan laporan.
* `modif_motor/testing.py`: pengujian mandiri.
* `tests/test_modif_motor.py`: kumpulan pengujian program.
* `data/`: penyimpanan data komponen.
* `laporan/`: penyimpanan laporan.

## Persyaratan

Python 3.

## Cara Menjalankan

Jalankan program dari folder utama proyek:

```bash
python3 main.py
```

## Cara Menjalankan Pengujian

Pengujian mandiri:

```bash
python3 -m modif_motor.testing
```

Seluruh pengujian:

```bash
python3 -m unittest discover -s tests -v
```
# sistem-modif-motor
