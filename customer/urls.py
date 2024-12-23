from django.urls import path
from customer.views import *
urlpatterns = [
    path('dashboard/',customer_dashboard,name="customer_dashboard")
]
