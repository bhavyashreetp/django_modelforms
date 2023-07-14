from django.shortcuts import render

# Create your views here.

from app.forms import *
from django.http import HttpResponse

def insert_topic(request):
    TMFO=TopicModelForm()
    d={'TMFO':TMFO}

    if request.method=='POST':
        TMFD=TopicModelForm(request.POST)
        if TMFD.is_valid():
            TMFD.save()
        return HttpResponse('data is submitted')

    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    WMO=WebpageModelForm()
    d={'WMO':WMO}

    if request.method=='POST':
        WMD=WebpageModelForm(request.POST)
        if WMD.is_valid():
            WMD.save()

        return HttpResponse('data submitted')

    return render(request,'insert_webpage.html',d)




def insert_accessrecord(request):
    ARMFO=AccessRecordModelForm()
    d={'ARMFO':ARMFO}

    if request.method=='POST':
        ARMFD=AccessRecordModelForm(request.POST)
        if ARMFD.is_valid():
            ARMFD.save()
        return HttpResponse('data is submitted')
    return render(request,'insert_accessrecord.html',d)