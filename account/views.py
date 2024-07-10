from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth
from .models import CUser
from django.contrib.auth.decorators import login_required

@login_required
def user_profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

def signin(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['email'], password=request.POST['password']) 
        print(user)
        if user is not None :
            auth.login(request, user)
            return redirect('/account/profile')
        else :
            return HttpResponse('Error')
    else:
        return render(request, 'account/signin.html')

def signup(request):
    if request.method == "POST":
        phone = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        user = auth.authenticate(phone=phone, password=password) 
        if user is not None :
            auth.login(request, user)
            return redirect('/')
        else :
            # Check if the user already exists
            if CUser.objects.filter(phone=phone).exists():
                return HttpResponse("This phone number has already been used to sign up!")
            else:
                # Create the new user
                user = CUser.objects.create_user(
                    fullname=name,
                    phone=phone,
                    password=(password),  # Hash the password
                )
                user.save()
                auth.login(request, user)
                return redirect('/')
                

              


    else :
        return render(request, 'account/signup.html')
    
def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('/')
    else :
        return redirect('/account/profile')