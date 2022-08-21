from django.shortcuts import render


def handler404(request, exception):
    """View to return 404 error page if page does not exists"""
    return render(request, "errors/404.html", status=404)
