from django.shortcuts import render
from .models import Title, Entry


# Create your views here.

def home(request):
    titles = Title.objects.all()
    entries = Entry.objects.all()

    return render(request, "title/index.html", {"titles": titles, "entries": entries})
