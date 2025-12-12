# 📘 Dokumentasi LCD 20x4

![Banner](https://img.shields.io/badge/Status-Documentation-blue?style=for-the-badge&logo=markdown)
![Hardware](https://img.shields.io/badge/Hardware-Raspberry_Pi_Pico-red?style=for-the-badge&logo=raspberrypi)


# Layar LCD (20x4 I2C)

LCD (*Liquid Crystal Display*) adalah "wajah" dari sistem ini. Layar ini bertugas menampilkan instruksi password, status permainan, dan pesan error. Kita menggunakan modul tambahan **I2C** (chip hitam di belakang layar) agar pemasangan kabel jauh lebih sederhana.

### 🔌 Panduan Pemasangan (Wiring)

Hubungkan 4 kaki dari modul LCD ke Raspberry Pi Pico mengikuti tabel berikut:

| Kaki LCD | Sambung ke Pico | Warna Kabel (Saran) | Fungsi |
| :--- | :--- | :--- | :--- |
| **GND** | **GND** (Pin 3, 8, dll) | ⬛ Hitam | **Ground** (Jalur negatif/pembuangan). |
| **VCC** | **VBUS** (Pin 40) | 🟥 Merah | **Power** (Sumber listrik 5 Volt). |
| **SDA** | **GP4** (Pin 6) | 🟧 Oranye | **Data** (Jalur pengirim huruf/angka). |
| **SCL** | **GP5** (Pin 7) | 🟪 Ungu | **Clock** (Pengatur irama pengiriman). |

> **⚠️ Peringatan:** Jangan sampai tertukar antara **VCC** dan **GND**. Kesalahan ini dapat menyebabkan modul LCD panas dan rusak seketika.

### 🧠 Bedah Logika & Perhitungan (Untuk Orang Awam)

#### 1. Kenapa Pakai I2C? (Analogi Kurir)
Bayangkan Anda ingin mengirim surat.
* **Cara Lama (Parallel):** Anda butuh 8 jalur kabel data + 3 jalur kontrol = 11 kabel hanya untuk mencetak satu huruf. Ini boros tempat.
* **Cara I2C (Serial):** Anda hanya butuh **2 kabel**:
    * **SDA (Kurir):** Membawa paket data (huruf 'A', 'B', dll).
    * **SCL (Satpam):** Membawa peluit (Clock) untuk mengatur kapan paket boleh dikirim supaya tidak tabrakan.

#### 2. Matematika Koordinat Layar
Dalam kode, Anda sering melihat perintah seperti: `lcd.move_to(5, 0)`.
Layar LCD 20x4 itu ibarat sebuah kertas milimeter blok atau *spreadsheet* Excel:

* **Punya 4 Baris (Y):** Dihitung dari 0 sampai 3 (Atas ke Bawah).
* **Punya 20 Kolom (X):** Dihitung dari 0 sampai 19 (Kiri ke Kanan).

**Rumus:** `(Kolom, Baris)`

* `move_to(0, 0)` = Pojok Kiri Atas.
* `move_to(5, 0)` = Baris paling atas, geser 5 kotak ke kanan.
* `move_to(0, 1)` = Awal baris kedua.

#### 3. Alamat Rumah (Address 0x27)
Komputer (Pico) perlu tahu ke mana data harus dikirim. Modul LCD ini memiliki "alamat rumah" digital, biasanya **0x27**. Jika alamat ini salah, Pico akan berteriak "LCD Error" karena tidak menemukan rumah yang dituju.

---

## 📜 Lisensi (MIT License)

Proyek dan dokumentasi ini dilindungi di bawah Lisensi MIT.

```text
MIT License

Copyright (c) 2025 CherryYume夢

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
````

-----

**© Documentation by Liwirya**
