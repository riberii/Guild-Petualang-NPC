# Guild Petualang NPC

Aplikasi CLI berbasis Python untuk mengelola pasukan NPC sebuah guild: merekrut anggota, menampilkan data, dan menganalisis kekuatan pasukan. Dibuat sebagai latihan Informatika kelas 11 (fungsi, class/PBO, file CSV, dan program multi-file).

## Fitur

- **Rekrut NPC**: validasi input, nama tidak boleh kembar, maksimal 5 anggota.
- **Lihat & Analisis Pasukan**: tabel pasukan, total/rata-rata HP, jumlah per peran, dan NPC terkuat.

## Struktur Proyek

```
guild_npc/
├── main.py         # Menu utama, membuka file lain dengan subprocess
├── models.py       # Class NPC (PBO)
├── rekrut_npc.py   # Menambah NPC ke npc.csv
├── tampil_npc.py   # Memuat data, menampilkan, dan menganalisis pasukan
└── npc.csv         # Data contoh (dibuat otomatis jika belum ada)
```

## Cara Menjalankan

Pastikan Python 3 sudah terpasang, lalu:

```bash
git clone https://github.com/USERNAME/guild-petualang-npc.git
cd guild-petualang-npc
python main.py
```

> Jika `python` tidak dikenali, gunakan `python3` (ubah juga pada `subprocess.run` di `main.py`).

## Contoh Alur

1. Pilih `1` untuk merekrut beberapa NPC (peran: `Prajurit`, `Penyihir`, atau `Tabib`).
2. Pilih `2` untuk melihat pasukan dan analisisnya.

## Konsep yang Dipakai

Fungsi, class dan objek (`__init__`, `to_list`, `__str__`), percabangan, perulangan `for` dan `while`, membaca/menulis file CSV, serta pemisahan program ke beberapa file.

## Lisensi

Proyek pembelajaran. Bebas digunakan untuk belajar.
