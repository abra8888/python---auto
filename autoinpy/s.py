from email.message import EmailMessage
import ssl
import smtplib


email_sender = 'example @gmail.com'
email_password = '123456'

email_receiver = ''#from tempemail.com get one 

subject = "hello to all "

body = """
 this message is true 

"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver, em.as_string())