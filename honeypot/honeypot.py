import socket
import json
import time
import redis
import os

r = None
while r is None:
    try:
        r = redis.Redis(host='redis_db', port=6379, db=0)
        r.ping()
        print("[*] Redis baglantisi basarili!")
    except:
        print("[!] Redis bekleniyor...")
        time.sleep(5)

def start_honeypot(port=9999):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', port))
    server.listen(5)
    print(f"[*] Honeypot {port} portunda dinlemede...")

    while True:
        try:
            client, addr = server.accept()
            client.send(b"Password: ")
            password = client.recv(1024).decode(errors='ignore').strip()
            client.close()
            
            log_data = {"timestamp": time.strftime("%H:%M:%S"), "ip": addr[0], "password": password}
            r.lpush('attacks', json.dumps(log_data))
            print(f"[!] KAYDEDILDI: {addr[0]} - {password}")
        except:
            pass

if __name__ == "__main__":
    start_honeypot()