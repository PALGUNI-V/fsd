from django.shortcuts import render
from .models import Alumni


def home(request):

    return render(
        request,
        'home.html'
    )


def save(request):

    Alumni.objects.create(

        name=request.POST['name'],
        usn=request.POST['usn'],
        year=request.POST['year'],
        company=request.POST['company']

    )

    return render(
        request,
        'home.html'
    )


def display(request):

    alumni=Alumni.objects.filter(

        year=request.POST['year']

    )

    return render(
        request,
        'display.html',
        {'alumni':alumni}
    )


def displayall(request):

    alumni=Alumni.objects.all()

    return render(
        request,
        'display.html',
        {'alumni':alumni}
    )