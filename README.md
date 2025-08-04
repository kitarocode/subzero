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


ENGLISH LANGUAGE~
# Subzero.xyz Waitlist Bot

A Python bot for automatically submitting waitlists to the website https://www.subzero.xyz/ using the requests library.

## Features

- ✅ Read email lists from the `email.txt` file
- ✅ Automatically generate usernames from emails + random numbers
- ✅ Submit to various endpoints that may be used
- ✅ Delay 3-6 seconds between requests (random)
- ✅ Log results to the `result.txt` file
- ✅ Complete headers and payload
- ✅ Analyze the website to find the correct endpoint

## Installation

1. Install Python 3.7+ if not already installed
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### 1. Prepare Email List

Edit the `email.txt` file and enter the email list (one per line):
```
email1@domain.com
email2@domain.com
email3@domain.com
```

### 2. Run the Bot (Recommended)

Use the optimized script:
```bash
python final_waitlist_bot.py
```

### 3. Website Analysis (Optional)

If you want to analyze the website first:
```bash
python analyze_endpoint.py
```

### 4. Test Single Email (Optional)

To test with a single email:
```bash
python test_single.py
```

## Output Files

### result.txt
This file will contain the submission results for each email:
```
=== SUBZERO WAITLIST BOT RESULTS ===
Started at: 2024-01-15 10:30:00
Total emails: 5

Email 1: test1@example.com
Username: test1123
Success: True
Endpoint: /api/waitlist
Status Code: 200
Response: {“success”: true, ‘message’: “Added to waitlist”}
--------------------------------------------------

### website_analysis.json
Website analysis results to find the correct endpoint.

## Configuration

### Endpoints Used
The bot uses endpoints that have been proven to work:
- `/api/subscribe` ✅ (CONFIRMED WORKING)

### Payloads Used
The bot uses payloads that have been proven to work:
```json
{“email”: “user@example.com”}
```

### Headers
The bot uses complete headers including:
- User-Agent (Chrome browser)
- Accept headers
- Security headers (Sec-Fetch-*)
- CSRF token (if found)

## Troubleshooting

### Error “All attempts failed”
1. Run `analyze_endpoint.py` to see available endpoints
2. Check if the website uses reCAPTCHA or anti-bot protection
3. Try with a longer delay (edit `random.uniform(3, 6)` to `random.uniform(10, 15)`)

### Error “Connection timeout”
1. Check your internet connection
2. Try with a longer timeout (edit `timeout=30` to `timeout=60`)

### Error “CSRF token not found”
This is normal if the website does not use CSRF protection. The bot will still function.

## Security and Ethics

⚠️ **Warning:**
- Use this bot responsibly
- Do not spam or abuse websites
- Respect the website's Terms of Service
- Use only for testing or legitimate purposes

## File Structure

```
subzero-waitlist-bot/
├── main.py   # ✅ Optimized main script
├── email.txt              # Email list (create your own)
├── requirements.txt       # Python dependencies
├── README.md
└── result.txt            # Submission results (created automatically)
```

## Dependencies

- `requests>=2.31.0` - HTTP library for requests

## License

This script is created for educational and testing purposes. Use it responsibly.
