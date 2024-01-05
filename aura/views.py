from django.shortcuts import render
from aura.models import Services,Itworks

def homepage(request):
    itworks = Itworks.objects.all()
    services = Services.objects.all()

    context = {
        'itworks':itworks,
        'services':services,
    }

    return render(request, 'index.html',context)

def phsycohomepage(request):
    return render(request,'aura/index.html')

# Create your views here.
