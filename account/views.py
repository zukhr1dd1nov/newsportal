from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _

from account.forms import LoginForm, RegistrationForm

# Create your views here.

def account_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request,**form.cleaned_data)
            if user is not None:
                login(request,user)
                messages.success(request, _(f"{user.get_full_name()} xush kelibsiz!"))

                return redirect("main_index")

                
        form.add_error("password", _("Login va/yoki parol noto'g'ri"))

    return render(request, "account/login.html",{
        'form' : form
    })

def account_registration(request):
    form = RegistrationForm()

    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.instance.set_password(form.cleaned_data.get('password'))
            form.save()
            messages.success(request, _("Siz mufavaqqiyatli ro'yhatdan o'tdingiz!!!"))
            return redirect('main_index')
    
    return render(request, "account/registration.html",{'form':form})

def account_logout(request):
    messages.success(request, _(f'Kelib turing , {request.user.get_full_name()}!!!'))
    logout(request)

    return redirect('main_index')
