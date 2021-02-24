from django.shortcuts import render

from .models import Slider

def home(request):
	sliderdata = Slider.objects.all()
	return render(request,'home/homebase.html',{'slider':sliderdata})