from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        Username=request.POST['username']
        Password=request.POST['password']
        user=auth.authenticate(username=Username,password=Password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid")
            return redirect('login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')



def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        Email=request.POST['email']
        Password=request.POST['password']
        ConfirmPassword=request.POST['password1']
        if Password==ConfirmPassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exist")
                return redirect('register')
            elif User.objects.filter(email=Email).exists():
                messages.info(request,"Email already exist")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=Email,password=Password)
                user.save();
                return redirect('login')
                # messages.info(request,"User Created")
                # print("User created")
        else:
            messages.info(request,"Password Not Matched")
            return redirect('register')
        return redirect('/')
            # print("Password Not Matched")
    return render(request,'register.html')