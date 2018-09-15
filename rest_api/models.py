from django.db import models


class MediaItem(models.Model):
    title = models.CharField(max_length=200, default='')
    type = models.TextField(
        choices=(
            ('youtube', 'Youtube Video'),
            ('audio', 'Audio'),
        ),
        default='youtube'
    )
    url = models.URLField(default='', blank=True)
    youtube_id = models.CharField(max_length=200, default='', blank=True)

    def __str__(self):
        return self.title


class Clip(models.Model):
    transcription = models.TextField(default='')
    translation = models.TextField(default='')
    start_time = models.CharField(max_length=5, default='00:00')
    end_time = models.CharField(max_length=5, default='00:00')
    media_item = models.ForeignKey(MediaItem, on_delete=models.CASCADE)

    def __str__(self):
        return f'{start_time} - {end_time}'
