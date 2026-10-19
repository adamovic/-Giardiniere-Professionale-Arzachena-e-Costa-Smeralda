import subprocess
import webbrowser
import time
import threading

print("🌐 SOLUTION COMPLÈTE POUR PARTAGE SITE")
print("=" * 50)

def start_django_server():
    """Démarre le serveur Django en arrière-plan"""
    print("🚀 Démarrage du serveur Django...")
    process = subprocess.Popen([
        "venv\\Scripts\\python.exe", "manage.py", "runserver", "8000", "--noreload"
    ], cwd="c:\\Users\\PROBOOK2\\Documents\\projet_3ami_Adile")
    time.sleep(3)
    return process

def create_serveo_tunnel():
    """Crée un tunnel Serveo stable"""
    print("🌍 Création tunnel Serveo...")
    try:
        process = subprocess.Popen([
            "ssh", "-R", "80:localhost:8000", "serveo.net"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        time.sleep(5)
        
        # Lire le output pour trouver le lien
        for line in process.stdout:
            if "https://" in line:
                url = line.strip()
                print("=" * 50)
                print("🎉 LIEN PUBLIC CRÉÉ!")
                print("=" * 50)
                print(f"🌐 {url}")
                print("=" * 50)
                print("📝 PARTAGEZ CE LIEN!")
                webbrowser.open(url)
                return process
                
    except Exception as e:
        print(f"❌ Erreur Serveo: {e}")
        return None

# Démarrer le serveur Django
django_process = start_django_server()

# Créer le tunnel
tunnel_process = create_serveo_tunnel()

if tunnel_process:
    print("\n🔄 Serveurs actifs...")
    print("Appuyez sur Ctrl+C pour arrêter")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Arrêt des serveurs...")
        django_process.terminate()
        tunnel_process.terminate()
        print("✅ Arrêté")
else:
    print("\n📱 Instructions manuelles:")
    print("1. Assurez-vous que Django tourne: py manage.py runserver 8000")
    print("2. Installez ngrok: https://ngrok.com/download")
    print("3. Lancez: ngrok http 8000")
