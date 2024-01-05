from django.urls import path
from aura.views import homepage

app_name = "aura"

urlpatterns = [
    path('', homepage, name='home'),
]