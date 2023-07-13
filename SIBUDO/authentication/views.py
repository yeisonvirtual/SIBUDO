from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

#from django.http import HttpResponse

class register_user(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "authentication/register.html",{"form":form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('/')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "authentication/register.html",{"form":form})
        
def sign_off(request):
    logout(request)
    return redirect('/')

def sing_in(request):
    if request.method=="POST": 
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            name_user = form.cleaned_data.get("username")
            password_user = form.cleaned_data.get("password")
            user=authenticate(username = name_user, password=password_user)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Verifique los datos y vuelva a intentar")
        else:
            messages.error(request, "Verifique los datos y vuelva a intentar")

    form = AuthenticationForm()
    context = {
        'form': form,
        # 'messages': messages.get_messages(request),
    }
    return render(request, "authentication/login/login.html", context)
        