# Generated by Django 4.2.1 on 2023-05-15 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('title', '0004_alter_entry_entry_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='most_like',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='entry',
            name='entry_text',
            field=models.TextField(max_length=8000),
        ),
    ]
