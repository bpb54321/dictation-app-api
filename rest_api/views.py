from .models import MediaItem, Clip
from .serializers import MediaItemSerializer, ClipSerializer
from rest_framework import generics


class MediaItemList(generics.ListCreateAPIView):
    queryset = MediaItem.objects.all()
    serializer_class = MediaItemSerializer


class MediaItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MediaItem.objects.all()
    serializer_class = MediaItemSerializer


class ClipList(generics.ListCreateAPIView):
    queryset = Clip.objects.all()
    serializer_class = ClipSerializer


class ClipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clip.objects.all()
    serializer_class = ClipSerializer
