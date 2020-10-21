from django.contrib import admin

# Register your models here.
from .models import Job
 
class JobAdmin(admin.ModelAdmin):
	"""docstring for QuarterAdmin"""
    
	fieldsets=[
	("Job Title ",{'fields':['title']}),
	("Description ",{'fields':['descritption']}),
    ("Location",{'fields':['location']}),
    ("Deadline",{'fields':['deadline']}),
	("Job Category",{'fields':['category_id']}),

	 
	]
 
admin.site.register(Job)
