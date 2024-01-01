from django.shortcuts import render
import json
import urllib.request

# Create your views here.

#bfe02dda9c1b329e1f7f717de5a3d4d0

def index(request):
    if request.method=="POST":
        city= request.POST['city']
        res= urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ city+ '&appid=bfe02dda9c1b329e1f7f717de5a3d4d0').read()
        json_data= json.loads(res)
        data={
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']) + "k",
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }
    else:
        data={

        }
    print(data)
    return render(request,'index.html', data)