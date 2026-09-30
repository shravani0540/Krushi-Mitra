from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import CropField
from .models import MarketPrice
from .models import ExpertForm
from .form1 import User
from krushimitra import settings
from django.core.mail import send_mail
from .models import Government
from .models import FarmerTraining
from .form2 import User1
from .models import Newsupdate

def index(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def second(request):
    all_news = Newsupdate.objects.all().order_by('-id').values()
    template = loader.get_template('news.html')
    context ={
        'all_news': all_news
    }
    return HttpResponse(template.render(context,request))

def third(request):
    price = MarketPrice.objects.all().values()
    template = loader.get_template('marketprice.html')
    context ={
        'price': price
    }
    return HttpResponse(template.render(context,request))

def fourth(request):
    crop = CropField.objects.all().values()
    template = loader.get_template('crops.html')
    context ={
        'crop': crop
    }
    return HttpResponse(template.render(context,request))

def fifth(request):
    g1= Government.objects.all()
    template = loader.get_template('govermentschemes.html')
    context = {
        'g1': g1
    }
    return HttpResponse(template.render(context, request))


def sixth(request):
    if request.method == 'POST':
        fm = User(request.POST)
        if fm.is_valid():
            subject="Problem"
            name = fm.cleaned_data['name']
            phoneno = fm.cleaned_data['phoneno']
            village = fm.cleaned_data['village']
            taluka = fm.cleaned_data['taluka']
            district = fm.cleaned_data['district']
            problem = fm.cleaned_data['problem']
            to ='akshyakabra@jkinnovative.online'
            msg = f"Hello{name}\n,want to register a problem regarding{problem}\n contact details are{phoneno} and belongs to {village} village from {taluka} taluka in {district} district"
            send_mail(subject,msg,settings.EMAIL_HOST_USER,[to],fail_silently=False,)
            return render(request,'home.html')
    else:
        fm = User()
    return render(request,'expert.html',{'form1':fm})

def seventh(request):
    if request.method == 'POST':
        fm = User1(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            ag = fm.cleaned_data['age']
            cn = fm.cleaned_data['contact']
            tk = fm.cleaned_data['taluka']
            vg = fm.cleaned_data['village']
            dt = fm.cleaned_data['district']
            cd = fm.cleaned_data['cropdetails']
            reg = FarmerTraining(name=nm,age=ag,contact=cn,taluka=tk,village=vg,district=dt,cropdetails=cd)
            reg.save()
            print(nm)
            print(ag)
            print(cn)
            print(tk)
            print(vg)
            print(dt)
            print(cd)
    else:
        fm = User1()
    return render(request,'training.html',{'form2':fm})


# Create your views here.
