from django.shortcuts import render
from django.http import HttpResponse
import folium

# Create your views here.
def index(request):
    #return HttpResponse("Hello from the Shop app")
    return render(request, 'index.html')

# info for driver
def info(request):
    return render(request, 'info.html')

# menu bar
def menu(request):
    return render(request, 'menu.html')

# POI
def poi(request):
    #m = folium.Map(location=[49.147417, 8.551702], zoom_start=9)()
    #context = {'map': m._repr_html_()}

    m = folium.Map(location=[49.147417, 8.551702], zoom_start=9)

    folium.Marker(
        location=[49.148157,8.553572],
        tooltip="Base Bruchsal",
        popup="49.148157,8.553572",
        icon=folium.Icon(color="green"),
    ).add_to(m)

    m = m._repr_html_()
    context = {
        'm': m,
    }

    return render(request, 'poi.html', context )

