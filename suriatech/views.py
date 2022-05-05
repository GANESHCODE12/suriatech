# Django
import imp
from django.conf import settings
from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages

# Settings
from decouple import config

# Utilities
import smtplib
from email.mime.multipart import MIMEMultipart

# Formularios
# from suriatech.forms import InfoForm


def send_email(name, phone, email, subject, message):
    context = {
        'name': name,
        'phone': phone,
        'email': email,
        'subject': subject,
        'message': message,
    }

    template = get_template('../templates/suriatech/correo.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Solicitud comercial',
        'Tienes una nueva solicitud comercial desde la página web',
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_HOST_USER,]
    )

    email.attach_alternative(content, 'text/html')
    email.send()


def index(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            send_email(name, phone, email, subject, message)
            messages.success(request, "Nos comunicaremos con usted en el menor tiempo posible")
        except Exception as e:
            messages.error(request, e)
    return render(request, '../templates/suriatech/inicio.html', {})
