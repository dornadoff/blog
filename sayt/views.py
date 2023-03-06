from django.shortcuts import render
from .models import *



def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def blog(request):

    data = {"maqola":Maqola.objects.all()}
    return render(request, "blog.html", data)

def maqola(request, son):
    data = {"maqola":Maqola.objects.get(id=son)}
    return render(request, "maqola.html", data)

def bitta_maqola(request, son):
    a = {"maqola":Maqola.objects.get(id=son)}
    return render(request, "bitta_maqola.html", a)