import smtplib
from email import encoders

server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('testinprojects7@gmail.com', password)

