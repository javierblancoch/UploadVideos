from django.shortcuts import render
from web.models import video #add

# Create your views here.
def home(request):
	content = video.objects.all()
	return render(request,'index.html',{'content':content,})