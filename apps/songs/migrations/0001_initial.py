# Generated by Django 3.2.16 on 2022-12-13 13:29

import ckeditor.fields
import django.db.models.deletion
import songs.models
import versatileimagefield.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('slug', models.CharField(default='', max_length=10)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='categs/')),
                ('priority', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('title_eng', models.CharField(blank=True, max_length=255)),
                ('text', ckeditor.fields.RichTextField(blank=True)),
                ('text_eng', ckeditor.fields.RichTextField(blank=True)),
                ('chords', ckeditor.fields.RichTextField(blank=True)),
                ('presentation', models.FileField(blank=True, upload_to=songs.models.pres_path)),
                ('text_file', models.FileField(blank=True, upload_to=songs.models.text_path)),
                ('author', models.CharField(blank=True, default='', max_length=100)),
                ('is_translated', models.BooleanField(blank=True, default=True)),
                ('main_key', models.CharField(blank=True, choices=[('C', 'C'), ('C#', 'C#'), ('D', 'D'), ('D#', 'D#'), ('E', 'E'), ('F', 'F'), ('F#', 'F#'), ('G', 'G'), ('G#', 'G#'), ('A', 'A'), ('A#', 'A#'), ('B', 'B')], default='E', max_length=2)),
                ('difficult', models.CharField(blank=True, choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], default='easy', max_length=6)),
                ('chordsFile1', models.FileField(blank=True, upload_to=songs.models.chords_path)),
                ('chordKey1', models.CharField(blank=True, choices=[('C', 'C'), ('C#', 'C#'), ('D', 'D'), ('D#', 'D#'), ('E', 'E'), ('F', 'F'), ('F#', 'F#'), ('G', 'G'), ('G#', 'G#'), ('A', 'A'), ('A#', 'A#'), ('B', 'B')], default='E', max_length=2)),
                ('chordsFile2', models.FileField(blank=True, upload_to=songs.models.chords_path)),
                ('chordKey2', models.CharField(blank=True, choices=[('C', 'C'), ('C#', 'C#'), ('D', 'D'), ('D#', 'D#'), ('E', 'E'), ('F', 'F'), ('F#', 'F#'), ('G', 'G'), ('G#', 'G#'), ('A', 'A'), ('A#', 'A#'), ('B', 'B')], default='E', max_length=2)),
                ('ytb_id1', models.CharField(blank=True, max_length=100)),
                ('ytb_id2', models.CharField(blank=True, max_length=100)),
                ('ytb_id3', models.CharField(blank=True, max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(blank=True, to='songs.Category')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
