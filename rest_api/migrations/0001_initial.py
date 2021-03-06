# Generated by Django 2.1.1 on 2018-09-13 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transcription', models.TextField(default='')),
                ('translation', models.TextField(default='')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='MediaItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(choices=[('youtube', 'Youtube Video'), ('audio', 'Audio')])),
                ('url', models.URLField()),
                ('youtube_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='clip',
            name='media_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.MediaItem'),
        ),
    ]
