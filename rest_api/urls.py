from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.MediaItemList.as_view(), name='mediaitem-list'),
    path('<int:pk>/', views.MediaItemDetail.as_view(), name='mediaitem-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
