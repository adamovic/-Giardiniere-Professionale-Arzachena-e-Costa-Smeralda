import subprocess
import webbrowser
import time
import os

print("🌐 CONDIVISIONE SITO IMMEDIATA")
print("=" * 50)

# Metodo 1: Usare tunnelto.dev (gratuito, senza registrazione)
print("🚀 Metodo 1: tunnelto.dev (nessuna registrazione richiesta)")
try:
    print("📦 Installazione tunnelto...")
    subprocess.run(["py", "-m", "pip", "install", "tunnelto"], capture_output=True)
    
    print("🚀 Creazione tunnel pubblico...")
    process = subprocess.Popen(["tunnelto", "--port", "8000"], 
                           stdout=subprocess.PIPE, 
                           stderr=subprocess.PIPE, 
                           text=True)
    
    time.sleep(5)
    
    # Controlla output per il link
    try:
        output, error = process.communicate(timeout=10)
        if "tunnelto.dev" in output:
            lines = output.split('\n')
            for line in lines:
                if "tunnelto.dev" in line:
                    print("✅ LINK PUBBLICO CREATO!")
                    print("=" * 50)
                    print(f"🌍 {line.strip()}")
                    print("=" * 50)
                    print("📝 CONDIVIDI QUESTO LINK CON TUTTI!")
                    webbrowser.open(line.strip())
                    input("\nPremi INVIO per chiudere...")
                    exit()
    except:
        pass
        
except Exception as e:
    print(f"❌ Errore tunnelto: {e}")

print("\n🔄 Provo metodo alternativo...")

# Metodo 2: localtunnel (gratuito)
try:
    print("🚀 Metodo 2: localtunnel")
    subprocess.run(["py", "-m", "pip", "install", "localtunnel"], capture_output=True)
    
    print("🚀 Avvio localtunnel...")
    print("Questo creerà un link pubblico immediato!")
    print("Attendi 10 secondi...")
    
    # Avvia localtunnel
    process = subprocess.Popen(["lt", "--port", "8000"], 
                           stdout=subprocess.PIPE, 
                           stderr=subprocess.PIPE, 
                           text=True)
    
    time.sleep(10)
    
    # Controlla output per il link
    try:
        output, error = process.communicate(timeout=5)
        if "https://" in output:
            lines = output.split('\n')
            for line in lines:
                if "https://" in line and "your url is:" in line.lower():
                    url = line.split("your url is:")[-1].strip()
                    print("✅ LINK PUBBLICO CREATO!")
                    print("=" * 50)
                    print(f"🌍 {url}")
                    print("=" * 50)
                    print("📝 CONDIVIDI QUESTO LINK CON TUTTI!")
                    webbrowser.open(url)
                    input("\nPremi INVIO per chiudere...")
                    exit()
    except:
        pass
        
except Exception as e:
    print(f"❌ Errore localtunnel: {e}")

print("\n📱 SOLUZIONI ALTERNATIVE:")
print("1. 🌍 Link locale (tutta la rete): http://192.168.28.1:8000/")
print("2. 🌐 Iscriviti a ngrok: https://ngrok.com/signup")
print("3. 🚀 Usa Netlify: https://netlify.com/")
print("\n🌿 Il tuo sito Adil ELMERABET è pronto!")
