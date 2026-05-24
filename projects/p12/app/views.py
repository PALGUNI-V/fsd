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
        department=request.POST['department'],
        grade=request.POST['grade']

    )

    return render(
        request,
        'home.html'
    )


def update(request):

    Student.objects.filter(
        name=request.POST['name']
    ).update(

        grade=request.POST['newgrade']

    )

    students=Student.objects.all()

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