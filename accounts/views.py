from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth import authenticate, login, get_user_model, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, LoginForm
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from .forms import UserRegistrationForm, LoginForm
import io
from .import views
from contacts.models import Person
import time
time.sleep(5)

from accounts.models import User
from .forms import *

def dashboard(request):
    person = Person.objects.count()
    context={
        'person': person,

         }
    return render(request, 'accounts/dashboard.html', context)

def homepage(request):
    return render(request, 'accounts/homepage.html')

def register(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "votre compte a ete bien cree")
            return redirect('accounts:connect')
    else:
        form = UserRegistrationForm()
        # messages.info(request, ("la creation de votre compte est echouee"))
    return render(request, 'accounts/register.html', {'form':form})
def connect(request):
    form = LoginForm(request.POST)
    if form.is_valid():
         username   = form.cleaned_data["username"]
         # email      = form.cleaned_data["email"]
         password   = form.cleaned_data["password"]
         user       = authenticate(username=username,  password=password)

         if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('accounts:dashboard')
            else:
                return redirect('accounts:dashboard')

    return render(request, "registration/login.html", {'form': form})

# def connect(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = auth.authenticate(request, username=username, email=email,password=password)
#         # first_name  = request.POST['first_name']
#         # last_name   = request.POST['last_name']
#         # username    = request.POST.get('username')
#         # phone       = request.POST['phone']
#         # email       = request.POST.get('email')
#         # password    = request.POST.get('password')
#         # password2   = request.POST['password2']
#         # user = auth.authenticate(username=username, password=password)
#         # user = authenticate(
#         # user = auth.authenticate(
#                             # request,
#                             # first_name=first_name,
#                             # last_name=last_name,
#                             # username=username,
#                             # phone=phone,
#                             # email=email,
#                             # password=password,
#                             # password2=password2
#                             # )
#         # and user.is_active
#         if user is not None:
#             if  user.is_active:
#              auth.login(request, user)
#              messages.success(request, ('Bienvenue vous etes connecté avec succés'))
#             return redirect('accounts:dashboard')
#         if password !=password:
#             messages.warning(request, ('votre mot de passe est different'))
#             return redirect('accounts:connect')
#
#         if email != email:
#             messages.warning(request, ('votre email est different'))
#             return redirect('accounts:connect')
#
#         if username !=username:
#             messages.warning(request, ('votre username est different'))
#             return redirect('accounts:connect')
#
#         else:
#             messages.success(request, ('Il faut refaire pour connecter'))
#             return redirect('accounts:dashboard')
#     else:
#         return render(request, 'registration/login.html')





# @login_required
def disconnect(request):
    logout(request)
    # messages.info(request, ("vous etes deconnecte sur le site"))
    return redirect('accounts:homepage')

     # # return redirect('accounts:homepage')
     # messages.success(request, 'vous etes deconnecte')


# def EditProfileForm(POST, instance):
#     pass


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
#             return render(request, 'gestion/homepage.html', {'obj': obj})
#     else:
#         form = ImageForm()
#     img = Image.objects.all()
#     return render(request, 'gestion/homepage.html', {'img': img, 'form': form})

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




