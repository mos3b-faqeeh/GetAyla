from django.db import models

# Create your models here.





class InstaProfiles(models.Model):
    InstagramUserNameCustomer= models.CharField(max_length=200)
    BusinessName = models.CharField(max_length=200)
    InstagramPassword= models.CharField(max_length=200)
    City = models.CharField(max_length=200)
    country= models.CharField(max_length=200)
    PostalCode= models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)







class followers(models.Model):
    followerUsername = models.CharField(max_length=200)
    instagramLink= models.CharField(max_length=200)
    relevancyScore= models.CharField(max_length=200)
    location= models.CharField(max_length=200)
    lastActivity= models.CharField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)
    InstagramUserNameCustomer = models.ForeignKey(InstaProfiles,on_delete=models.SET_DEFAULT,default=1)


class targets(models.Model):
    targetUsername = models.CharField(max_length=200)
    instagramLink= models.CharField(max_length=200)
    relevancyScore= models.CharField(max_length=200)
    location= models.CharField(max_length=200)
    lastActivity= models.CharField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)
    InstagramUserNameCustomer = models.ForeignKey(InstaProfiles,on_delete=models.SET_DEFAULT,default=1)





class CustomerInteractionsOnFollowers(models.Model):
    InstagramFollower = models.ForeignKey(followers,on_delete=models.SET_DEFAULT,default=1)
    interactionType=models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    InstagramUserNameCustomer = models.ForeignKey(InstaProfiles,on_delete=models.SET_DEFAULT,default=1)


class CustomerInteractionsOnTarget(models.Model):
    InstagramTarget = models.ForeignKey(targets,on_delete=models.SET_DEFAULT,default=1)
    interactionType=models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    InstagramUserNameCustomer = models.ForeignKey(InstaProfiles,on_delete=models.SET_DEFAULT,default=1)












