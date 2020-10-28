from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _
from .models import Job
from django.utils import translation
from categories.models import Category
from django.db.models import Q
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
import socket
socket.getaddrinfo('localhost', 8080)
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
	categoryJobs = Job.objects.filter(category_id=catId).order_by('-deadline').values() #include date now comparison.
	otherJobs = Job.objects.filter(~Q(category_id=catId)).order_by('-deadline').values()[:20]
	categoryCount = Job.objects.filter(category_id=catId).order_by('-deadline').count()
	return render (request,'jobs.html',{'categoryJobs':categoryJobs,'otherJobs':otherJobs,'categoryCount':categoryCount})

def sendEmail(request):
	print ('Here we are!!')
	if request.method == "POST":
		sender = request.POST.get('email')
		acknowledgment = settings.EMAIL_HOST_USER
		message = request.POST.get('message')
		subject = request.POST.get('subject')
		name = request.POST.get('name ')
		message = str(message)  + "  By  : "  + str (name)
		try:
			send_mail(subject, message, sender,['stylofyz2006@yahoo.com'])
		except BadHeaderError:
			return redirect({'failure_t': 'Erreur! Essayez plus tard!'})
		try:
			send_mail("Message recu par CamerSante","Merci pour votre interet dans nos service. Nous vous contacte avec le delais",acknowledgment,[sender,])
		except BadHeaderError:
			return redirect({'failure_t': 'Erreur! Essayez plus tard!'})
		return redirect({'success_t':'Merci! Message envoye!!'})
#def contact_success(request):


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
		
 
