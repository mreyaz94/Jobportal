from django.shortcuts import render
from webapp.models import Filter_DB

# Create your views here.

def filter_view(request):
    obj = Filter_DB.objects.all()
    return render(request,'webapp/home.html',{'obj':obj})

def upper_view(request):
    obj = Filter_DB.objects.all()
    return render(request,'webapp/upper.html',{'obj':obj})

def lower_view(request):
    obj = Filter_DB.objects.all()
    return render(request,'webapp/lower.html',{'obj':obj})