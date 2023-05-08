# Generated by Django 4.2.1 on 2023-05-08 13:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('title', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='likes',
        ),
        migrations.AddField(
            model_name='entry',
            name='likers',
            field=models.ManyToManyField(blank=True, related_name='likers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='title',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
    ]