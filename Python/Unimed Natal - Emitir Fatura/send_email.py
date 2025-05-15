import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import smtplib
from config import SENDER_MAIL, SENDER_PASS, RECEIVERS_MAILS

def send_mail(invoice_generated, invoice_path=None):

    if invoice_generated:
        subject = "BOT SEGUNDA VIA FATURA UNIMED (PYTHON) - SUCESSO"
        body = "A fatura foi emitida e segue em anexo neste e-mail."
    else:
        subject = "BOT SEGUNDA VIA FATURA UNIMED (PYTHON) - ATENÇÃO"
        body = "Não havia fatura disponível para emissão."

    message = MIMEMultipart()
    message["From"] = SENDER_MAIL
    message["To"] = ", ".join(RECEIVERS_MAILS)
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Anexar fatura se disponível
    if invoice_generated and invoice_path:
        try:
            with open(invoice_path, "rb") as arquivo:
                attach = MIMEApplication(arquivo.read(), _subtype="pdf")
                attach.add_header("Content-Disposition", "attachment", filename=os.path.basename(invoice_path))
                message.attach(attach)
        except Exception as e:
            print(f"Erro ao anexar fatura: {e}")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_MAIL, SENDER_PASS)
            server.sendmail(SENDER_MAIL, RECEIVERS_MAILS, message.as_string())
            print("E-mail enviado com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

def send_error_mail(error_message):

    subject = "BOT SEGUNDA VIA FATURA UNIMED (PYTHON) - ERRO"
    body = f"{error_message}"

    message = MIMEMultipart()
    message["From"] = SENDER_MAIL
    message["To"] = ", ".join(RECEIVERS_MAILS)
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_MAIL, SENDER_PASS)
            server.sendmail(SENDER_MAIL, RECEIVERS_MAILS, message.as_string())
            print("Email de erro enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar email de erro: {e}")