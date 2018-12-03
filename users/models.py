from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='profile_pics/default.jpeg', upload_to='profile_pics')

    def __str__(self):
        return self.user.username

    def save(self):
        super().save()
        img = Image.open(self.profile_pic.path)
        if img.height > 300 or img.width > 300:
            outputsize = (300, 300)
            img.thumbnail(outputsize)
            img.save(self.profile_pic.path)
