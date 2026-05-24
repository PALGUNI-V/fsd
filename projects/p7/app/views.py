from django.shortcuts import render

# Create your views here.
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
    semester=request.POST['semester'],
    status=request.POST['status']

    )

    return render(
    request,
    'home.html'
    )


def delete(request):

    Student.objects.filter(
    status="Not Paid"
    ).delete()

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