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

# menu teilparty
def index2(request):
    return render(request, 'index2.html')

# menu roads payments
def menu_roads_pay(request):
    return render(request, 'menu_roads_pay.html')

# menu roads payments
def AT_road_pay(request):
    return render(request, 'RoadPayInfo/AT_road_pay.html')

# HR roads payments
def HR_road_pay(request):
    return render(request, 'RoadPayInfo/HR_road_pay.html')

# menu DKV setting
def DKV_box_setting(request):
    return render(request, 'RoadPayInfo/DKV_box_setting.html')

# POI/
def poi(request):
    lat = +49.100565
    lon = +5.258491
    zoom_start = 5

    # start parameter map
    m = folium.Map(location=[lat, lon], zoom_start=zoom_start)

    #add marker base Bruchsal
    folium.Marker(
        location=[49.148157,8.553572],
        tooltip="Base Bruchsal",
        popup="49.148157,8.553572",
        icon=folium.Icon(color="green"),
    ).add_to(m)

    # add marker base Chalon
    folium.Marker(
        location=[46.782522, 4.80012],
        tooltip="Base Chalon",
        popup="46.782522, 4.80012",
        icon=folium.Icon(color="green"),
    ).add_to(m)

    # add marker base Bochum
    folium.Marker(
        location=[51.4748720, 7.2931740],
        tooltip="Base Bochum",
        popup="51.4748720, 7.2931740",
        icon=folium.Icon(color="green"),
    ).add_to(m)

    # add marker base Paris 2 48.5598970, 2.2285070
    folium.Marker(
        location=[48.5598970, 2.2285070],
        tooltip="Base Paris 2",
        popup="48.5598970, 2.2285070",
        icon=folium.Icon(color="green"),
    ).add_to(m)

    # add marker Zarska Wies
    folium.Marker(
        location=[51.2067780, 15.1242180],
        tooltip="Base Zarska Wies",
        popup="51.2067780, 15.1242180",
        icon=folium.Icon(color="green"),
    ).add_to(m)

    #add line  N4
    locations = [
        [48.77346, 7.241291],
        [48.572703, 6.713767],
        [48.689371, 5.669345],
        [48.640857, 4.911575],
        [48.737867, 3.944146],
        [48.685219, 3.041926],
        [48.773103, 2.616687],
    ]

    folium.PolyLine(
        locations=locations,
        color="orange",
        weight=8,
        opacity=1,
        smooth_factor=0,
    ).add_to(m)

    #*********
    m = m._repr_html_()
    context = {
        'm': m,
    }

    return render(request, 'poi.html', context )

