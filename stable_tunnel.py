from pyngrok import ngrok
import time
import webbrowser
import subprocess
import threading

print("🌐 SOLUTION NGROK STABLE")
print("=" * 50)

def keep_tunnel_alive():
    """Maintient le tunnel ngrok actif avec reconnexion automatique"""
    retry_count = 0
    max_retries = 5
    
    while retry_count < max_retries:
        try:
            print(f"🚀 Tentative de connexion {retry_count + 1}/{max_retries}")
            
            # Créer le tunnel
            public_tunnel = ngrok.connect(8000, proto="http")
            
            print("=" * 50)
            print("🎉 NOUVEAU LIEN PUBLIC CRÉÉ!")
            print("=" * 50)
            print(f"🌐 {public_tunnel.public_url}")
            print("=" * 50)
            print("📝 PARTAGEZ CE LIEN AVEC TOUT LE MONDE!")
            print("🔄 Reconnexion automatique en cas de déconnexion")
            print("=" * 50)
            
            # Ouvrir dans le navigateur
            webbrowser.open(public_tunnel.public_url)
            
            # Garder le tunnel actif
            start_time = time.time()
            while time.time() - start_time < 300:  # 5 minutes max par session
                time.sleep(10)
                # Vérifier si le tunnel est toujours actif
                try:
                    tunnels = ngrok.get_tunnels()
                    if not tunnels:
                        break
                except:
                    break
            
            # Fermer le tunnel actuel
            try:
                ngrok.disconnect(public_tunnel.public_url)
            except:
                pass
                
            print("🔄 Tunnel déconnecté, reconnexion...")
            retry_count += 1
            
        except Exception as e:
            print(f"❌ Erreur: {e}")
            retry_count += 1
            time.sleep(5)
    
    print("\n🛑 Nombre maximum de tentatives atteint")
    print("📱 Solutions alternatives:")
    print("1. Redémarrez ce script")
    print("2. Utilisez ngrok manuellement:")
    print("   - Installez ngrok: https://ngrok.com/download")
    print("   - Lancez: ngrok http 8000")
    print("3. Essayez localtunnel: npm install -g localtunnel && lt --port 8000")

# Démarrer le maintien du tunnel
keep_tunnel_alive()
