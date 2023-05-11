from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth import get_user_model
from django import forms
from django.forms import widgets
import datetime


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

class RegisterForm(UserCreationForm):
    email      = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Enter Email Here' }))
    last_name  = forms.CharField(label='last_name', widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Last Name' }))
    first_name = forms.CharField(label='first_name', widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name' }))

    class Meta:
            model =get_user_model()
            fields = [
                'first_name',
                'last_name',
                'username',
                'email',
                'password',
                'password2']

class LoginForm(forms.Form):
    username =forms.CharField(max_length=65)
    password= forms.CharField(max_length=65, widget=forms.PasswordInput)

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


class EditProfileForm(UserChangeForm):
        password = forms.CharField(label="", widget=forms.TextInput(attrs={'type': 'hidden'}))

        class Meta:
            model = get_user_model()
            fields = ('username',
                      'first_name',
                      'last_name',
                      'email',
                      'password')


class  PasswordRsestForm(PasswordChangeForm):
    password = forms.CharField(label="", widget=forms.TextInput(attrs={'type': 'hidden'}))

    class Meta:
        model = get_user_model()
        fields = ('__all__')


# ==============================================
#                  FORM ACCOUNTS
#                        END
# ==============================================
