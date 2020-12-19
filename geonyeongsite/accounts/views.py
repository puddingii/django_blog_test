from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Account
from .form import AccountLogin, AccountSignup

# Create your views here.
def signup(request):
    sig= AccountSignup()
    if request.method == "POST":
        if request.POST["acc_password"] == request.POST["password_chk"]:
            user = User.objects.create_user(
                username=request.POST["acc_id"],
                password=request.POST["acc_password"]
            )
            auth.login(request, user)
            return redirect('home')
        return render(request, 'accounts/signup.html', {'form':sig})
    return render(request, 'accounts/signup.html', {'form':sig})


def login(request):
    #login action
    if request.method == "POST":
        username = request.POST["acc_id"]
        password = request.POST["acc_password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect'})
    #login page
    else:
        account = AccountLogin()
        return render(request, 'accounts/login.html', {'form':account})


def logout(request):
    auth.logout(request)
    return redirect('home')
