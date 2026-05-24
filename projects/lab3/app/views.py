from django.shortcuts import render
import requests

def home(request):

    weather=None
    error=""

    if request.method=="POST":

        city=request.POST.get('city')

        api_key="d5e26f92c66c81d6e94d2a64490e9fb5"

        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response=requests.get(url)

        data=response.json()

        if data["cod"]==200:

            weather={

                'city':data['name'],
                'temp':data['main']['temp'],
                'desc':data['weather'][0]['description']

            }

        else:

            error="Invalid City Name"

    return render(
        request,
        'home.html',
        {
            'weather':weather,
            'error':error
        }
    )