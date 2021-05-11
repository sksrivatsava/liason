from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from flask import request



class CustomUser(models.Model):
    userid      = models.CharField(max_length=50,default='')
    username    = models.CharField(max_length=50,default='')
    department  = models.CharField(max_length=50,default='')
    designation = models.CharField(max_length=50,default='')
    foll        = models.CharField(max_length=5000,default='')
    followers   = models.CharField(max_length=5000,default='')
    acctype     = models.CharField(max_length=10,default='Public')
    foll_req    = models.CharField(max_length=5000,default='')
    display_picture = models.ImageField(upload_to='display_pictures/',height_field=None,width_field=None,max_length=None,blank=True,default='display_pictures/default_nice.jpg')
    
    REQUIRED_FIELDS = ['userid','username','department','designation']

    def __str__(self):
        lis = (self.userid,self.department,self.designation,self.username)
        return "/".join(lis)

class Post(models.Model):
    userid    = models.CharField(max_length=25,default=' ')
    image     = models.ImageField(upload_to='images/',height_field=None,width_field=None,max_length=None,blank=True)
    message   = models.TextField(max_length=128)
    date      = models.DateTimeField(default=datetime.now())
    likediff  = models.CharField(max_length=5000,default='')
    likecount = models.IntegerField(default=0)
    
    REQUIRED_FIELDS = ['image','message']