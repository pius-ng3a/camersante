from django.contrib import admin

# Register your models here.
from .models import Job
 
class JobAdmin(admin.ModelAdmin):
	"""docstring for QuarterAdmin"""
    
	fieldsets=[
	("Job Title ",{'fields':['title']}),
	("Description ",{'fields':['descritption']}),
	("Deadline ",{'fields':['deadline']}),
    ("Location",{'fields':['location']}),
    ("Deadline",{'fields':['deadline']}),

	 
	]
 
admin.site.register(Job)
