from django.shortcuts import render
from WebApp.models import Job

# Create your views here.



def home_page(request):
    # employee=Employee1.objects.all()
    # return render(request, 'WebApp/result.html',{'employees':employee})
    # job=Job.objects.filter(locations='Mumbai')
    # return render(request, 'WebApp/Mumjob.html', {'job':job})
    return render(request, 'WebApp/home.html')

def mumbai_jobs(request):
    # job = Job.objects.all()
    job = Job.objects.filter(locations='Mumbai')
    return render(request, 'WebApp/Mumjob.html', {'job':job})

def hyderabad_jobs(request):
    # job = Job.objects.all()
    job = Job.objects.filter(locations='Hyderabad')
    return render(request, 'WebApp/Hydjob.html', {'job':job})

def pune_jobs(request):
    # job = Job.objects.all()
    job = Job.objects.filter(locations='Pune')
    return render(request, 'WebApp/Punejob.html', {'job':job})

def all_jobs(request):
    # job = Job.objects.all()
    job = Job.objects.all()
    return render(request, 'WebApp/result.html', {'job':job})
