from django.shortcuts import render
from .models import Avion

# Create your views here.
def indexAviones(request):
    losAvion=Avion.objects.all()
    return render(request,'gestAviones.html',{'myavion':losAvion})