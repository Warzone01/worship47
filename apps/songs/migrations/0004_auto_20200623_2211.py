# Generated by Django 2.2.13 on 2020-06-23 19:11

import songs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_auto_20200622_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='chordKey1',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('C#', 'C#'), ('D', 'D'), ('D#', 'D#'), ('E', 'E'), ('F', 'F'), ('F#', 'F#'), ('G', 'G'), ('G#', 'G#'), ('A', 'A'), ('A#', 'A#'), ('B', 'B')], default='E', max_length=2),
        ),
        migrations.AlterField(
            model_name='song',
            name='chordKey2',
            field=models.CharField(blank=True, choices=[('C', 'C'), ('C#', 'C#'), ('D', 'D'), ('D#', 'D#'), ('E', 'E'), ('F', 'F'), ('F#', 'F#'), ('G', 'G'), ('G#', 'G#'), ('A', 'A'), ('A#', 'A#'), ('B', 'B')], default='E', max_length=2),
        ),
        migrations.AlterField(
            model_name='song',
            name='chordsFile1',
            field=models.FileField(blank=True, upload_to=songs.models.chords_path),
        ),
        migrations.AlterField(
            model_name='song',
            name='chordsFile2',
            field=models.FileField(blank=True, upload_to=songs.models.chords_path),
        ),
        migrations.AlterField(
            model_name='song',
            name='presentation',
            field=models.FileField(blank=True, upload_to=songs.models.pres_path),
        ),
        migrations.AlterField(
            model_name='song',
            name='text_file',
            field=models.FileField(blank=True, upload_to=songs.models.text_path),
        ),
    ]
