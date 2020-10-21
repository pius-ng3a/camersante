from django.contrib import admin
from .models import Category

# Register your models here.
# Register your models here.
class CategoriesAdmin(admin.ModelAdmin):
	"""docstring for MemberAdmin"""
	fieldsets=[
	("Title ",{'fields':['title']}),
	("Image",{'fields':['category_icon']}),
    ("User Id ",{'fields':['user_id']}),
	 
	]
admin.site.register(Category)