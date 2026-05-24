from django.shortcuts import render

def home(request):

    return render(
        request,
        'home.html'
    )


def result(request):

    data={

        'name':request.POST.get('name'),
        'age':request.POST.get('age'),
        'email':request.POST.get('email'),
        'phone':request.POST.get('phone'),
        'address':request.POST.get('address')

    }

    return render(
        request,
        'result.html',
        data
    )