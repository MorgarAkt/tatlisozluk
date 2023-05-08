from django.shortcuts import render
from .models import Title, Entry
from account.models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def home(request):
    titles = Title.objects.all()
    titles_list = []
    for title in titles:
        entry = Entry.objects.filter(title=title).order_by('-likes')[0]
        user = entry.author
        profile = Profile.objects.get(user=user)
        titles_list.append({'title':title, 'entry':entry, 'profile':profile})
    return render(request, "title/index.html", {'titles_list':titles_list})


def createNewTitle(request, slug=None):
    if slug:
        slug = slug.split('-')
        slug = ' '.join(slug)
    if slug == "createTitle":
        slug = ""
    return render(request, "title/createTitle.html", {'slug':slug})


@login_required
def saveTitle(request):
    if request.method != "POST":
        return redirect("home")
    
    title_name = request.POST.get("title_name")
    entry_text = request.POST.get("entry_text")
    title = Title(title_name=title_name, author=request.user)
    title.save()
    entry = Entry(title=title, entry_text=entry_text, author=request.user)
    entry.save()
    return redirect(f"/{title.slug}?titleId={title.id}")


def title(request, slug):
    title_id = request.GET.get('titleId')
    if title_id is None:
        return createNewTitle(request, slug)

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
        return title(request, title.slug, title_id)
    
    entry.likers.add(request.user)
    entry.likes += 1
    entry.save()
    return title(request, title.slug, title_id)


@login_required
def dislike(request, title_id, entry_id):
    if request.method != "PUT":
        return title(request, title_id)
    entry = Entry.objects.get(id=entry_id)
    title = Title.objects.get(id=title_id)

    if request.user not in entry.likers.all():
        return title(request, title.slug, title_id)
    
    entry.likes -= 1
    entry.save()
    return title(request, title.slug, title_id)