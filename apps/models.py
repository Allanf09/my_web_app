from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='', blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Body(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='', blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50] + "..."
