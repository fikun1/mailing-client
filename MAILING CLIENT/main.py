import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart



server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('testinprojects7@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'testinprojects7@gmail.com'
msg['To'] = 'davidoladejo200@gmail.com'
msg['Subject'] = 'Test Email'



