# file_share/models.py
from django.db import models

class UserProfile(models.Model):
    token = models.CharField(max_length=10, unique=True)
    shared_files = models.ManyToManyField('self', symmetrical=False, blank=True)

class File(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/')
