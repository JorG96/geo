from django.shortcuts import render
import folium

# Create your views here.
def home(request):
    m=folium.Map(location=[-16.22,-71.59],zoom_start=10#)  
        ## exporting
    m=m._repr_html_()
    context= {'my_map': m}
    return render(request,'geoApp/home.html',context)