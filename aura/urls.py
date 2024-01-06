from django.urls import path
from aura.views import (
    homepage,phsycohomepage,
    join_room,videocall,
)

app_name = "aura"

urlpatterns = [
    path('', homepage, name='home'),
    path('dashboard/', phsycohomepage, name='dashboard'),
    path('meeting/',videocall, name='meeting'),
    path('join/',join_room, name='join_room'),
]