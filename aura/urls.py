from django.urls import path
from aura.views import (
    homepage,phsycohomepage,clienthomepage,
    join_room,videocall,
)

app_name = "aura"

urlpatterns = [
    path('', homepage, name='home'),
    path('dashboard/', phsycohomepage, name='dashboard'),
    path('clientdashboard/', clienthomepage, name='clientdashboard'),
    path('meeting/',videocall, name='meeting'),
    path('join/',join_room, name='join_room'),
]