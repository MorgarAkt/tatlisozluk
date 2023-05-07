from django.shortcuts import render
from .models import Title, Entry
from account.models import Profile


# Create your views here.

def home(request):
    titles = Title.objects.all()
    titles_list = []
    for title in titles:
        entry = Entry.objects.filter(title=title).order_by('-likes')[0]
        user = entry.author
        profile = Profile.objects.get(user=user)
        titles_list.append({'title':title, 'entry':entry, 'profile':profile})
    return render(request, "title/index.html", {'titles_list':titles_list})


def title(request, title_id):
    title = Title.objects.get(id=title_id)
    entries = Entry.objects.filter(title=title).order_by('created_date')
    entries_profiles_list = []
    for entry in entries:
        user = entry.author
        profile = Profile.objects.get(user=user)
        entries_profiles_list.append({'entry':entry, 'profile':profile})
    print(entries_profiles_list)
    return render(request, "title/title.html", {'title':title, 'entries_profiles':entries_profiles_list})
