from .models import MediaItem
from .serializers import MediaItemSerializer
from rest_framework import generics


class MediaItemList(generics.ListCreateAPIView):
    queryset = MediaItem.objects.all()
    serializer_class = MediaItemSerializer


class MediaItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MediaItem.objects.all()
    serializer_class = MediaItemSerializer
