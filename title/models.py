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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_name)
        super(Title, self).save(*args, **kwargs)

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
    