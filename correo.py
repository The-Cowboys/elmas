import sys
import smtplib 
from email.message import EmailMessage

# Configuración del servidor de correos
email_smtp = "smtp.office365.com"  

emisor = sys.argv[1]
email_password = sys.argv[2]

def enviar_correo(destinatarios, el_tonto):
    server = smtplib.SMTP(email_smtp, 587) 
    server.ehlo() 
    server.starttls()
    server.login(emisor, email_password)

    # Crear un objeto de email 
    message = EmailMessage()

    # Configurar el email 
    message['Subject'] = "El mas tonto del dia es..."
    message['From'] = emisor
    message['To'] = destinatarios
    message.set_content(f"Felicidades, {el_tonto} es el mas tonto :D")

    server.send_message(message)

    server.quit()
