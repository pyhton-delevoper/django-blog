from django.db import models

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField(default='super text')
    timestamp = models.DateTimeField(auto_now_add=True)
