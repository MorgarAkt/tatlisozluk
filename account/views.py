from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from title.models import Entry
from .models import Profile
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage

# Create your views here.


def logout_request(request):
    logout(request)
    return redirect("home")


def login_request(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        print(request.POST)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "account/login.html", {"error": "Kullanıcı Bulunamadı"})

    return render(request, "account/login.html")


def register_request(request):
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
                    "error": "Kullanıcı Adı Kullanılıyor",
                    "name": name,
                    "surname": surname,
                    "username": username,
                    "email": email,
                    "password": password,
                    "repassword": password,
                })
            elif User.objects.filter(email=email).exists():
                return render(request, "account/register.html", {
                    "error": "Email Kullanılıyor",
                    "name": name,
                    "surname": surname,
                    "username": username,
                    "email": email,
                    "password": password,
                    "repassword": password
                })
            else:
                user = User.objects.create_user(
                    first_name=name, last_name=surname, username=username, email=email, password=password)
                user.save()
                profile = Profile(user=user, image="/profile_pics/"+image.name)
                profile.save()
                return redirect("home")
        else:
            return render(request, "account/register.html", {
                "error": "Şifreler Eşleşmiyor",
                "name": name,
                "surname": surname,
                "username": username,
                "email": email,
            })

    return render(request, "account/register.html")


def user_details(request, username):
    try:
        total_likes = 0
        # Retrieve the user based on the provided username
        user = User.objects.get(username=username)

        entry_list = Entry.objects.filter(author=user)
        for entry in entry_list:
            total_likes += entry.likes

        # Create a context dictionary with the user's information
        context = {
            'user': user,
            'total_likes': total_likes
        }

        # Render the page template and pass the context dictionary
        return render(request, "account/user_details.html", context)

    except User.DoesNotExist:
        # Handle the case when the user does not exist
        # You can redirect to an error page or return an appropriate response
        return render(request, 'user_not_found.html')
