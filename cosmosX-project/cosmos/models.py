from django.db import models
from datetime import date


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='cosmos/static/images')
    url = models.URLField(blank=True)
    date = models.DateField(default=date.today)
