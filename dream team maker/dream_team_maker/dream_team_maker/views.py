from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import usersForm
from .forms import usersForm2,markforms
from services.models import Service
from news.models import News
from django.core.paginator import Paginator
from contactus.models import Contact

def homePage(request):
    newsData=News.objects.all()
    serviceData=Service.objects.all().order_by('service_des')
    paginator=Paginator(serviceData,2)
    page_number=request.GET.get('page')
    serviceDatafinal=paginator.get_page(page_number)
    if request.method=="GET":
        st=request.GET.get('servicename')
        if st!=None:
            serviceData=Service.objects.filter(service_icon__icontains=st)
    data={
        'serviceData':serviceDatafinal,
        'newsData':newsData
    }
    return render(request,"index.html",data)

def temalist(request):
    return render(request,"teamlist.html")

def userform(request):
    fn=usersForm()
    final=0
    data={'form':fn}
    try:
        n1=int(request.POST['num1'])
        n2=int(request.POST['num2'])
        final=n1+n2
        data={
            'form':fn,
            'n1':n1,
            'n2':n2,
            'output':final,
        
        }
        #return HttpResponseRedirect('/teamlist')
    except:
        pass
    
    return render(request,"userform.html",data)

def calculator(request):
    fn2=usersForm()
    final=0
    c=''
    data1={
        'form':fn2,
    }
    
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2
            data1={
                'c':c,
                'form':fn2,
                'output':c
            }
    except:
        c="invalid opertaion..."
        data1={
            "c":c
        }
    return render(request,"calculator.html",data1)
def even_odd(request):
    fn2=usersForm2()
    c=''
    
    if request.method=="POST":
        num=eval(request.POST.get('num1'))
        if num%2==0:
            c="even"
        else:
            c="odd"
    data={
        'form':fn2,
        'c':c
    }
    return render(request,"evenodd.html",data)
def marksheet(request):
    fn=markforms()
    percentage=''
    total=''
    if request.method=="POST":
        n1=eval(request.POST.get('sub_1'))
        n2=eval(request.POST.get('sub_2'))
        n3=eval(request.POST.get('sub_3'))
        n4=eval(request.POST.get('sub_5'))
        n5=eval(request.POST.get('sub_5'))
        percentage=((n1+n2+n3+n4+n5)/5)
        total=n1+n2+n3+n4+n5
    data={
        "form":fn,
        "per":percentage,
        "tol":total
    }
    return render(request,"marksheet.html",data)

def newsDetails(request,slug):
    newsDetails=News.objects.get(news_slug=slug)
    
    data={
        "newsDetails":newsDetails
    }
    return render(request,'newsDetails.html',data)

def contact(request):
    if request.method=="POST":
        email=request.POST.get('email')
        en=Contact(email=email)
        en.save()
    return render(request,"contact.html")
