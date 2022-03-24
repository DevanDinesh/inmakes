from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

class People(models.Model):
    img=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=200)
    desc=models.TextField()

    def __str__(self):
        return self.name