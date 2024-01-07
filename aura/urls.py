from django.urls import path
from aura.views import (
    homepage,dashboard,
    join_room,videocall,
    create_meeting,schedule_meeting,approve_meeting,
    add_meeting,end_meeting,
)

app_name = "aura"

urlpatterns = [
    path('', homepage, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('new-meeting/', create_meeting, name='new-meeting'),
    path('create-meeting/<str:id>/', add_meeting, name='create-meeting'),
    path('schedule-meeting/<str:id>/', schedule_meeting, name='schedule-meeting'),
    path('approve-meeting/<str:id>/', approve_meeting, name='approve-meeting'),
    path('end-meeting/<str:id>/', end_meeting, name='end-meeting'),
    path('meeting/<str:meetingid>/',videocall, name='meeting'),
    path('join/<str:meetingID>/',join_room, name='join-room'),
]