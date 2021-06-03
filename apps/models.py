from django.db import models
from django.contrib.auth.models import User 


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=50, null=True)
    website = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.full_name

class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='', blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Body(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='', blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50] + "..."
