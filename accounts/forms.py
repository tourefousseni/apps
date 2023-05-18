from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth import get_user_model
from django import forms
from django.forms import widgets
import datetime
from accounts.models import User
from .views import *

# UserModel = get_user_model()

# ==============================================
#                  FORM ACCOUNTS
#                        START
# ==============================================
# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = get_user_model
#         fields = ('username', 'email')


# class UserForm(UserCreationForm):
#     class Meta:
#         model = get_user_model
#         fields = ('username', 'email')
# from accounts.views import UserRegisterForm


class UserRegistrationForm(UserCreationForm):
    # date_birth = forms.DateField(label="Date Birth", widget=forms.DateInput(attrs={
    #     'class': 'form-control',
    #     'type': 'date'}))
    # email      = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Enter Email Here' }))
    # last_name  = forms.CharField(label='last_name', widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Last Name' }))
    # first_name = forms.CharField(label='first_name', widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name' }))

    class Meta:
            model = get_user_model()
            fields = [
                'email',
                'first_name',
                'last_name',
                'username',
                'phone',
                # 'date_birth',
                'password1',
                'password2']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    phone    = forms.CharField(max_length=20)
    password = forms.CharField( widget=forms.PasswordInput)

    class Meta:
            model = get_user_model()
            fields = [
                'email',
                'username',
                'phone',
                # 'date_birth',
                'password1',
                'password2']

            # self.fields['username'].widget.attrs['class']        = 'form-control'
            # self.fields['username'].widget.attrs['placeholder']  = 'Pseudo'
            # self.fields['username'].label                        = ''
            # self.fields['username'].help_text = '<span class= "form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
            #
            # self.fields['password1'].widget.attrs['class']       = 'form-control'
            # self.fields['password1'].widget.attrs['placeholder'] = 'Password'
            # self.fields['password1'].label                       = ''
            # self.fields['password1'].help_text                   = '<ul class ="form-text text-muted small" ><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\' t be a commonly used password.</li><li>Your password can\' t be entirely numeric.</li></ul>'
            #
            # self.fields['password2'].widget.attrs['class']       = 'form-control'
            # self.fields['password2'].widget.attrs['placeholder'] = 'Comfirm password'
            # self.fields['password2'].label                       = ''
            # self.fields['password2'].help_text                   = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


# class EditProfileForm(UserChangeForm):
#         password = forms.CharField(label="", widget=forms.TextInput(attrs={'type': 'hidden'}))
#
#         class Meta:
#             model = User
#             fields = ('username',
#                       'first_name',
#                       'last_name',
#                       'email',
#                       'phone',
#                       'password')
#
#
# class  PasswordRsestForm(PasswordChangeForm):
#     password = forms.CharField(label="", widget=forms.TextInput(attrs={'type': 'hidden'}))
#
#     class Meta:
#         model = User
#         fields = ('__all__')


# ==============================================
#                  FORM ACCOUNTS
#                        END
# ==============================================
