from django.urls import path
from aura.views import homepage,phsycohomepage

app_name = "aura"

urlpatterns = [
    path('', homepage, name='home'),
    path('dashboard/', phsycohomepage, name='dashboard'),
]