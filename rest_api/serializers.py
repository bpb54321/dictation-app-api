from rest_framework import serializers
from .models import MediaItem, Clip


class ClipSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Clip
        fields = (
            'url', 'id', 'transcription', 'translation',
            'start_hours', 'start_minutes', 'start_seconds',
            'end_hours', 'end_minutes', 'end_seconds',
            'media_item'
        )


class MediaItemSerializer(serializers.HyperlinkedModelSerializer):
    clips = ClipSerializer(many=True)

    class Meta:
        model = MediaItem
        fields = (
            'url', 'id', 'title', 'type', 'resource_url', 'youtube_id',
            'clips',
        )
