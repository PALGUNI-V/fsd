from django.shortcuts import render
from .models import Student

def home(request):

    return render(
    request,
    'home.html'
    )


def save(request):

    Student.objects.create(

    usn=request.POST['usn'],
    name=request.POST['name'],
    company=request.POST['company']

    )

    return render(
    request,
    'home.html'
    )


def display(request):

    students=Student.objects.filter(
    company="Amazon"
    )

    return render(
    request,
    'display.html',
    {'students':students}
    )


def displayall(request):

    students=Student.objects.all()

    return render(
    request,
    'display.html',
    {'students':students}
    )