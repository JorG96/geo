import folium
from django.shortcuts import render


# Create your views here.
def home(request):
    m=folium.Map(location=[4.703,-74.1],zoom_start=17)  
        ## exporting
    m=m._repr_html_()
    context= {'my_map': m}
    return render(request,'geoApp/home.html',context)