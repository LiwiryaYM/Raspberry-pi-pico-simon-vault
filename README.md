<div align="center">
  <img src="https://via.placeholder.com/150?text=Simon+Vault+Logo" alt="Simon Vault Logo" width="150" height="150" />
  
  # Raspberry Pi Pico: Simon Vault
  
  <p>
    <b>Sistem Keamanan Brankas & Permainan Memori Berbasis MicroPython</b>
  </p>

  <a href="https://micropython.org/">
    <img src="https://img.shields.io/badge/Language-MicroPython-orange?style=flat-square&logo=python&logoColor=white" alt="MicroPython">
  </a>
  <a href="https://www.raspberrypi.com/products/raspberry-pi-pico/">
    <img src="https://img.shields.io/badge/Hardware-Raspberry_Pi_Pico-red?style=flat-square&logo=raspberrypi&logoColor=white" alt="Raspberry Pi Pico">
  </a>
  <a href="https://wokwi.com/">
    <img src="https://img.shields.io/badge/Simulator-Wokwi-blue?style=flat-square" alt="Wokwi">
  </a>
  <a href="./LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License">
  </a>
</div>

---

## 📝 Gambaran Proyek

**Simon Vault** menggabungkan konsep keamanan digital dengan hiburan interaktif. Proyek ini mensimulasikan mekanisme brankas elektronik yang dilindungi PIN, yang apabila berhasil dibuka, akan memberikan akses ke permainan memori klasik "Simon Says".

Dirancang sebagai media pembelajaran *embedded system*, proyek ini mencakup implementasi:
* **State Machine Logic** (Locked → Unlocked → Game Mode).
* **Komunikasi I2C** untuk manajemen tampilan LCD.
* **Handling GPIO Kompleks** (Input Matrix & Output LED/7-Segment).
* **Pulse Width Modulation (PWM)** untuk sintesis audio sederhana.

---

## ⚡ Fitur Utama

### 1. Sistem Keamanan (Vault Mode)
* **PIN Protection**: Akses dilindungi oleh kombinasi 4 tombol unik.
* **Secure Feedback**: Karakter input disamarkan (masked) pada layar LCD dan 7-Segment untuk privasi.
* **Auto-Lock**: Sistem otomatis terkunci kembali saat reset atau *power cycle*.

### 2. Permainan Interaktif (Game Mode)
* **Infinite Progression**: Tingkat kesulitan (jumlah urutan) bertambah tanpa batas seiring keberhasilan pemain.
* **Random Pattern Generation**: Pola permainan dihasilkan secara acak menggunakan *hardware timer entropy*.
* **Audio-Visual Feedback**: Sinkronisasi antara nyala LED dan nada *buzzer* yang berbeda untuk setiap warna.

---

## 🔧 Spesifikasi Teknis

Daftar teknologi dan perangkat keras yang digunakan dalam proyek ini:

| Kategori | Komponen / Teknologi | Keterangan |
| :--- | :--- | :--- |
| **Microcontroller** | Raspberry Pi Pico W | Otak utama sistem |
| **Bahasa** | MicroPython v1.20+ | *Logic* pemrograman |
| **Display 1** | LCD 20x4 (I2C) | Antarmuka teks utama |
| **Display 2** | 7-Segment (1-Digit) | Indikator level & masking |
| **Input** | 4x Push Button | Navigasi & Input Game |
| **Output** | 4x LED (R/G/B/Y) + Buzzer | Indikator Game & Suara |

---

## 🔌 Panduan Wiring

Pastikan koneksi pin sesuai dengan tabel di bawah ini untuk fungsionalitas yang benar:

### I2C LCD
* **SDA**: `GP4`
* **SCL**: `GP5`

### Input (Tombol) & Output (LED)
| Index | Tombol (Input) | LED (Output) | Warna |
| :---: | :---: | :---: | :--- |
| **1** | `GP11` | `GP16` | Merah |
| **2** | `GP12` | `GP17` | Hijau |
| **3** | `GP13` | `GP18` | Biru |
| **4** | `GP10` | `GP19` | Kuning |

### Indikator Tambahan
* **7-Segment (A-G)**: `GP0`, `GP1`, `GP6`, `GP7`, `GP8`, `GP9`, `GP14`
* **Buzzer (PWM)**: `GP20`

---

## 🚀 Instalasi & Penggunaan

### Prasyarat
1.  **Python Environment**: Thonny IDE atau VS Code.
2.  **Firmware**: MicroPython terbaru terpasang pada Pico.

### Langkah Instalasi
1.  **Clone Repository**:
    ```bash
    git clone [https://github.com/liwiryaym/raspberry-pi-pico-simon-vault.git](https://github.com/liwiryaym/raspberry-pi-pico-simon-vault.git)
    ```
2.  **Upload File**:
    Salin file `main.py`, `pico_i2c_lcd.py`, dan `buzzer_lib.py` ke direktori root Pico.

### Cara Bermain
1.  **Buka Kunci**: Saat layar menampilkan "INPUT PASSWORD", masukkan urutan:
    > **Tombol 1 → Tombol 3 → Tombol 2 → Tombol 4**
2.  **Mulai Game**: Setelah akses terbuka, ikuti pola nyala lampu LED.
3.  **Input Ulang**: Tekan tombol sesuai urutan lampu yang menyala.
4.  **Skor**: Level Anda saat ini akan ditampilkan pada layar 7-Segment.

---

## 📂 Struktur Direktori

```text
raspberry-pi-pico-simon-vault/
├── main.py             # Program utama (Logic, Game Loop)
├── buzzer_lib.py       # Library kontrol nada & frekuensi
├── pico_i2c_lcd.py     # Driver LCD I2C
├── diagram.json        # Skema simulasi (Wokwi)
├── LICENSE             # Dokumen Lisensi MIT
└── README.md           # Dokumentasi Proyek
