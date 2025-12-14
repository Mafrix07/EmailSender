import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Charge les variables d'environnement depuis le fichier .env
load_dotenv()

# --- Configuration ---
# Paramètres du serveur SMTP pour Gmail
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Récupère les identifiants depuis les variables d'environnement
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# --- Fonctions Principales ---

def send_email(recipient_email, subject, body):
    """
    Envoie un email en utilisant les identifiants des variables d'environnement.
    """
    # Vérification essentielle : s'assurer que l'email et le mot de passe sont définis dans le .env
    if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
        print("Erreur : Les variables d'environnement EMAIL_ADDRESS et EMAIL_PASSWORD doivent être définies.")
        print("Veuillez créer un fichier .env et y ajouter ces variables.")
        return

    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        print(f"Connexion à {SMTP_SERVER}...")
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Sécurise la connexion
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            print("Connexion réussie.")
            server.sendmail(EMAIL_ADDRESS, recipient_email, msg.as_string())
        print(f"Email envoyé avec succès à {recipient_email}")

    except smtplib.SMTPAuthenticationError:
        print("Erreur d'authentification SMTP. Vérifiez votre email et mot de passe (ou mot de passe d'application).")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

# --- Exécution ---

if __name__ == '__main__':
    # Ce bloc est exécuté lorsque le script est lancé directement
    # Exemple d'utilisation de la fonction send_email
    recipient_email = "ADDRESSE DU RECEPTEUR"
    subject = "Test d'envoi d'email via Python"
    body = "Ceci est un email de test envoyé depuis un script Python sécurisé."
    
    send_email(recipient_email, subject, body)