from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.decoraters import seller_required
@login_required(login_url='/login/')
@seller_required
def seller_dashboard(request):
    return render(request,'seller/seller_profile.html')