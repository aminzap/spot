from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=15)
    family = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    def __str__(self):
        return self.username


class Spot(models.Model):
    name=models.CharField(max_length=15,default=' ')
    image = models.ImageField(upload_to='media')
    descript=models.TextField(blank=True, null=True)
    rate = models.IntegerField()
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    comment = models.TextField( blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True,on_delete=models.PROTECT)
    def __str__(self):
        return self.name
