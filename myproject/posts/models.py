from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True) #dateTime stamp will be added every time a user enters a post
    banner = models.ImageField(default='profile_picture.jpg', blank=True)
    
    #create method that will return the post title
    
    def __str__(self):
        return self.title
    