# Generated by Django 3.2.5 on 2021-09-25 18:24
from django.contrib.postgres.operations import TrigramExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0005_song_user'),
    ]

    operations = [
        TrigramExtension(),
    ]
