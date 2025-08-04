import requests
import time
import random
import json
from datetime import datetime

class OptimizedSubzeroWaitlistBot:
    def __init__(self):
        self.base_url = "https://www.subzero.xyz"
        self.session = requests.Session()
        
        # Headers yang sudah terbukti bekerja
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'DNT': '1',
            'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Content-Type': 'application/json'
        }
        
        self.session.headers.update(self.headers)
    
    def generate_username(self, email):
        """Generate username dari email dengan angka acak"""
        username_part = email.split('@')[0]
        random_number = random.randint(100, 999)
        return f"{username_part}{random_number}"
    
    def submit_waitlist(self, email, username):
        """Submit waitlist dengan endpoint yang sudah terbukti bekerja"""
        
        # Endpoint yang sudah terbukti bekerja
        endpoint = "/api/subscribe"
        url = f"{self.base_url}{endpoint}"
        
        # Payload yang sudah terbukti bekerja (hanya email)
        payload = {"email": email}
        
        try:
            response = self.session.post(url, json=payload, timeout=30)
            
            # Log response untuk debugging
            print(f"Endpoint: {endpoint}")
            print(f"Payload: {payload}")
            print(f"Status Code: {response.status_code}")
            
            # Jika berhasil (status 200)
            if response.status_code == 200:
                return {
                    'success': True,
                    'endpoint': endpoint,
                    'payload': payload,
                    'status_code': response.status_code,
                    'response': 'Success - Email added to waitlist'
                }
            else:
                return {
                    'success': False,
                    'endpoint': endpoint,
                    'payload': payload,
                    'status_code': response.status_code,
                    'response': response.text[:200]
                }
        
        except requests.exceptions.RequestException as e:
            return {
                'success': False,
                'endpoint': endpoint,
                'payload': payload,
                'status_code': None,
                'response': f'Request error: {e}'
            }
    
    def run(self):
        """Jalankan bot untuk semua email dalam file"""
        
        # Baca email dari file
        try:
            with open('email.txt', 'r', encoding='utf-8') as f:
                emails = [email.strip() for email in f.readlines() if email.strip()]
        except FileNotFoundError:
            print("❌ File email.txt tidak ditemukan!")
            return
        except Exception as e:
            print(f"❌ Error membaca file email.txt: {e}")
            return
        
        if not emails:
            print("❌ Tidak ada email dalam file email.txt!")
            return
        
        print("=== SUBZERO WAITLIST BOT (OPTIMIZED) ===")
        print(f"📧 Total emails: {len(emails)}")
        print(f"🎯 Target: {self.base_url}/api/subscribe")
        print(f"⏰ Delay: 3-6 seconds between requests")
        print("=" * 50)
        
        # Statistik
        success_count = 0
        failed_count = 0
        
        # Buka file result untuk menulis hasil
        with open('result.txt', 'w', encoding='utf-8') as result_file:
            result_file.write(f"=== SUBZERO WAITLIST BOT RESULTS ===\n")
            result_file.write(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            result_file.write(f"Total emails: {len(emails)}\n")
            result_file.write(f"Endpoint: /api/subscribe\n\n")
            
            for i, email in enumerate(emails, 1):
                print(f"\n[{i}/{len(emails)}] 📧 Processing: {email}")
                
                # Generate username (untuk log saja, tidak digunakan dalam payload)
                username = self.generate_username(email)
                print(f"👤 Generated username: {username}")
                
                # Submit waitlist
                result = self.submit_waitlist(email, username)
                
                # Update statistik
                if result['success']:
                    success_count += 1
                    status_icon = "✅"
                    status_text = "SUCCESS"
                else:
                    failed_count += 1
                    status_icon = "❌"
                    status_text = "FAILED"
                
                # Tulis hasil ke file
                result_file.write(f"Email {i}: {email}\n")
                result_file.write(f"Username: {username}\n")
                result_file.write(f"Success: {result['success']}\n")
                result_file.write(f"Endpoint: {result['endpoint']}\n")
                result_file.write(f"Status Code: {result['status_code']}\n")
                result_file.write(f"Response: {result['response']}\n")
                result_file.write("-" * 50 + "\n")
                
                # Print hasil ke console
                print(f"{status_icon} Result: {status_text}")
                
                # Tunggu sebelum request berikutnya (3-6 detik)
                if i < len(emails):  # Jangan tunggu setelah email terakhir
                    wait_time = random.uniform(3, 6)
                    print(f"⏳ Waiting {wait_time:.2f} seconds...")
                    time.sleep(wait_time)
            
            # Tulis statistik akhir
            result_file.write(f"\n=== FINAL STATISTICS ===\n")
            result_file.write(f"Total processed: {len(emails)}\n")
            result_file.write(f"Successful: {success_count}\n")
            result_file.write(f"Failed: {failed_count}\n")
            result_file.write(f"Success rate: {(success_count/len(emails)*100):.1f}%\n")
            result_file.write(f"Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        # Print statistik akhir
        print(f"\n" + "=" * 50)
        print(f"🎉 FINISHED!")
        print(f"📊 Statistics:")
        print(f"   Total: {len(emails)}")
        print(f"   ✅ Success: {success_count}")
        print(f"   ❌ Failed: {failed_count}")
        print(f"   📈 Success Rate: {(success_count/len(emails)*100):.1f}%")
        print(f"📄 Results saved to: result.txt")

def main():
    print("🚀 Starting Subzero Waitlist Bot...")
    bot = OptimizedSubzeroWaitlistBot()
    bot.run()

if __name__ == "__main__":
    main() 