from django.urls import path
from account.views import *
urlpatterns = [
    path('',home,name="home"),
    path('register/',register,name="user_register"),
    path('activate/<str:uidb64>/<str:token>/',activate_account,name="activate"),
    path('login/',login_view,name="user_login"),
    path('logout/',user_logout,name="user_logout"),
]
