import smtplib

fromname = 'ennadroj'
fromaddr = 'jord.vanessa@gmail.com'
toname = 'Jordanne'
toaddr = 'sweetjordie@hotmail.com'
subject = 'hailings from zion'
msg = 'Jah bless'
message = """From: {} <{}>
To: {} <{}>
Subject: {}

{}
"""
messagetosend = message.format(
                            fromname,
                            fromaddr,
                            toname,
                            toaddr,
                            subject,
                            msg)

# Credentials (if needed)
username = 'jord.vanessa@gmail.com'
password = 'qcciwbpgniyummve'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddr, messagetosend)
server.quit()