from django.urls import path
from accounts.views import  clientRegistration, login_user,psyclogin, psycRegistration ,activate

app_name = "accounts"

urlpatterns = [
    path('login/', login_user, name='login'),
    path('register/', clientRegistration, name="sign-up"),
    path('psyclogin/', psyclogin, name='psyclogin'),
    path('psycregister/', psycRegistration, name="psycsign-up"),
    path('activate/<str:uidb64>/<str:token>/', activate, name='activate'),
    # path('reset/<str:uidb64>/<str:token>/<str:password>/', reset, name='reset'),
]