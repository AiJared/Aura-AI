from django.urls import path
from accounts.views import homepage, clientRegistration, login_user, activate

app_name = "accounts"

urlpatterns = [
    path('', homepage, name='home'),
    path('login/', login_user, name='login'),
    path('register/', clientRegistration, name="sign-up"),
    path('activate/<str:uidb64>/<str:token>/', activate, name='activate'),
    # path('reset/<str:uidb64>/<str:token>/<str:password>/', reset, name='reset'),
]