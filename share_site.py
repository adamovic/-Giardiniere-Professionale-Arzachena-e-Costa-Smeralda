import subprocess
import webbrowser
import time

print("🌐 CREAZIONE LINK PUBBLICO PER IL TUO SITO")
print("=" * 50)

# Prova con serveo (alternativa gratuita a ngrok)
try:
    print("📦 Installazione serveo...")
    subprocess.run(["py", "-m", "pip", "install", "serveo"], capture_output=True)
    
    print("🚀 Avvio tunnel pubblico...")
    print("Questo creerà un link che tutti potranno usare!")
    print("Attendi 10 secondi...")
    
    # Avvia serveo
    process = subprocess.Popen(["serveo"], 
                           stdout=subprocess.PIPE, 
                           stderr=subprocess.PIPE, 
                           text=True)
    
    time.sleep(10)
    
    # Controlla l'output per il link
    output, error = process.communicate(timeout=5)
    
    if "serveo.net" in output:
        lines = output.split('\n')
        for line in lines:
            if "serveo.net" in line:
                print("✅ LINK PUBBLICO TROVATO!")
                print("=" * 50)
                print(f"🌍 {line.strip()}")
                print("=" * 50)
                print("📝 CONDIVIDI QUESTO LINK CON TUTTI!")
                
                # Apre il link nel browser
                webbrowser.open(line.strip())
                break
    
except Exception as e:
    print(f"❌ Errore: {e}")
    print("🔄 Provo metodo alternativo...")
    
    # Metodo alternativo: localhost.run
    try:
        print("📦 Installazione localhost.run...")
        subprocess.run(["py", "-m", "pip", "install", "requests"], capture_output=True)
        
        import requests
        import threading
        
        def create_tunnel():
            response = requests.post('https://localhost.run/api/tunnels', 
                                  json={'port': 8000})
            if response.status_code == 200:
                data = response.json()
                url = data.get('url', '')
                if url:
                    print("✅ LINK PUBBLICO CREATO!")
                    print("=" * 50)
                    print(f"🌍 {url}")
                    print("=" * 50)
                    print("📝 CONDIVIDI QUESTO LINK CON TUTTI!")
                    webbrowser.open(url)
                    return url
        
        print("🚀 Creazione tunnel con localhost.run...")
        tunnel_url = create_tunnel()
        
        if tunnel_url:
            input("\nPremi INVIO per chiudere il tunnel...")
        
    except Exception as e2:
        print(f"❌ Errore alternativo: {e2}")
        print("📱 Usa il link locale invece:")
        print("http://127.0.0.1:8000/")

print("\n🌿 Il tuo sito Adil ELMERABET è pronto!")
