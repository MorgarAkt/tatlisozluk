from django.shortcuts import render
from .models import Title, Entry
from account.models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.utils.text import slugify


def home(request):
    titles = Title.objects.all().order_by('-created_date')
    titles_list = []
    for title in titles:
        entry = Entry.objects.filter(title=title).order_by('-likes')[0]
        user = entry.author
        try:
            profile = Profile.objects.get(user=user)
        except:
            profile = None
            
        titles_list.append({'title':title, 'entry':entry, 'profile':profile})

    return render(request, "title/index.html", {'titles_list':titles_list, 'all_titles':titles})


def createNewTitle(request):
    return render(request, "title/createTitle.html")


@login_required
def saveTitle(request):
    if request.method != "POST":
        return redirect("home")

    title_name = request.POST.get("title_name")
    entry_text = request.POST.get("entry_text")

    if slugify(title_name) in Title.objects.all().values_list('slug', flat=True):
        return render(request, "title/createTitle.html", {'error':'Böyle bir başlık bulunuyor.'})

    title = Title(title_name=title_name, author=request.user)
    title.save()
    entry = Entry(title=title, entry_text=entry_text, author=request.user)
    entry.save()
    return redirect(f"/{title.slug}?titleId={title.id}")


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

    if request.user in entry.likers.all():
        entry.likers.remove(request.user)
        entry.likes -= 1
    elif request.user in entry.dislikers.all():
        entry.dislikers.remove(request.user)
        entry.likers.add(request.user)
        entry.likes += 2
    else:
        entry.likers.add(request.user)
        entry.likes += 1
    
    entry.save()
    return redirect(f"/{title.slug}?titleId={title.id}")


@login_required
def dislike(request, title_id, entry_id):
    if request.method != "PUT":
        return title(request, title_id)
    entry = Entry.objects.get(id=entry_id)
    title = Title.objects.get(id=title_id)

    if request.user in entry.dislikers.all():
        entry.dislikers.remove(request.user)
        entry.likes += 1
    elif request.user in entry.likers.all():
        entry.dislikers.add(request.user)
        entry.likers.remove(request.user)
        entry.likes -= 2
    else:
        entry.dislikers.add(request.user)
        entry.likes -= 1
    
    entry.save()
    return title(request, title.slug, title_id)


@login_required
def createEntry(request, title_id):
    if request.method != "POST":
        return redirect("home")
    title = Title.objects.get(id=title_id)
    entry_text = request.POST.get("entry_text")
    entry = Entry(title=title, entry_text=entry_text, author=request.user)
    entry.save()
    return redirect(f"/{title.slug}?titleId={title.id}")


@login_required
def deleteEntry(request, entry_id):
    if request.method != "DELETE":
        return redirect("home")
    
    entry = Entry.objects.get(id=entry_id)
    if request.user != entry.author:
        return redirect("home")
    entries = Entry.objects.filter(title=entry.title)
    if len(entries) == 1:
        entry.title.delete()
        return redirect("/")
    else:
        entry.delete()
    return redirect(f"/{entry.title.slug}?titleId={entry.title.id}")


@login_required
def editEntry(request, entry_id):
    if request.method != "PUT":
        return redirect("home")
    
    entry = Entry.objects.get(id=entry_id)

    if request.user != entry.author:
        return redirect("home")

    entry_text = request.PUT.get("entry_text")
    entry.entry_text = entry_text
    entry.save()
    return redirect(f"/{entry.title.slug}?titleId={entry.title.id}")

def changeEntry(request, title_id, entry_id):
    title = Title.objects.get(id=title_id)

    entries = Entry.objects.filter(title=title).order_by('created_date')
    entries_profiles_list = []
    for entry in entries:
        user = entry.author
        profile = Profile.objects.get(user=user)
        entries_profiles_list.append({'entry':entry, 'profile':profile})
    return render(request, "title/title.html", {'title':title, 'entries_profiles':entries_profiles_list, 'change_entry_id':entry_id})