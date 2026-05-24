from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Faculty


def home(request):

    return render(
        request,
        'home.html'
    )


def save(request):

    Faculty.objects.create(

        fid=request.POST['fid'],
        title=request.POST['title'],
        name=request.POST['name'],
        branch=request.POST['branch']

    )

    return render(
        request,
        'home.html'
    )


def display(request):

    faculty=Faculty.objects.filter(

        title="Professor",
        branch="CSE"

    )

    return render(
        request,
        'display.html',
        {'faculty':faculty}
    )


def displayall(request):

    faculty=Faculty.objects.all()

    return render(
        request,
        'display.html',
        {'faculty':faculty}
    )