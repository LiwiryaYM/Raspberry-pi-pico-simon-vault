# 📘 Dokumentasi : Buzzer

![Banner](https://img.shields.io/badge/Status-Documentation-blue?style=for-the-badge&logo=markdown)
![Hardware](https://img.shields.io/badge/Hardware-Raspberry_Pi_Pico-red?style=for-the-badge&logo=raspberrypi)

# Audio Buzzer (Piezo Speaker)

Buzzer adalah komponen yang mengubah sinyal listrik menjadi getaran suara. Ini memberikan efek "klik" saat tombol ditekan dan melodi saat menang/kalah.

### 🔌 Panduan Pemasangan (Wiring)

Buzzer memiliki 2 kaki. Perhatikan tanda **(+)** pada bodi buzzer jika menggunakan komponen asli.

| Kaki Buzzer | Sambung ke Pico | Fungsi |
| :--- | :--- | :--- |
| **Kaki Pendek (-)** | **GND** (Pin mana saja) | Negatif / Ground. |
| **Kaki Panjang (+)** | **GP20** (Pin 26) | Sinyal Data Suara (PWM). |

### 🧠 Bedah Logika & Perhitungan Nada

Di dalam kode `buzzer_lib.py`, terdapat angka-angka misterius seperti `262`, `330`, atau `32768`. Mari kita terjemahkan ke bahasa manusia.

#### 1. Konsep Hertz (Hz): Kecepatan Ketuk
Suara dihasilkan oleh getaran.
* Jika Anda mengetuk meja 1 kali per detik = 1 Hz.
* Jika Anda bisa mengetuk meja **262 kali per detik** = 262 Hz.
* Telinga manusia menerjemahkan "262 ketukan per detik" sebagai nada **Do (C)**.

#### 2. Tabel Rumus Nada
Angka frekuensi ini bukan asal tebak, melainkan standar musik internasional (Scale C4):

| Tombol | Warna LED | Nada Musik | Frekuensi (Hz) |
| :--- | :--- | :--- | :--- |
| Tombol 1 | Merah | **Do (C)** | 262 getaran/detik |
| Tombol 2 | Hijau | **Re (D)** | 294 getaran/detik |
| Tombol 3 | Biru | **Mi (E)** | 330 getaran/detik |
| Tombol 4 | Kuning | **Fa (F)** | 349 getaran/detik |

#### 3. Konsep PWM (Volume & Tenaga)
Buzzer dihubungkan ke kaki digital yang hanya punya dua kondisi: **Nyala (Hidup)** atau **Mati**. Lalu bagaimana cara mengatur volume agar tidak pecah?

Kita menggunakan teknik **PWM (Pulse Width Modulation)**:
* Pico menyalakan dan mematikan listrik ke buzzer ribuan kali per detik.
* Nilai Maksimal di Pico = **65535** (100% Tenaga).
* Di kode kita tertulis: `buzzer.duty_u16(32768)`.

**Perhitungannya:**
$$\text{Volume} = \frac{32768}{65535} \approx 50\%$$

Jadi, kita menyuruh buzzer bekerja dengan **setengah tenaga**. Ini membuat suaranya nyaring tapi jernih dan tidak merusak komponen.

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
