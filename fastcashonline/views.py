from django.shortcuts import render
from fastcashonline import models
# Create your views here.

def HomePage(request):
    applicationname = GetAppName()

    data ={
        "AppName" : applicationname,
        "specials" : "Apply for a quick cash today and you can stand a chance to win a V-Class"
    }

    return render(request,'index.html', data)

    # return render(request,'index.html', {"AppName" : applicationname})


def GetAppName():
    return "FAST CASH ONLINE - Instant Money"



def EmployersList(request):

    data ={
        "AppName": GetAppName(),
        "Employers": models.Employers.objects.all()
    }
    return render(request,'employerslist.html',data)