from django.urls import path
from account.views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('',home,name="home"),
    path('register/',register,name="user_register"),
    path('activate/<str:uidb64>/<str:token>/',activate_account,name="activate"),
    path('login/',login_view,name="user_login"),
    path('logout/',LogoutView.as_view(),name="user_logout"),
    

]
