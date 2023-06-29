from django.shortcuts import render

# Create your views here.

def index(request):
    user_name = request.user.username
    return render(request, "SIBUDO_app/index.html", {'nombre': user_name})