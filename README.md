# Raspberry Pi Pico: Simon Vault 🔐🎮

![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![MicroPython](https://img.shields.io/badge/Language-MicroPython-blue)
![Platform](https://img.shields.io/badge/Platform-Raspberry_Pi_Pico-red)

**Simon Vault** adalah proyek sistem tertanam (*embedded system*) berbasis Raspberry Pi Pico yang menggabungkan keamanan digital dengan permainan memori klasik. Proyek ini mensimulasikan sistem brankas yang dilindungi password, di mana akses yang berhasil akan membuka permainan "Simon Says" interaktif.

Proyek ini mendemonstrasikan penggunaan logika *State Machine*, komunikasi I2C (LCD), manipulasi GPIO kompleks (7-Segment & LED), serta modulasi PWM (Buzzer) menggunakan MicroPython.

---

## 🌟 Fitur Utama

* **Sistem Keamanan Ganda**:
    * **Vault Mode**: Membutuhkan input PIN 4-digit yang benar melalui tombol fisik untuk membuka sistem.
    * **Feedback Visual & Audio**: Indikator status (Locked/Unlocked/Error) melalui LCD dan suara buzzer yang berbeda.
* **Permainan Simon Says**:
    * Permainan memori visual dan audio yang dimulai otomatis setelah brankas terbuka.
    * **Infinite Levels**: Kesulitan meningkat seiring bertambahnya skor pengguna.
    * **Randomized Pattern**: Pola permainan dihasilkan secara acak setiap sesi.
* **Antarmuka Hardware Lengkap**:
    * **LCD 20x4 (I2C)**: Menampilkan instruksi, status, dan pesan game.
    * **7-Segment Display**: Menampilkan masking input password dan skor permainan terkini.
    * **RGB+Y LEDs**: Indikator visual untuk permainan.

---

## 🛠️ Teknologi & Hardware

Proyek ini dibangun menggunakan teknologi berikut:

* **Microcontroller**: Raspberry Pi Pico / Pico W
* **Bahasa Pemrograman**: [MicroPython](https://micropython.org/)
* **Komponen Hardware**:
    * 1x I2C LCD (20x4 atau 16x2)
    * 1x 7-Segment Display (Common Cathode)
    * 4x Push Button (Pull-up)
    * 4x LED (Merah, Hijau, Biru, Kuning)
    * 1x Buzzer (PWM)
* **Simulator**: Mendukung simulasi penuh di [Wokwi](https://wokwi.com/).

---

## 🔌 Konfigurasi Pin (Wiring)

Pastikan merangkai komponen sesuai dengan tabel berikut agar kode berjalan dengan benar:

| Komponen | Pin Komponen | Raspberry Pi Pico (GP) |
| :--- | :--- | :--- |
| **I2C LCD** | SDA | `GP4` |
| | SCL | `GP5` |
| **Tombol (Input)** | Tombol 1 | `GP11` |
| | Tombol 2 | `GP12` |
| | Tombol 3 | `GP13` |
| | Tombol 4 | `GP10` |
| **LED (Output)** | LED 1 (Merah) | `GP16` |
| | LED 2 (Hijau) | `GP17` |
| | LED 3 (Biru) | `GP18` |
| | LED 4 (Kuning)| `GP19` |
| **7-Segment** | Seg A, B, C | `GP0`, `GP1`, `GP6` |
| | Seg D, E, F | `GP7`, `GP8`, `GP9` |
| | Seg G | `GP14` |
| **Buzzer** | PWM Pin | `GP20` |

---

## 📥 Prasyarat & Instalasi

### 1. Persiapan Environment
* Pastikan Raspberry Pi Pico sudah di-flash dengan firmware **MicroPython** terbaru.
* Gunakan IDE seperti **Thonny** atau **VS Code** (dengan ekstensi Pico-Go).

### 2. Instalasi Kode
Clone repository ini atau unduh file secara manual:

```bash
git clone [https://github.com/username/raspberry-pi-pico-simon-vault.git](https://github.com/username/raspberry-pi-pico-simon-vault.git)
````

### 3\. Upload File ke Pico

Salin file-file berikut ke direktori *root* Raspberry Pi Pico Anda:

  * `main.py` (Logika utama program)
  * `pico_i2c_lcd.py` (Library driver LCD)
  * `buzzer_lib.py` (Library nada buzzer)

-----

## 📖 Cara Penggunaan

1.  **Menyalakan Sistem**:
    Hubungkan Pico ke sumber daya. LCD akan menampilkan pesan untuk memasukkan password.

2.  **Membuka Brankas (Unlock)**:
    Masukkan kode default dengan menekan tombol secara berurutan:

    > **Password:** Tombol 1 ➔ Tombol 3 ➔ Tombol 2 ➔ Tombol 4

      * Setiap tekanan tombol akan menampilkan karakter `*` pada LCD dan garis pada 7-segment.
      * Jika benar: LCD menampilkan "AKSES TERBUKA" dan permainan dimulai.
      * Jika salah: Buzzer berbunyi nada error dan sistem mereset input.

3.  **Bermain Simon Says**:

      * Perhatikan urutan nyala LED dan suaranya.
      * Ulangi urutan tersebut dengan menekan tombol yang sesuai (Tombol 1 untuk LED 1, dst).
      * Jika benar, level naik dan urutan bertambah panjang.
      * Skor level Anda ditampilkan di layar 7-Segment.

-----

## 📂 Struktur Project

```text
.
├── main.py             # Entry point: Logika utama Vault & Game
├── buzzer_lib.py       # Modul helper untuk nada dan frekuensi buzzer
├── pico_i2c_lcd.py     # Driver class untuk mengontrol LCD via I2C
├── diagram.json        # File konfigurasi untuk simulasi Wokwi
├── README.md           # Dokumentasi proyek
└── LICENSE             # Lisensi MIT
```

-----

## 🤝 Kontribusi

Kontribusi sangat terbuka\! Jika Anda ingin meningkatkan fitur atau memperbaiki bug:

1.  Fork repository ini.
2.  Buat branch fitur baru (`git checkout -b fitur-keren`).
3.  Commit perubahan Anda (`git commit -m 'Menambahkan fitur keren'`).
4.  Push ke branch tersebut (`git push origin fitur-keren`).
5.  Buat Pull Request.

-----

## 📄 Lisensi

Proyek ini didistribusikan di bawah lisensi **MIT**.

```text
Copyright (c) 2025 CherryYume夢

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

Lihat file [LICENSE](https://www.google.com/search?q=./LICENSE) untuk informasi lebih lanjut.
