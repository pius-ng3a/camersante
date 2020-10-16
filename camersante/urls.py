"""camersante URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns
urlpatterns = [
    re_path(r'^i18n/',include('django.conf.urls.i18n')),
    re_path(r'^admin/', admin.site.urls),
    path('', include('jobs.urls')),
    #path('about/',include('jobs.urls')),
    #path('contact/',include('jobs.urls')),
    re_path(r'^', include('jobs.urls')), 
    #path('services/',include('jobs.urls')),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

#urlpatterns += i18n_patterns(
#    path('admin/', admin.site.urls),
#    path('', include('jobs.urls')),
#    path('about/',include('jobs.urls')),
#    path('contact/',include('jobs.urls')),
#    path('jobs/', include('jobs.urls')), 
#    path('set_language/', include('jobs.urls')),
#    prefix_default_language =False,
    
#) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
