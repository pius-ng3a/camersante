from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.utils.translation import gettext_lazy as _


urlpatterns = [
    path('',views.index,name='index'),
    path(_('about/'),views.about,name='about'),
    path(_('contact/'),views.contact,name='contact'),
    path(_('services/'),views.services,name='services'),
    path(_('category/<int:catId>'),views.getJobByCategory,name='getJobByCategory'),
]
  #no need appending the settings here. it is enough in root dir