# Generated by Django 3.2.9 on 2021-12-13 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0002_auto_20211211_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]