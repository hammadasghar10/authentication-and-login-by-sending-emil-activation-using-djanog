from django.urls import path
from seller.views import *
urlpatterns = [
    path('dashboard/',seller_dashboard,name="seller_dashboard"),
    
]
