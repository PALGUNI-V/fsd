from django.shortcuts import render
import html

def home(request):

    name=""
    safe_name=""

    if request.method=="POST":

        name=request.POST.get('name')

        safe_name=html.escape(name)

    return render(
        request,
        'home.html',
        {
            'name':name,
            'safe_name':safe_name
        }
    )