from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings  # for referencing the user model

class Song(models.Model):
    title = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='songs/')
    bpm = models.FloatField(null=True, blank=True)
    key = models.CharField(max_length=50, null=True, blank=True)
    
    # The user who created/uploaded this song
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='songs'
    )
    
    # Collaborators: other users who can view/edit/participate
    collaborators = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='collaborations',
        blank=True
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.owner.username}"