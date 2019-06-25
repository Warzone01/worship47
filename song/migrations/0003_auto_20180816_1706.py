# Generated by Django 2.0.6 on 2018-08-16 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0002_auto_20180816_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='song',
            name='urls',
        ),
        migrations.AddField(
            model_name='link',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='song.Song'),
        ),
    ]