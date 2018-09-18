from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('media-items/', views.MediaItemList.as_view(), name='mediaitem-list'),
    path(
        'media-items/<int:pk>/', views.MediaItemDetail.as_view(),
        name='mediaitem-detail'
    ),
    path('clips/', views.ClipList.as_view(), name='clip-list'),
    path('clips/<int:pk>/', views.ClipDetail.as_view(), name='clip-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
