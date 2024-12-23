from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from account.froms import Registerform,LoginForm
from account.models import User
from django.contrib import messages
from django.conf import settings
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from account.utils import send_activation_email
def home(request):
    return render(request,'base.html')
def register(request):
 if request.method=="POST":
       form =Registerform(request.POST)
       if form.is_valid():
           user=form.save(commit=False)
           user.set_password(form.cleaned_data["password"])
           user.is_active=False
           user.save()
           uidb64=urlsafe_base64_encode(force_bytes(user.pk))
           token=default_token_generator.make_token(user)
           activation_link=reverse('activate',kwargs={'uidb64':uidb64,
                                              'token':token})
           complete_activation_link=f'{settings.SITE_DOMAIN}{activation_link}'
           send_activation_email(user.email,complete_activation_link)

           messages.success(request,
                            "registeration successfully done ")
           return redirect('/login/')
 else:
            form=Registerform()

 return render(request,'account/register.html',{"form":form})
def activate_account(request,uidb64,token):
    try:
        uid=force_bytes(urlsafe_base64_decode(uidb64))
        user=User.objects.get(pk=uid)
        if user.is_active:
            messages.warning(request,"This account already activate")
            return redirect('login')
        if default_token_generator.check_token(user,token):
            user.is_active=True
            user.save()
            messages.success(request,"your account is activated ")
            return redirect('/login/')
        else:
            messages.error(request,"the token is invalid or expired")
            return redirect('register')
    except(TypeError,ValueError,
        user.DoesNotExist,OverflowError):
        messages.error(request,"invalid activation link")
        return redirect('login')
        
def login_view(request):
    
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            print(email)
            print(password)
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in!")
                if user.is_seller:
                 return redirect('seller_dashboard')
                elif user.is_customer:
                 return redirect('customer_dashboard')
            else:
                messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Invalid form submission.")
    else:
        form = LoginForm()
 
    return render(request, 'account/login.html', {'form': form})

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('user_login')