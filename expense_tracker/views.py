from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from users.models import User
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate, login 
from django.db import IntegrityError, OperationalError
from django.contrib import messages

# Create your views here.



@never_cache
def login(request):
    error_message = None
    if request.POST:
        mail = request.POST['email']
        pas = request.POST['password']

        try:
            user = User.objects.get(email=mail)
            if check_password(pas, user.password):
                request.session["user_id"] = user.user_id
                request.session["user_name"] = user.first_name
                return redirect('/dashboard/',user)
            else:
                error_message = "Invalid Credentials"
        except User.DoesNotExist:
            error_message = "Invalid Credentials"

    return render(request,'login.html',{'error_message' : error_message})

@never_cache
def dash(request):
    user_name = request.session.get("user_name")
    if not user_name:
        return redirect("/login/")  
    return render(request, "dashboard.html", {"user_name": user_name})



def reg(request):
    if request.POST:
        first = request.POST.get('first_name')
        last = request.POST.get('last_name')
        mail = request.POST.get('email')
        pas = request.POST.get('password')
        cur = request.POST.get('currency')

        hashed_password = make_password(pas)

        try:
            u = User(
                first_name=first,
                last_name=last,
                email=mail,
                password=hashed_password,
                currency=cur
            )
            u.save()
            messages.success(request, "User registered successfully.")
            return redirect('/login/')

        except OperationalError as e:
            if 'User with this email already exists' in str(e):
                messages.error(request, "A user with this email already exists.")
            else:
                messages.error(request, "An unexpected database error occurred.")

        except IntegrityError:
            messages.error(request, "Duplicate email. Please use a different one.")

    return render(request, 'registration.html')

def logout(request):
    request.session.flush()  
    return redirect("/login/")



