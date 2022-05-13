from django.db import models

# Create your models here.

class Travelplace(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    description=models.TextField()

    def __str__(self):
        return self.name


class Travelteam(models.Model):
    tname=models.CharField(max_length=250)
    timage=models.ImageField(upload_to='pics')
    tdesc=models.TextField()


    def __str__(self):
        return self.tname