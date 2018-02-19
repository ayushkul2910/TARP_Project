from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Cost

# Create your views here.


def Ard(I):
    Journey_ID=2
    if I==Journey_ID:
        return True
    else:
        return False


def index(request):
    
    l=Cost.objects.all()
    for i in range(len(l)):
        record=l[i]
        I=record.ID
        T=record.To_city
        F=record.From_city
        P=record.Price
        flag=Ard(I)
        if(flag):
            S="Access Granted"
        else:
            S="Access Denied"

    return HttpResponse("<h2>"+S+"</h2>")




