from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
import io
# from reportlab.pdfgen import canvas
# from reportlab.lib.units import inch
# from reportlab.lib.pagesizes import letter, A8

import time
time.sleep(5)

from accounts.models import *
from .forms import *
# from django.contrib.gis.db import models Person

from django.template import context
from django.template import defaulttags
from  django.db.models import *
import datetime
from django.forms import ModelForm
from io import BytesIO
from django.template.loader import get_template, select_template
from django.views import View
from xhtml2pdf import pisa
from django.core.paginator import Paginator
from django.db.models import Q
import xhtml2pdf.default
from xhtml2pdf.util import getSize
# from . import views

def dashboard(request):
    return render(request, 'accounts/dashboard.html')


# def logout(request):
#     return redirect('accounts:dashboard')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You Have been Logged In !'))
            return redirect('accounts:dashboard')
        else:
            messages.success(request, ('Error you can try again !'))
            return redirect('accounts:login')
    else:
        return render(request, 'accounts/login.html', {})


def logout(request):
     messages.success(request, ('You Have Been Logged out...'))
     return redirect('accounts:login')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,('You Have Registered now...'))
            return redirect('accounts:dashboard')
    else:
        form = SignUpForm(request.POST)
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


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



# SEARCH NAME OR CONTACT PERSON IN DATABASE
# def search_person(request):
#     search = request.GET.get('search')
#     list_person = Person.objects.filter(Q(nom__icontains=search) |
#                                         Q(code_person__icontains=search) |
#                                         Q(prenom__icontains=search) |
#                                         Q(contact_1__icontains=search) |
#                                         Q(genre__icontains=search) |
#                                         Q(status__icontains=search)
#                                         )
#     person_number = list_person.count()
#     message = f' results : {person_number }'
#     if person_number == 1:
#           message = f' results : {person_number }'
#
#     context = {
#         'list_person': list_person,
#         'message': message
#     }
#     return render(request, 'kalaliso/search_person.html', context)




# BEGIN GENERATED PDF

# def report_person_pdf(request):
#     persons = Person.objects.all().order_by('-id')
#     template_path = 'kalaliso/xhtml2pdf/report_persons.html'
#     context = {'list_person': persons}
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'filename="report_person.pdf"'
#     template = get_template(template_path)
#     html = template.render(context)
#     pisa_status = pisa.CreatePDF(html, dest=response)
#
#     if pisa_status.err:
#         return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response

# END GENERATED PDF

# def show_video(request):
#     all_video=Video.objects.all()
#     if request.method == "POST":
#         form=Video_form(data=request.POST,files=request.FILES)
#         if form.is_valid():
#          form.save()
#         return HttpResponse("<h1> Uploaded successfully </h1>")
#     else:
#          form=Video_form()
#          return render(request, 'kalaliso/add_videos.html', {"form":form, "all":all_video})




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




