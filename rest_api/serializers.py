from rest_framework import serializers
from .models import MediaItem, Clip


class ClipSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Clip
        fields = (
            'url', 'id', 'transcription', 'translation', 'start_time',
            'end_time', 'media_item'
        )


class MediaItemSerializer(serializers.HyperlinkedModelSerializer):
    clips = ClipSerializer(many=True)

    class Meta:
        model = MediaItem
        fields = (
            'url', 'id', 'title', 'type', 'resource_url', 'youtube_id',
            'clips',
        )
