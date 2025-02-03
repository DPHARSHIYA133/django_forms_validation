from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from app.models import *
# Create your views here.
def insertTopic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            topic_name=TFDO.cleaned_data['topic_name']
            LTO=Topic.objects.get_or_create(topic_name=topic_name)
            if LTO[1]:
                return HttpResponse(f'{topic_name} is created')
            else:
                return HttpResponse(f'{topic_name} is already exists!.')
        else:
            return HttpResponse('Invalid data')
    return render(request,'insert_topic.htm',d)

def insertWebpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            topic_name=WFDO.cleaned_data['topic_name']
            name=WFDO.cleaned_data['name']
            url=WFDO.cleaned_data['url']
            email=WFDO.cleaned_data['email']
            TO=Topic.objects.get_or_create(topic_name=topic_name)
            WTO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)
            if WTO[1]:
                    return HttpResponse(f'{name} is created')
            else:
                return HttpResponse(f'{name} is already exists!.')
        else:
            return HttpResponse('Invalid data')
    return render(request,'insertion_webpage.htm',d)

def insertAccessrecord(request):
    EAFO=AccessrecordForm()
    d={'EAFO':EAFO}
    if request.method=='POST':
        AFDO=AccessrecordForm(request.POST)
        if AFDO.is_valid():
            name=AFDO.cleaned_data['name']
            date=AFDO.cleaned_data['date']
            author=AFDO.cleaned_data['author']
            NO=Webpage.objects.filter(name=name).first()
            ATO=AccessRecords.objects.get_or_create(name=NO,date=date,author=author)
            if ATO[1]:
                return HttpResponse(f'{author} is created')
            else:
                return HttpResponse(f'{author} is already exists!.')
        else:
            return HttpResponse('Invalid data')
    return render(request,'insert_accessrecord.htm',d)
