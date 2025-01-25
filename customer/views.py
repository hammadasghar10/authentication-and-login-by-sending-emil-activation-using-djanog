from django.shortcuts import render,redirect,get_object_or_404
from account.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from account.decoraters import customer_required
@login_required(login_url='/login/')
@customer_required
def customer_dashboard(request,username):
    username=request.user.name
    return render(request,'customer/customer_profile.html')
@login_required
def change_password(request, id):
    user = get_object_or_404(User, id=id)  # Retrieve the user by id

    if request.method == "POST":
        form = PasswordChangeForm(user, request.POST)  # Bind the form to the user
        if form.is_valid():
            form.save()
            logout(request)
            return redirect('user_login')  # Redirect to login after password change
    else:
        form = PasswordChangeForm(user)  # Initialize the form with the user

    return render(request, 'customer/changepassword.html', {'form': form})