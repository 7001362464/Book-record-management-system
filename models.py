from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class boi(models.Model):
    title=models.CharField(max_length=100)
    price=models.FloatField();
    author=models.CharField(max_length=100);
    publisher=models.CharField(max_length=100);
    pdf=models.FileField(upload_to='documents/%Y/%m/%d')

