from django.db import models
from time import time
from django.urls import reverse
from django.contrib.auth.models import User
from django.forms import ModelForm
# Create your models here.

def get_upload_file_name(instance,filename): #function to rename files and give a unique name
	return "upld_videos/%s_%s"%(str(time()).replace('.','_'),filename)

def get_uploaded_image(instance,filename):
	return "upld_cat/%s_%s"%(str(time()).replace('.','_'),filename)
class Category(models.Model):
	"""Job category model."""
	title=models.CharField(max_length=100)
	user_id = models.ForeignKey(User,on_delete=models.CASCADE)
	created_at = models.DateField(blank=True,null=True ,auto_now_add=True)
	updated_at= models.DateField(blank=True, null=True,auto_now=True)
	category_icon =models.ImageField(upload_to=get_uploaded_image,blank=True)
	def __unicode__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('categories')
	def __str__(self):
		return self.title