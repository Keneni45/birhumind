
from django.core.mail import send_mail
from django.conf import settings

def send_subscription_email(email):
    subject = 'Subscription Confirmed'
    message = 'Thank you for subscribing to our newsletter!'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    
    send_mail(subject, message, from_email, recipient_list)
