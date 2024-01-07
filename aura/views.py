import random
import string

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from aura.models import Services, Itworks, Meeting
from aura.forms import MeetingForm
from accounts.models import Psychiatrist, Client

def common_data(request):
    if request.user.role == 'Psychiatrist':
        user = Psychiatrist.objects.get(user= request.user)
    else:
        user = Client.objects.get(user= request.user)
    return {
        'user_' :  user,
    }

def homepage(request):
    itworks = Itworks.objects.all()
    services = Services.objects.all()

    context = {
        'itworks':itworks,
        'services':services,
    }

    return render(request, 'index.html',context)

def create_meeting(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            meeting = form.save()
            meeting.client = Client.objects.get(user= request.user)
            meeting.save()
            return redirect('/dashboard/')  # Assuming you have a meeting detail view

    else:
        form = MeetingForm()

    return render(request, 'aura/new-meeting.html', {'form': form,**common_data(request),'nav':'create'})

def schedule_meeting(request,id):
    meet = Meeting.objects.get(id=id)
    if request.method == 'POST':
        datetime  = request.POST.get('date')
        meet.date = datetime
        meet.save()
        return redirect('/dashboard/')
    return render(request, 'aura/schedule_meet.html')



def generate_unique_random_numbers():
    
    digits = string.digits
    number = ""
    for i in range(10):
        number += random.choice(digits)
    number = int(number)
   
    return number


def add_meeting(request,id):
    meet = Meeting.objects.get(id=id)
    meetid = generate_unique_random_numbers()
    meet.meetingID = meetid
    meet.save()
    return redirect(f'/meeting/{meetid}/')

def approve_meeting(request,id):
    meet = Meeting.objects.get(id=id)
    meet.approved = True
    meet.save()
    return redirect('/dashboard/')

def end_meeting(request,id):
    meet = Meeting.objects.get(id=id)
    meet.is_done = True
    meet.save()
    return redirect('/dashboard/')

@login_required
def dashboard(request):
    if request.user.role == 'Psychiatrist':
        user = Psychiatrist.objects.get(user= request.user)
        requested = Meeting.objects.filter(pychiatrist = user,is_done=False,approved=False)
        done = Meeting.objects.filter(pychiatrist = user,is_done=True)
        all = Meeting.objects.filter(pychiatrist = user)
    else:
        user = Client.objects.get(user= request.user)
        requested = Meeting.objects.filter(client = user,is_done=False,approved=False)
        done = Meeting.objects.filter(client = user,approved=True)
        all = Meeting.objects.filter(client = user)
    context = {
        'requested':requested,
        'done': done,
        'all':all,
        'nav':'dash',
        **common_data(request),
    }
    return render(request,'aura/psycdashboard.html', context)

@login_required
def videocall(request,meetingid):
    context = {
        'name': request.user.full_name,
        'id':meetingid,
    }
    return render(request, 'aura/videocall.html', context)

@login_required
def join_room(request,meetingID):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect(f"/meeting/{roomID}/" )
    return render(request, 'aura/joinroom.html', {'id':meetingID})

