from django.db import models
from account.models import User
from django.utils.text import slugify

# Create your models here.

class Title(models.Model):
    title_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    most_like = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_name)
        super(Title, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/{self.slug}?titleId={self.id}"

    def __str__(self):
        return self.title_name
    

class Entry(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    entry_text = models.TextField(max_length=8000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    likers = models.ManyToManyField(User, related_name="likers", blank=True)
    dislikers = models.ManyToManyField(User, related_name="dislikers", blank=True)

    def __str__(self):
        return self.author.username + "- " + self.title.title_name
    
    def get_absolute_title_url(self):
        return f"/{self.title.slug}?titleId={self.title.id}"
    
    def is_liked_by_user(self, user):
        return user in self.likers.all()
    
    def is_disliked_by_user(self, user):
        return user in self.dislikers.all()