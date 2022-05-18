from django.shortcuts import render
from. models import Travelplace,Travelteam


def fun(request):
    obj=Travelplace.objects.all()
    obj1=Travelteam.objects.all()
    return render(request,"index.html",{'result':obj,'value':obj1})
