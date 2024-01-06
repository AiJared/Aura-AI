from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from aura.models import Services,Itworks

def homepage(request):
    itworks = Itworks.objects.all()
    services = Services.objects.all()

    context = {
        'itworks':itworks,
        'services':services,
    }

    return render(request, 'index.html',context)

@login_required
def phsycohomepage(request):
    return render(request,'aura/index.html')

@login_required
def videocall(request):
    return render(request, 'aura/videocall.html', {'name': request.user.first_name + " " + request.user.last_name})

@login_required
def join_room(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/meeting?roomID=" + roomID)
    return render(request, 'aura/joinroom.html')