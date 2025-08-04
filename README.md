# Subzero.xyz Waitlist Bot

Bot Python untuk auto-submit waitlist ke situs https://www.subzero.xyz/ menggunakan library requests.

## Fitur

- ✅ Baca daftar email dari file `email.txt`
- ✅ Generate username otomatis dari email + angka acak
- ✅ Submit ke berbagai endpoint yang mungkin digunakan
- ✅ Delay 3-6 detik antar request (random)
- ✅ Log hasil ke file `result.txt`
- ✅ Headers dan payload yang lengkap
- ✅ Analisis website untuk menemukan endpoint yang benar

## Instalasi

1. Install Python 3.7+ jika belum ada
2. Install dependensi:
```bash
pip install -r requirements.txt
```

## Penggunaan

### 1. Persiapan Email List

Edit file `email.txt` dan masukkan daftar email (satu per baris):
```
email1@domain.com
email2@domain.com
email3@domain.com
```

### 2. Jalankan Bot (Recommended)

Gunakan skrip yang sudah dioptimalkan:
```bash
python final_waitlist_bot.py
```

### 3. Analisis Website (Opsional)

Jika ingin menganalisis website terlebih dahulu:
```bash
python analyze_endpoint.py
```

### 4. Test Single Email (Opsional)

Untuk test dengan satu email:
```bash
python test_single.py
```

## File Output

### result.txt
File ini akan berisi hasil submit untuk setiap email:
```
=== SUBZERO WAITLIST BOT RESULTS ===
Started at: 2024-01-15 10:30:00
Total emails: 5

Email 1: test1@example.com
Username: test1123
Success: True
Endpoint: /api/waitlist
Status Code: 200
Response: {"success": true, "message": "Added to waitlist"}
--------------------------------------------------
```

### website_analysis.json
Hasil analisis website untuk menemukan endpoint yang benar.

## Konfigurasi

### Endpoint yang Digunakan
Bot menggunakan endpoint yang sudah terbukti bekerja:
- `/api/subscribe` ✅ (CONFIRMED WORKING)

### Payload yang Digunakan
Bot menggunakan payload yang sudah terbukti bekerja:
```json
{"email": "user@example.com"}
```

### Headers
Bot menggunakan headers yang lengkap termasuk:
- User-Agent (Chrome browser)
- Accept headers
- Security headers (Sec-Fetch-*)
- CSRF token (jika ditemukan)

## Troubleshooting

### Error "All attempts failed"
1. Jalankan `analyze_endpoint.py` untuk melihat endpoint yang tersedia
2. Periksa apakah website menggunakan reCAPTCHA atau anti-bot protection
3. Coba dengan delay yang lebih lama (edit `random.uniform(3, 6)` menjadi `random.uniform(10, 15)`)

### Error "Connection timeout"
1. Periksa koneksi internet
2. Coba dengan timeout yang lebih lama (edit `timeout=30` menjadi `timeout=60`)

### Error "CSRF token not found"
Ini normal jika website tidak menggunakan CSRF protection. Bot akan tetap berfungsi.

## Keamanan dan Etika

⚠️ **Peringatan:**
- Gunakan bot ini dengan bertanggung jawab
- Jangan spam atau abuse website
- Hormati Terms of Service website
- Gunakan hanya untuk testing atau keperluan yang sah

## Struktur File

```
subzero-waitlist-bot/
├── main.py   # ✅ Skrip utama yang dioptimalkan
├── email.txt              # Daftar email (buat sendiri)
├── requirements.txt       # Dependensi Python
├── README.md             # Dokumentasi ini
└── result.txt            # Hasil submit (dibuat otomatis)
```

## Dependensi

- `requests>=2.31.0` - HTTP library untuk request

## Lisensi

Script ini dibuat untuk tujuan edukasi dan testing. Gunakan dengan bertanggung jawab. 