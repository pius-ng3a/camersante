from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.utils.translation import gettext_lazy as _


urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('services/',views.contact,name='services'),
]
  #no need appending the settings here. it is enough in root dir