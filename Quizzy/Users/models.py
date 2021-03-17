from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image
# Create your models here.
User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    # uploads image to Profile_Pictures dir inside project directory
    image = models.ImageField(default='default.jpg', upload_to = 'Profile_Pictures')

    def __str__(self):
        return self.user.username

    # To resize the Image
    # def save(self):
    #     super().save()
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
