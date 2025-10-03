# Proyek MQTT Python: Kirim & Terima Pesan

Proyek ini berisi dua skrip Python sederhana untuk demonstrasi komunikasi MQTT menggunakan topik:

```
universitas teknologi yogyakarta/sahwan
```

## Daftar File

- `kirim_mqtt.py` — Mengirim minimal 5 pesan ke topik MQTT.
- `subscribe_mqtt.py` — Berlangganan dan menampilkan pesan yang diterima dari topik MQTT.

## Cara Menjalankan

### 1. Persiapan
- Pastikan Python sudah terinstal.
- Pastikan sudah menginstal dependensi dengan perintah:
  ```
  pip install paho-mqtt
  ```
- (Opsional) Gunakan virtual environment agar dependensi terisolasi.

### 2. Jalankan Subscriber (Penerima)
Buka terminal di folder proyek, lalu jalankan:
```
& ".venv/Scripts/python.exe" subscribe_mqtt.py
```
Biarkan terminal ini tetap berjalan untuk menerima pesan.

### 3. Jalankan Publisher (Pengirim)
Buka terminal baru, lalu jalankan:
```
& ".venv/Scripts/python.exe" kirim_mqtt.py
```
Skrip ini akan mengirim 5 pesan ke topik MQTT.

### 4. Lihat Hasil
Pesan yang dikirim akan muncul di terminal subscriber.

## Penjelasan Skrip

### kirim_mqtt.py
- Menghubungkan ke broker MQTT publik (broker.hivemq.com).
- Mengirim 5 pesan ke topik `universitas teknologi yogyakarta/sahwan`.

### subscribe_mqtt.py
- Menghubungkan ke broker MQTT publik.
- Berlangganan ke topik yang sama.
- Menampilkan pesan yang diterima secara real-time.

## Catatan
- Topik dan broker dapat diubah sesuai kebutuhan.
- Untuk penggunaan di lingkungan produksi, gunakan broker MQTT yang aman.

---

**Proyek ini dibuat untuk pembelajaran IoT dan komunikasi MQTT di Universitas Teknologi Yogyakarta.**
