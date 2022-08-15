from django.shortcuts import render


def index(request):
    """ A view to return the index page"""

    return render(request, 'home/index.html')


def handle_404(request, exception):
    """View to return 404 error page if page does not exists"""
    return render(request, 'errors/404.html')
