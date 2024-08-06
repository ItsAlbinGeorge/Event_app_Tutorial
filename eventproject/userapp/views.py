from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already taken")
                return redirect('/register')
            else:
                messages.info(request,"Successfully registered")
                user_reg=User.objects.create_user(username=username,email=email,password=password)
                user_reg.save()
                return redirect('/')
        else:
            messages.info(request,"Password doesnt match")
            return redirect('/register')
    return render(request,'reg.html')


def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=auth.authenticate(email=email,password=password)
        if user is not None:
            messages.info(request,"Login Successfull")
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Register")
            return redirect('/register')
    return render(request,'log.html')

def logout(request):
    auth.logout(request)
    return redirect('/')