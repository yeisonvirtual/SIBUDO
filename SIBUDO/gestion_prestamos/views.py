from django.shortcuts import render

# Create your views here.
def gestion_prestamos(request):
    return render(request, "gestion_prestamos/gestion_prestamos.html", {})