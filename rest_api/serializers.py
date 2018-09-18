from rest_framework import serializers
from .models import MediaItem, Clip


class ClipSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Clip
        fields = (
            'url', 'id', 'transcription', 'translation', 'start_time',
            'end_time'
        )


class MediaItemSerializer(serializers.HyperlinkedModelSerializer):
    clips = ClipSerializer(many=True)

    class Meta:
        model = MediaItem
        fields = (
            'url', 'id', 'title', 'type', 'resource_url', 'youtube_id',
            'clips',
        )

    def create(self, validated_data):
        clips_data = validated_data.pop('clips')
        media_item = MediaItem.objects.create(**validated_data)
        for clip_data in clips_data:
            Clip.objects.create(media_item=media_item, **clip_data)
        return clip
