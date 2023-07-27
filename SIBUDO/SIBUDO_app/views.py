from django.shortcuts import render

def index(request):
    user_name = request.user.username
    return render(request, "SIBUDO_app/index.html", {'nombre': user_name})

def error_404(request, exception):
    return render(request, 'authentication/error/not_fount.html')
