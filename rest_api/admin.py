from django.contrib import admin
from .models import MediaItem, Clip


class ClipInline(admin.StackedInline):
    model = Clip
    extra = 3


class MediaItemAdmin(admin.ModelAdmin):
    inlines = [ClipInline]

admin.site.register(MediaItem, MediaItemAdmin)
