from django.contrib import admin

# Register your models here.
from .models import Song

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'bpm', 'key', 'uploaded_at')
    search_fields = ('title', 'owner__username')