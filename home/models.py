from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image1 = models.ImageField(upload_to = 'home/images')
    image2 = models.ImageField(upload_to = 'home/images', blank=True)

    def __str__(self):
    	return self.title

class Services(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to = 'home/services')

    def __str__(self):
    	return self.title


class Our_Product(models.Model):
   name = models.CharField(max_length=100)
   details = models.TextField(blank=True)
   image = models.ImageField(upload_to = 'home/products')
   url = models.URLField(blank=True)

   def __str__(self):
   		return self.name

class Teams(models.Model):
   name = models.CharField(max_length=100)
   profileImage = models.ImageField(upload_to = 'home/teams',blank=True)
   designation = models.CharField(max_length=100, blank=True)
   education = models.CharField(max_length=200,blank=True)
   url = models.URLField(blank=True)

   def __str__(self):
   		return self.name


class GetInTouch(models.Model):
   service = models.CharField(max_length=100,blank=True)
   name = models.CharField(max_length=100, blank=False)
   email = models.EmailField(max_length=250)
   phone = PhoneNumberField(null=False, blank=False, unique=True)
   project_details = models.TextField(blank=False)

   def __str__(self):
   		return self.name