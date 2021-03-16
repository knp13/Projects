from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics',editable=True,help_text="Profile Picture")
    image_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="100")
    image_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="100")

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        image = Image.open(self.image.path)

        (width, height) = image.size
        size = ( 100, 100)
        image = image.resize(size, Image.ANTIALIAS)
        image.thumbnail(size)
        image.save(self.image.path)
