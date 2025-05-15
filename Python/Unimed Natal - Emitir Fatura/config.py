import os
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

# Variáveis sensíveis
LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")

SENDER_MAIL = os.getenv("SENDER_MAIL")
SENDER_PASS = os.getenv("SENDER_PASS")
RECEIVERS_MAILS = [email.strip() for email in os.getenv("RECEIVERS_MAILS", "").split(",") if email.strip()]

# Constantes
ELEMENT_WAIT_TIME = 5  # Espera por elementos sem troca de página
PAGE_WAIT_TIME = 10    # Espera por elementos após troca de página

# Caminho da pasta de downloads
DOWNLOAD_PATH = os.path.join(os.getcwd(), "downloads")
