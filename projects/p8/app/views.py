from django.shortcuts import render
from .models import Employee

def home(request):

    return render(
    request,
    'home.html'
    )


def save(request):

    Employee.objects.create(

    name=request.POST['name'],
    email=request.POST['email'],
    phone=request.POST['phone'],
    date=request.POST['date'],
    job=request.POST['job'],
    salary=request.POST['salary']

    )

    return render(
    request,
    'home.html'
    )


def display(request):

    employees=Employee.objects.filter(
    salary__gt=50000
    )

    return render(
    request,
    'display.html',
    {'employees':employees}
    )


def displayall(request):

    employees=Employee.objects.all()

    return render(
    request,
    'display.html',
    {'employees':employees}
    )