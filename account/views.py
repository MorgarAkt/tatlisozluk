from django.shortcuts import render, redirect
from blog.models import Blog, Category, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
from .forms import ProfileForm

# Create your views here.


def login_request(request):
    if request.user.is_authenticated:
        return redirect("home")
        
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "account/login.html", {"error": "Kullanıcı Bulunamadı"})

    return render(request, "account/login.html")


def register_request(request):
    form = ProfileForm(request.POST, request.FILES)
    
    if request.user.is_authenticated:
        return redirect("home")


    if request.method == "POST" :

        form.is_valid()
        username = form.cleaned_data["username"]
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        repassword = form.cleaned_data["repassword"]
        image = request.FILES["image"]

        print(request.FILES)

        fs = FileSystemStorage(location='uploads/profile_pics')
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, "account/register.html", {
                    "error": "Kullanıcı adı kullanılıyor",
                    "username": username,
                    "password":password,
                    "repassword":password                    
                })
            elif User.objects.filter(email=email).exists():
                return render(request, "account/register.html", {
                    "error": "Email Kullanılıyor",
                    "username": username,
                    "password":password,
                    "repassword":password   
                    })
            else:
                user = User.objects.create_user(username=username,
                                    email=email, password=password)
                user.save()
                profile = Profile(user = user, image = "/profile_pics/"+image.name)
                profile.save()
                return redirect("home")
            return redirect("home")
        else:
            return render(request, "account/register.html", {
                    "error": "Şifre tekrarı yanlış",
                    "username": form.cleaned_data["username"]})
    return render(request, "account/register.html", {"form":form})


def logout_request(request):
    logout(request)
    return redirect("home")
