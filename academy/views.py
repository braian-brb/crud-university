
from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages

# Create your views here.


def home(request):
    courseList = Course.objects.all()
    messages.success(request, 'Courses listed!')
    return render(request, 'courseManagment.html', {'courses': courseList})



def registerCourse(request):
    code=request.POST['code']
    name=request.POST['name']
    credits=request.POST['credits']


    course = Course.objects.create(
        code= code,
        name=name,
        credits=credits
    )
    messages.success(request, 'Registered course!')
    return redirect('/')

def courseEdition(request, code):
    course = Course.objects.get(code=code)
    return render(request, 'courseEdition.html',{'course': course})

def editCourse(request):
    code=request.POST['code']
    name=request.POST['name']
    credits=request.POST['credits']

    course = Course.objects.get(code=code)
    course.name= name
    course.credits=credits
    course.save()
    messages.success(request, 'Edited course!')
    return redirect('/')



def deleteCourse(request, code):
    course = Course.objects.get(code=code)
    course.delete()
    messages.success(request, 'Deleted course!')
    return redirect('/')
