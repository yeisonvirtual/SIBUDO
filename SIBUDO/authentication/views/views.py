
from django.shortcuts import render

def not_fount(request):
    return render(request, "authentication/error/not_fount.html")