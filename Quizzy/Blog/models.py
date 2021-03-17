from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from Tests.models import Topic

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    published_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})


# class Comment(models.Model):
#     post = models.ForeignKey('Blog.Post',related_name='comments',on_delete=models.CASCADE)
#     author = models.CharField(max_length=200)
#     text = models.TextField()
#     create_date = models.DateTimeField(default=timezone.now)
#
#     def get_absolute_url(self):
#         return reverse('post_list')
#
#     def __str__(self):
#         return self.text
