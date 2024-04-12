
from django.conf import settings
from django.core.mail import send_mail,EmailMessage

def sendemailto():
    subject = 'Test Email'
    message = f'Hi TEST, thank you for Testing.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['jatinsatani1995@gmail.com', 'jatinsatani7@gmail.com','jatinsatani2023@gmail.com']
    send_mail( subject, message, email_from, recipient_list )
    
    
def mail_with_file(filepath):
    subject = 'Test Email'
    message = f'Hi TEST, thank you for Testing with File.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list =  ['jatinsatani1995@gmail.com', 'jatinsatani7@gmail.com','jatinsatani2023@gmail.com']
    user = EmailMessage(subject=subject,body=message,from_email=email_from,to=recipient_list)
    user.attach_file(filepath)
    user.send()