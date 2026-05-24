from django.shortcuts import render
from .models import Student

def home(request):

    if request.method=="POST":

        Student.objects.create(

        usn=request.POST['usn'],
        name=request.POST['name'],
        subject=request.POST['subject'],
        cie=request.POST['cie']

        )

    return render(
    request,
    'home.html'
    )


def display(request):

    students=Student.objects.filter(
    cie__lt=20
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