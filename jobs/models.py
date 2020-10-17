from django.db import models
from time import time
from django.urls import reverse
from django.contrib.auth.models import User
from django.forms import ModelForm
# Create your models here.

def get_upload_file_name(instance,filename): #function to rename files and give a unique name
	return "upld_files/%s_%s"%(str(time()).replace('.','_'),filename)

def get_uploaded_image(instance,filename):
	return "upld_img/%s_%s"%(str(time()).replace('.','_'),filename)
class Job(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    location=models.CharField(max_length=100)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    deadline=models.DateField(null=False)
    created_at=models.DateField(blank=True,null=True,auto_now_add=True)
    updated_at=models.DateField(blank=True,null=True,auto_now=True)
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('jobs')
    def __str__(self):
        return self.title

class NewsForm(ModelForm):
	"""docstring for NewsForm"""
	class Meta:
		model = Job
		fields = ['title','description','location','user_id','deadline'] # ,'icon' left out, user_id should be picked from auth_user
class AddNews(ModelForm):
	"""docstring for AddNews"""
	def __init__(self, arg):
		super(AddNews, self).__init__()
		self.arg = arg
		