from django.db import models


class MediaItem(models.Model):
    type = models.TextField(
        choices=(
            ('youtube', 'Youtube Video'),
            ('audio', 'Audio'),
        )
    )
    url = models.URLField()
    youtube_id = models.CharField(max_length=200)


class Clip(models.Model):
    transcription = models.TextField(default='')
    translation = models.TextField(default='')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    media_item = models.ForeignKey(MediaItem, on_delete=models.CASCADE)
