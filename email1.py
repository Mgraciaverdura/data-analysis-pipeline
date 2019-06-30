import smtplib
import getpass
from email.mime.multipart import MIMEMultipart

gmail_user = input("Enter your gmail account: ")
gmail_password = getpass.getpass("Enter your password: ")
to = input("Who should receive the mail?")


# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Importante | Informe final"
msg['From'] = gmail_user
msg['To'] = to

# Create the body of the message (a plain-text and an HTML version).
text = 'Buenas tardes\n, a continuación encontrará el informe que prometí en mandarle. \nUn saludo.'

# Send the message via local SMTP server.
mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login('userName', 'password')
mail.sendmail(gmail_user, to, msg.as_string())
mail.quit()
