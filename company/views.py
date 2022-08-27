from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail


def about(request):
    """ A view to return the about page"""

    return render(request, 'about/about.html')


def faqs(request):
    """ A view to return the FAQ's page"""

    return render(request, 'faqs/faqs.html')


def privacy(request):
    """ A view to return the privacy policy page"""

    return render(request, 'privacy/privacy.html')


def contact(request):
    """ A view to return the contact page"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        message_data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }
        message = '''
        From: {}
        New message: {}
        '''.format(message_data['email'], message_data['message'])

        send_mail(
            message_data['subject'], message, '', ['smith.liam1994@gmail.com'])

        messages.info(request, (
            f'Your message has been sent, we will contact you \
                via { email } as soon as possible.'))
        return render(request, 'home/index.html')

    return render(request, 'contact/contact.html')
