from django.shortcuts import render

from .models import Slider , Services

def home(request):
	sliderData = Slider.objects.all()
	serviceData = Services.objects.all()
	return render(request,'home/homebase.html',{'slider':sliderData,'services':serviceData})