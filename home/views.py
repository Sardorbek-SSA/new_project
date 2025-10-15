from django.shortcuts import render
from .models import Home

def home(request):
    homes = Home.objects.filter(recomended=True)
    return render(request,"index.html",context={"data":homes})