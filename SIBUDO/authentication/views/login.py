from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
        
def sign_off(request):
    logout(request)
    return redirect('/')

def sing_in(request):
    if request.method=="POST" : 
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
        