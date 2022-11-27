from django.db import models
# Create your models here.


class Information(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    img = models.ImageField(default=None)
    gender = models.CharField(max_length=20, default=None)
    hobby = models.CharField(max_length=50, default=None)
    country = models.CharField(max_length=50, default=None)
