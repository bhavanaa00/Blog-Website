from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((0, "Draft"),(1,"Published"))

class Post(models.Model):
  title = models.CharField(max_length=200,unique=True)
  slug = models.SlugField(max_length=200,unique=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_post")
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now_add=True)
  content = models.TextField()
  status = models.IntegerField(choices=STATUS, default=0)

  class Meta:
    ordering = ['-created_on']

  def __str__(self):
    return self.title

class Contact(models.Model):
  fullname = models.CharField(max_length=100)
  phone = models.CharField(max_length=10)
  message = models.TextField()

  def __str__(self):
    return self.fullname
  
class Newsletter(models.Model):
    email = models.EmailField(unique=False)
    
    def __str__(self):
      return self.email