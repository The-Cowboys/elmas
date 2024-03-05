import sys
import smtplib 
from email.message import EmailMessage

# Configuración del servidor de correos
email_smtp = "smtp.office365.com"  

emisor = "elmastontocow@hotmail.com"
email_password = "MasMasTonto123"

def enviar_correo(destinatarios, el_tonto):

    print("Enviando correo...")
    
    print("Tonto: ", el_tonto)
    
    print("Destinatarios: ", destinatarios)
     
    print("Args: ", sys.argv)

    # server = smtplib.SMTP(email_smtp, 587) 
    # server.ehlo() 
    # server.starttls()
    # server.login(emisor, email_password)

    # # Crear un objeto de email 
    # message = EmailMessage()

    # # Configurar el email 
    # message['Subject'] = "El mas tonto del dia es..."
    # message['From'] = emisor
    # message['To'] = destinatarios
    # message.set_content(f"Felicidades, {el_tonto} es el mas tonto :D")

    # server.send_message(message)

    # server.quit()
