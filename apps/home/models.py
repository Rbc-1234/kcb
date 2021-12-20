# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Brand(models.Model):
    brandname=models.CharField(max_length=200,unique=True)
    logo=models.FileField(default=None)
    status=models.CharField(max_length=200,default=None)

class Size(models.Model):
    brandsize=models.IntegerField(max_length=200, unique=True)

class BrandColor(models.Model):
    color=models.CharField(max_length=200, unique=True)

class Category(models.Model):
    brandcategory=models.CharField(max_length=200, unique=True)
    

class Master_Page(models.Model):
    masterid=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=200)
    discription=models.TextField()
    document=models.FileField(default=None)
    brandsize = models.ForeignKey('Size',on_delete=models.CASCADE)
    brandname = models.ForeignKey('Brand',on_delete=models.CASCADE)
    brandcategory = models.ForeignKey('Category',on_delete=models.CASCADE)
    price=models.CharField(max_length=200)
    masterstatus=models.CharField(max_length=200,default=None)
    
    def __str__(self):
        return self.id.brandsize,id.brandname,id.brandcategory

    


