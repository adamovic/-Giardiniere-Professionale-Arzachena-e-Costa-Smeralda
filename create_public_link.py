from pyngrok import ngrok
import os

# Avvia un tunnel ngrok sulla porta 8000
public_tunnel = ngrok.connect(8000)

print("🌐 IL TUO SITO È ORA ONLINE PER TUTTI!")
print("=" * 50)
print(f"📱 Link Pubblico: {public_tunnel.public_url}")
print("=" * 50)
print("✅ Condividi questo link con chiunque!")
print("📝 Il link rimarrà attivo finché questo programma è in esecuzione")
print("\nPer fermare il link, chiudi questa finestra o premi CTRL+C")

# Mantieni il tunnel attivo
try:
    input("\nPremi INVIO per fermare il tunnel...")
except KeyboardInterrupt:
    print("\n🛑 Tunnel chiuso")

ngrok.disconnect(public_tunnel.public_url)
print("✅ Link pubblico disattivato")
