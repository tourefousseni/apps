from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth import authenticate,  login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
import io
from .import views
import time
time.sleep(5)

from accounts.models import *
from .forms import *

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def register(request):
    username = None
    email    = None
    password = None
    if request.method == 'POST':
        # GET FORM VALUES
      first_name = request.POST.get('first_name')
      last_name  = request.POST.get('last_name')
      username   = request.POST.get('username')
      email      = request.POST.get('email')
      password   = request.POST.get('password')
      password2  = request.POST.get('password2')

 # Check if passwords match

      if password == password2:
          # check username
          # if User.objects.filter(username=username).exists():
          #     messages.error(request, 'that username is take')
          #     return redirect('accounts:register')
          # else:
              if User.objects.filter(email=email).exists():
                  messages.error(request, 'this email is using')
                  return redirect('accounts:register')
              else:
              # LOOKS GOOD
               user = User.objects.create_user(first_name=first_name,
                                               last_name=last_name,
                                               username=username,
                                               email=email,
                                               password=password,
                                               password2=password2)
              # authenticate.login(request, user)
              # messages.success(request, 'you are now logged in')
              # return redirect('accounts:dashboard')
              user.save()
              messages.success(request, 'you are now registered and can log in')
              return redirect('accounts:login')
        # else:
        #   messages.error(request,'Passwords do not match')
        #   return redirect('accounts:register')
    else:
      return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:dashboard')
        else:
            return redirect('accounts:login')
    else:
        return render(request, 'accounts/login.html')

@login_required
def logout(request):
     messages.success(request, ('You Have Been Logged out...'))
     return redirect('accounts:login')

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, ('You Have been Logged In !'))
#             return redirect('accounts:dashboard')
#         else:
#             messages.success(request, ('Error you can try again !'))
#             return redirect('accounts:login')
#     else:
#         return render(request, 'accounts/login.html', {})

# def login(request):
#     if request.method == 'POST':
#         return redirect('accounts:dashboard')
#     else:
#         return render(request, 'accounts/login.html')




# def register(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             messages.success(request,('You Have Registered now...'))
#             return redirect('accounts:dashboard')
#     else:
#         form = SignUpForm(request.POST)
#     context = {'form': form}
#     return render(request, 'accounts/register.html', context)



def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('You Have Edited Your Profiel...'))
            return redirect('accounts:dashboard')
    else:
        form = EditProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'accounts/edit_profile.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request,('You Have Edited Your Password...'))
            return redirect('accounts:dashboard')
    else:
        form = PasswordChangeForm(user=request.user)

    context = {'form': form}

    return render(request, 'accounts/change_password.html', context)



# ===========================
#      VIEWS KALALISO
#          START
# ===========================


# def image_upload_view(request, **kwargs):
#     form = ImageForm
#     if request.method == "POST":
#         form=ImageForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             obj=form.instance
#             return render(request, 'kalaliso/homepage.html', {'obj': obj})
#     else:
#         form = ImageForm()
#     img = Image.objects.all()
#     return render(request, 'kalaliso/homepage.html', {'img': img, 'form': form})

# def homepage(request,):
#     customer = Person.objects.count()
#     order_count = Order.objects.count()
#     product_count = Product.objects.count()
#
#     context = {
#         'customer': customer,
#         'order_count': order_count,
#         'product_count': product_count,
#     }
#     return render(request, 'accounts/homepage.html', context)




