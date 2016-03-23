import smtplib

fromname='jill'
toname='lamb'
subject='test'
fromaddr = 'jillianjohnson9957@gmail.com'
msg='hi'
toaddr  = 'coding.testing.email@gmil.com'
toaddrs  = 'coding.testing.email@gmil.com'
message = """From: {} <{}>

To: {} <{}>

Subject: {}

{}"""

messagetosend = message.format(

                             fromname,

                             fromaddr,

                             toname,

                             toaddr,

                             subject,

                             msg)

# Credentials (if needed)

username = 'coding.testing.email@gmil.com'

password = 'Test-ing'

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()

server.login(username,password)

server.sendmail(fromaddr, toaddrs, messagetosend)

server.quit()