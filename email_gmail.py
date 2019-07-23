import smtplib, getpass, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encoder_base64

print( "*** Enviar email con GMAIL ***" )
user = input( "Cuenta de Gmail: " )
password = getpass.getpass( "Password: " )

#Para las cabeceras del email
remitente = input( "From, Ejemplo: admin <admin@correo.com>:" )
destinatario = input( "To, ejemplo: amigo <amigo@correo.com>:" )
asunto = input( "Subject, Asunto del mensaje: " )
mensaje = input( "Mensaje HTML: " )
archivo = input( "Adjuntar Archivo: " )

#Host y puerto SMTP de Gmail
gmail = smtplib( 'smtp.gmail.com', 587 )

#Protocolo de cifrado de datos utilizado por gmail
gmail.starttls()

#Credenciales
gmail.login( user, password )

#Muestra la depuración de la operación de envío
gmail.set_debuglevel( 1 )

header = MIMEMultipart()
header['Subject'] = asunto
header['From'] = remitente
header['To'] = destinatario

mensaje = MIMEText( mensaje, 'HTML' )
header.attach( mensaje )

if( os.path.isfile( archivo ) ):
    adjunto = MIMEBase( 'application', '' )

#Enviar email
gmail.sendmail( remitente, destinatario, header.as_string() )

#Cerrar conexión smtp
gmail.quit()
