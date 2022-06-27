from django.shortcuts import render

# Create your views here.


def about(request):
    """ A view to return the about page"""

    return render(request, 'about/about.html')


def faqs(request):
    """ A view to return the FAQ's page"""

    return render(request, 'faqs/faqs.html')


def privacy(request):
    """ A view to return the privacy policy page"""

    return render(request, 'privacy/privacy.html')
