from django import forms
from account.models import User
from django.contrib.auth.forms import AuthenticationForm
class Registerform(forms.ModelForm):
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['email','name','password','confirm_password']
        widgets = {
            'password': forms.PasswordInput(),
            
        }
        def clean_password(self):
            cleaned_data=super().clean()
            password=cleaned_data.get("password")
            confirm_password=cleaned_data.get("confirm_password")
            if password != confirm_password :
                self.add_error("Your password did't match")
            return cleaned_data
        def clean_email(self):
            email=self.cleaned_data.get('email')
            
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("user with this email already exist ")
            return email
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Email", widget=forms.TextInput(attrs={'autofocus': True}))

