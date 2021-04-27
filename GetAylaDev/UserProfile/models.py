from django.db import models

# Create your models here.



class InstaProfiles(models.Model):
    BusinessName = models.CharField(max_length=200)
    InstagramUserName= models.CharField(max_length=200)
    InstagramPassword= models.CharField(max_length=200)
    City = models.CharField(max_length=200)
    Province= models.CharField(max_length=200)
    PostalCode= models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

