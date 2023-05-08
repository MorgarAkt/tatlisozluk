from django.shortcuts import render
from .models import Title, Entry
from account.models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse


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


def title(request, slug):
    title_id = request.GET.get('titleId')
    title = Title.objects.get(id=title_id)
    print(title)
    if slug != title.slug:
        print("Slug is not equal to title slug")
        return redirect(f"/{title.slug}?titleId={title_id}")
    
    entries = Entry.objects.filter(title=title).order_by('created_date')
    entries_profiles_list = []
    for entry in entries:
        user = entry.author
        profile = Profile.objects.get(user=user)
        entries_profiles_list.append({'entry':entry, 'profile':profile})
    return render(request, "title/title.html", {'title':title, 'entries_profiles':entries_profiles_list})

@login_required
def like(request, title_id, entry_id):
    if request.method != "PUT":
        return title(request, title_id)
    entry = Entry.objects.get(id=entry_id)
    title = Title.objects.get(id=title_id)
    entry.likes += 1
    entry.save()
    return title(request, title.slug, title_id)


def dislike(request, title_id, entry_id):
    if request.method != "PUT":
        return title(request, title_id)
    entry = Entry.objects.get(id=entry_id)
    title = Title.objects.get(id=title_id)
    entry.likes -= 1
    entry.save()
    return title(request, title.slug, title_id)