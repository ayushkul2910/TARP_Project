from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Cost
from etravel_search.models import User_Journey
import serial

# Create your views here.


def Ard(I):
    ser=serial.Serial("COM3",9600)
    serin =ser.readline()
    serin=str(serin)[2:9]
    ser.close()

    if str(I)==str(serin):
        return True,serin
    else:
        return False,serin


def index(request):
    template=loader.get_template('index.html')
    J_ID=1 #different for every bus
    l=User_Journey.objects.all()
    S="Access Denied"
    for i in range(len(l)):
        record=l[i]
        I=record.id
        U=record.User_id
        J=record.Journey_id
        if int(J)==J_ID:
            flag,serin=Ard(U)
            if(flag):
                S="Access Granted"
                record.Session_id=True
                record.save(update_fields=["Session_id"])
                break
                
    context={
        'S':S,
        'U':serin,
    }


    return HttpResponse(template.render(context,request))




