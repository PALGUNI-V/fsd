from django.shortcuts import render
from .models import Student

def home(request):

    return render(
    request,
    'home.html'
    )


def save(request):

    Student.objects.create(

    name=request.POST['name'],
    usn=request.POST['usn'],
    grade=request.POST['grade']

    )

    return render(
    request,
    'home.html'
    )


def display(request):

    students=Student.objects.filter(
    grade="O"
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