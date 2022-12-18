from django.shortcuts import render
from django.db.models.functions import Length

# Create your views here.
from app.models import *
def display_topic(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    # LWO=Webpage.objects.all()
    # LWO=Webpage.objects.filter(Topic_name='football')   
    # LWO=Webpage.objects.exclude(Topic_name='Cricket')
    # LWO=Webpage.objects.all()[:6:]
    # LWO=Webpage.objects.all().order_by('Name')
    # LWO=Webpage.objects.all().order_by('Topic_name')
    # LWO=Webpage.objects.filter(Topic_name='Cricket').order_by('Name')
    # LWO=Webpage.objects.all().order_by(Length('Name'))
    # LWO=Webpage.objects.all().order_by(Length('name').desc())
    # LWO=Webpage.objects.all()
    # LWO=Webpage.objects.filter(name__startswith='m')
    # LWO=Webpage.objects.filter(name__endswith='a')
    # LWO=Webpage.objects.filter(name__contains='s')
    # LWO=Webpage.objects.filter(name__in=('Meghana','MSD'))
    # LWO=Webpage.objects.filter(name__regex='^M\w{6}')
    # LWO=Webpage.objects.all()
    # LWO=Webpage.objects.filter(Q(topic_name='Cricket') & Q(name__startswith='m'))
    # LWO=Webpage.objects.all()
    # LWO=Webpage.objects.filter(Q(topic_name='Foot Ball') | Q(url__endswith='in'))
    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    return render(request,'display_webpage.html',d)

def display_access(request):
    # LAO=AccessRecords.objects.all()
    # LAO=AccessRecords.objects.filter(date='1999-11-01')    
    # LAO=AccessRecords.objects.filter(date__year='2022')
    # LAO=AccessRecords.objects.filter(date__month='1')    
    # LAO=AccessRecords.objects.filter(date__day='14')    
    # LAO=AccessRecords.objects.filter(date__gte='1999-11-01')
    # LAO=AccessRecords.objects.filter(date__lte='1999-11-01')
    # LAO=AccessRecords.objects.filter(date__year__gte='1999')
    LAO=AccessRecords.objects.all() 
    d={'LAO':LAO}
    return render(request,'display_access.html',d)


def update_webpage(request):
    #Webpage.objects.filter(topic_name='Boxing').update(name='Naresh',url='https://Naresh.in')
    #Webpage.objects.filter(name='ABCDE').update(topic_name='Foot Ball')
    T=Topic.objects.get_or_create(topic_name='Cricket')[0]
    T.save()
    Webpage.objects.update_or_create(name='ABD',defaults={'topic_name':T,'url':'https://ABD.in'})
    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    return render(request,'display_webpages.html',d)


def delete_webpage(request):
    #Webpage.objects.filter(topic_name='Cricket').delete()
    
    Webpage.objects.all().delete()
    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    return render(request,'display_webpages.html',d)
