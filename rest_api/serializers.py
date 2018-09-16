from rest_framework import serializers
from .models import MediaItem, Clip


class MediaItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MediaItem
        fields = ('title', 'type', 'url', 'youtube_id')
