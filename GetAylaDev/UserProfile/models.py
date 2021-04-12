from django.db import models

# Create your models here.



class Profiles(models.Model):
    profileInsta = models.CharField(max_length=200)
    InstaDesk = models.CharField(max_length=200)
