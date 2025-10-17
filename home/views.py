from django.shortcuts import render
from .models import Home,Client

def home(request):
    homes = Home.objects.filter(recomended=True)
    clients = Client.objects.all()
    return render(request,"index.html",context={"data":homes,"clients":clients})


def blog(request):
    return render(request,"blog.html") 