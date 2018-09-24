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
    resource_url = models.URLField(default='', blank=True)
    youtube_id = models.CharField(max_length=200, default='', blank=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Clip(models.Model):
    transcription = models.TextField(default='')
    translation = models.TextField(default='')
    start_hours = models.IntegerField(default=0)
    start_minutes = models.IntegerField(default=0)
    start_seconds = models.IntegerField(default=0)
    end_hours = models.IntegerField(default=0)
    end_minutes = models.IntegerField(default=0)
    end_seconds = models.IntegerField(default=0)
    media_item = models.ForeignKey(
        MediaItem, related_name='clips', on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.start_time} - {self.end_time}'
