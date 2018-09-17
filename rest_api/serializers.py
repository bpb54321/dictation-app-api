from rest_framework import serializers
from .models import MediaItem, Clip


class MediaItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MediaItem
        fields = ('url', 'id', 'title', 'type', 'resource_url', 'youtube_id')
