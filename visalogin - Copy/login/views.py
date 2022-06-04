from django.shortcuts import render,redirect
from login.forms import empform
from login.models import emplogin
from django.http import HttpResponse
def register(request):
    if(request.method=='POST'):
        frm=empform(request.POST)
        if (frm.is_valid()):
            frm.save()
            return HttpResponse("Thanks for Register")
    else:
        frm=empform()
    return render(request,'home.html',{'frm':frm})
def check(request):
    if(request.method=='POST'):
        logid=request.POST['name']
        Passportid=request.POST['passportid']
        try:
    
            emp=emplogin.objects.get(name=logid,passportid=Passportid)
            return render(request,'home1.html',{'emp':emp})
        except:
            return HttpResponse("Sorry")
    else:
        frm=empform()
    return render(request,'login.html',{'frm':frm})
# Create your views here.
def Main(request):
    return render(request,'index.html')
def show(request):
    return render(request,'new.html')