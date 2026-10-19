# Giardiniere Pro - Sito Web per Giardiniere Professionista

Sito web professionale per un giardiniere in Italia, sviluppato con Django, HTML/CSS e MySQL.

## 🌿 Caratteristiche

- **Homepage** con presentazione personale e servizi offerti
- **Galleria** dei lavori realizzati con foto prima/dopo
- **Form di contatto** per richieste di preventivi
- **Design responsive** per tutti i dispositivi
- **Lingua italiana** con contenuti localizzati
- **Database MySQL** per la gestione dei dati

## 🛠️ Tecnologie Utilizzate

- **Backend**: Django 4.2.7
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Database**: MySQL (XAMPP)
- **Email**: SMTP per notifiche contatti
- **Immagini**: Pillow per la gestione dei media

## 📋 Prerequisiti

- Python 3.8+
- MySQL/XAMPP installato
- pip (Python package manager)

## 🚀 Installazione

### 1. Clona il progetto
```bash
git clone <repository-url>
cd projet_3ami_Adile
```

### 2. Crea un ambiente virtuale
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Installa le dipendenze
```bash
pip install -r requirements.txt
```

### 4. Configura il database
1. Avvia XAMPP e avvia MySQL
2. Esegui lo script `setup_database.sql` in MySQL
3. Aggiorna le credenziali nel file `giardinaggio/settings.py`

### 5. Esegui le migrazioni
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crea un superutente (per l'admin)
```bash
python manage.py createsuperuser
```

### 7. Avvia il server di sviluppo
```bash
python manage.py runserver
```

## 📁 Struttura del Progetto

```
projet_3ami_Adile/
├── giardinaggio/          # Configurazione Django
│   ├── settings.py       # Impostazioni del progetto
│   ├── urls.py          # URL principali
│   └── wsgi.py          # Configurazione WSGI
├── core/                # App principale
│   ├── models.py        # Modelli database
│   ├── views.py         # Viste
│   ├── forms.py         # Form
│   ├── urls.py          # URL dell'app
│   └── admin.py         # Configurazione admin
├── templates/           # Template HTML
│   ├── base.html        # Template base
│   └── core/            # Template specifici
├── static/              # File statici
│   ├── css/            # Fogli di stile
│   └── images/         # Immagini
├── media/              # Media uploadati
├── requirements.txt    # Dipendenze Python
└── manage.py          # Script gestione Django
```

## ⚙️ Configurazione

### Database
Modifica le impostazioni del database in `giardinaggio/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'giardinaggio_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### Email
Configura le impostazioni email per il form di contatto:
```python
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'tua-email@gmail.com'
EMAIL_HOST_PASSWORD = 'tua-password-app'
```

## 📝 Utilizzo

### 1. Accedi all'admin
Vai su `http://localhost:8000/admin/` e accedi con le credenziali del superutente.

### 2. Aggiungi progetti
Nell'admin, puoi aggiungere:
- **Progetti**: Titolo, descrizione, immagini
- **Messaggi**: Visualizza i messaggi di contatto

### 3. Personalizza i contenuti
Modifica i template in `templates/core/` per personalizzare:
- Informazioni personali
- Contatti
- Servizi offerti

## 🌐 Funzionalità Principali

### Homepage
- Presentazione professionale
- Elenco dei servizi
- Anteprima dei lavori recenti
- Informazioni di contatto

### Galleria
- Visualizzazione completa dei progetti
- Immagini prima/dopo
- Descrizioni dettagliate

### Form di Contatto
- Invio messaggi diretti
- Notifica email automatica
- Gestione messaggi nell'admin

## 📱 Responsive Design

Il sito è completamente responsive e si adatta a:
- Desktop
- Tablet
- Smartphone

## 🔒 Sicurezza

- Protezione CSRF
- Validazione input
- Sicurezza file upload
- Configurazione per produzione

## 🚀 Deploy in Produzione

Per il deploy in produzione:
1. Imposta `DEBUG = False` in settings.py
2. Configura `ALLOWED_HOSTS`
3. Usa un server web come Apache/Nginx
4. Configura HTTPS
5. Ottimizza i file statici

## 📞 Supporto

Per assistenza o domande:
- Email: info@giardinierepro.it
- Telefono: +39 333 1234567

## 📄 Licenza

Questo progetto è open source e disponibile sotto licenza MIT.
