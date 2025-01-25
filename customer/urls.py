from django.urls import path
from customer.views import *
urlpatterns = [
    path('changepassword/<int:id>',change_password,name='change_password'),
    path('<str:username>/',customer_dashboard,name="customer_dashboard")
]
