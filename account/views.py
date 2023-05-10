
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profile
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage

# Create your views here.
def login(request):
    return render(request, "account/login.html")

def register(request):
    if request.method == "POST":
        form_data = request.POST
        name = form_data.get('name')
        surname = form_data.get('surname')
        username = form_data.get("username")
        email = form_data.get("email")
        password = form_data.get("password")
        passwordConfirmation = form_data.get("repassword")
        image = request.FILES.get('image')
        fs = FileSystemStorage(location='uploads/profile_pics')
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)

        if password == passwordConfirmation:
            if User.objects.filter(username=username).exists():
                return render(request, "account/register.html", {
                    "error": "Kullanıcı adı kullanılıyor",
                    "name": name,
                    "surname": surname,
                    "email": email,
                    "password":password,
                    "repassword":password,    
                })
            elif User.objects.filter(email=email).exists():
                return render(request, "account/register.html", {
                    "error": "Email Kullanılıyor",
                    "name": name,
                    "surname": surname,
                    "username": username,
                    "password":password,
                    "repassword":password   
                    })
            else:
                user = User.objects.create_user(first_name = name, last_name = surname, username=username,
                                    email=email, password=password)
                user.save()
                profile = Profile(user = user, image = "/profile_pics/"+image.name)
                profile.save()
                return redirect("home")

    return render(request, "account/register.html")