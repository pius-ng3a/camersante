from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _
from .models import Job
from django.utils import translation
from categories.models import Category
from django.db.models import Q
# Create your views here.
def index(request):
    #example of code to indicate need translation
    my_var = _("My variable in English") #we have used gettext here to say that the string needs to be translated if passed to a template.
    categories = Category.objects.order_by('-created_at')
    return render(request, "index.html",{'categories':categories})
def about(request):
    return render(request, "about.html")
def get_given_job(request,id): #find job with specific Id number
    job = Job.objects.get(id=id)
def services(request):
    return render(request, 'services.html')
#get jobs of a given category
def getJobByCategory(request,catId):
	categoryJobs = Job.objects.filter(category_id=catId).order_by('-created_at').values() #include date now comparison.
	otherJobs = Job.objects.filter(~Q(category_id=catId)).order_by('-created_at').values()[:20]
	return render (request,'jobs.html',{'categoryJobs':categoryJobs,'otherJobs':otherJobs})

def news(request):
	news_items = Video.objects.order_by('-created_at')[2:10]
	latest_news=Video.objects.order_by('-created_at')[:2]
	podcast_items = Podcast.objects.order_by('-created_at')[2:10]
	latest_podcast = Podcast.objects.order_by('-created_at')[:2]
	return render(request, "news.html",{'news_items':news_items,'podcast_items':podcast_items,'latest_news':latest_news,'latest_podcast':latest_podcast})
def contact(request):
    return render(request, "contact.html")

class PlayMovie(TemplateView):
	"""docstring for PlayMovie"""
	template_name="play.html"

def play_video(request,videoid):
	video =Video.objects.get(pk = videoid)
	return render(request, 'play.html',{"video":video})
		
 
