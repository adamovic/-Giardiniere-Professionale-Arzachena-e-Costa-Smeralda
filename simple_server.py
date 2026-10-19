import http.server
import socketserver
import threading
import requests
import time
import socket

# Ottieni un IP pubblico semplice
def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        return response.json()['ip']
    except:
        return "localhost"

# Configura il server
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

# Trova un IP locale funzionante
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print("🌐 AVVIO SERVER PUBBLICO PER IL TUO SITO")
print("=" * 50)
print(f"📱 IP Locale: {local_ip}")
print(f"🌍 IP Pubblico: {get_public_ip()}")
print("=" * 50)

# Avvia il server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"✅ Server attivo su:")
    print(f"   🏠 Locale: http://{local_ip}:{PORT}/")
    print(f"   🌍 Pubblico: http://{get_public_ip()}:{PORT}/")
    print("=" * 50)
    print("📝 CONDIVIDI QUESTO LINK CON TUTTI:")
    print(f"   http://{get_public_ip()}:{PORT}/")
    print("=" * 50)
    print("⚠️  Nota: Assicurati che il firewall permetta connessioni sulla porta 8000")
    print("🛑 Per fermare il server, premi CTRL+C")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server fermato")
