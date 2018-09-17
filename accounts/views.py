from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request,'accounts/signup_page.html',{'error':'Username is Taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password = request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'accounts/signup_page.html',{'error':'Password must match'})
    else:
        return render(request, 'accounts/signup_page.html')

def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'], password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/login_page.html',{'error':'UserName or Password is incorrect'})
    else:
        return render(request, 'accounts/login_page.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')