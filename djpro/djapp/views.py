from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def upload(request):
    if request.method=="POST":
        a=uploadform(request.POST,request.FILES)
        if a.is_valid():
            iname=a.cleaned_data['iname']
            iprice=a.cleaned_data['iprice']
            file=a.cleaned_data['file']
            b=uploadmodel(iname=iname,iprice=iprice,file=file)
            b.save()
            return HttpResponse("success")
        else:
            return  HttpResponse("failed")
    else:
        return render(request,"upload.html")

            # Create your views here.
def itemdisplay(request):
    a=uploadmodel.objects.all()
    name=[]
    price=[]
    files=[]
    for i in a:
        path=i.file.url
        name.append(i.iname)
        price.append(i.iprice)
        files.append(path)
    return render(request,"itemdisplay.html",{'iname':name,'iprice':price,'file':files})
def itemorder(request,iname):
    a=uploadmodel.objects.filter(iname=iname)
    return render(request,"itemorder.html",{'data':a})

def itembill(request):
    if request.method=="POST":
        iname=request.POST.get('iname')
        iprice=request.POST.get('iprice')
        qty=request.POST.get('qty')
        total=int(iprice)*int(qty)
        a=itembillmodel(iname=iname,iprice=iprice,qty=qty,total=total)
        a.save()
    return render(request,"itembill.html",{'iname':iname,'total':total})