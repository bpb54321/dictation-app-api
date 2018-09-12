from django.db import models


class Clip(models.Model):
    transcription = models.TextField(default='')
    translation = models.TextField(default='')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

# TO-DO: Create MediaItem model
# Type:
# URL:
# Youtube ID:
# Clips
