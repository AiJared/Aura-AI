from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from aura.models import Services, Itworks, Meeting
from accounts.models import Psychiatrist, Client

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
    psyco = Psychiatrist.objects.get(user= request.user)
    requested = Meeting.objects.filter(pychiatrist = psyco,is_done=False)
    done = Meeting.objects.filter(pychiatrist = psyco,is_done=True)
    all = Meeting.objects.all()
    context = {
        'requested':requested,
        'done': done,
        'all':all,
    }
    return render(request,'aura/psycdashboard.html', context)

@login_required
def videocall(request):
    if request.method == 'POST':
        roomID = request.POST.get('roomID')
        print(roomID)
    return render(request, 'aura/videocall.html', {'name': request.user.full_name})

@login_required
def join_room(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/meeting?roomID=" + roomID)
    return render(request, 'aura/joinroom.html')

