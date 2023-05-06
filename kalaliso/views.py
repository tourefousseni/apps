import io
import time
import uuid
time.sleep(5)
from django.urls import reverse_lazy
from django.urls import reverse
from .forms import *
from accounts.models import *
from kalaliso.models import *
from contacts.models import *
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
# from django.contrib.gis.db import models Person
from django.template import context
from django.template import defaulttags
from  django.db.models import *
from django.conf import settings
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
from paypal.standard.forms import PayPalPaymentsForm

def mesure(request):
    if request.method == 'POST':
        form = MesureForm(request.POST)
        if form.is_valid():
             form.save()
             # return HttpResponse('mesure_list')
             # return redirect('/')
             return redirect('kalaliso:list')
    else:
       form = MesureForm()
       # form = PersonForm()
    return render(request, 'kalaliso/mesure.html', {'form': form})

def list(request):
    list_mesure = Mesure.objects.all().order_by('-id')
    obj = Person.objects.all()
    context = {
        'list_mesure': list_mesure,
        'obj': obj,
    }
    return render(request, 'kalaliso/list.html', context)

def detail(request, id):
    mesure_detail = Mesure.objects.get(pk=id)
    list_person = Person.objects.get(pk=id)
    context = {
        'mesure_detail': mesure_detail,
        'list_person': list_person,
    }
    return render(request, 'kalaliso/mesure_detail.html', context)

def update(request, id):
    update_mesure = Mesure.objects.get(pk=id)
    obj = Person.objects.get(pk=id)
    context = {
        'update_mesure': update_mesure,
        'obj': obj,
    }
    return render(request, 'kalaliso/list.html', context)

# def report_mesure(request):
#     mesure_detail = Mesure.objects.get(pk=id)
#     list_person = Person.objects.get(pk=id)
#     context = {
#         'mesure_detail': mesure_detail,
#         'list_person': list_person,
#     }
#     return render(request, 'kalaliso/mesure_detail.html', context)

def report_mesure(request):
    mesures = Mesure.objects.all().order_by('id')
    template_path = 'kalaliso/xhtml2pdf/report_mesure.html'
    context = {'mesure_list': mesures}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report_mesure.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    status = pisa.CreatePDF(html, dest=response)

    if status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def search_mesure(request):
    search = request.GET.get('search')
    filter_mesure = Mesure.objects.filter(Q(coude__icontains=search))
                                          # |
                                          # Q(epaule__icontains=search))
    # person_number = list_person.count()
    # message = f' results : {person_number }'
    # if person_number == 1:
    #       message = f' results : {person_number }'

    context = {
        'filter_mesure': filter_mesure,
        # 'message': message
    }
    return render(request, 'kalaliso/search_mesure.html', context)

# def mesure_custom(request, mesure_id,):
#     qs = Mesure.objects.get(pk=mesure_id)
#     context = {
#         'mesure_list': qs, }
#     return render(request, 'kalaliso/mesure_custom.html', context)

def album(request):
    album = Album.objects.all()

    context = {
        'img': album,
    }
    return render(request, 'kalaliso/album.html', context)

def annonce(request):
    annonce = Annonce.objects.all()

    context = {
        'ann': annonce,
    }
    return render(request, 'kalaliso/annonce.html', context)



# def list(request):
#     list_person = Person.objects.all().order_by('id')
#     return render(request, 'kalaliso/person_list.html', {'list_person': list_person})


# def detail_person(request, person_id):
#
#     list_person = Person.objects.filter(pk=person_id)
#     context = {
#         'list_person': list_person,
#     }
#
#     return render(request, 'kalaliso/detail_person.html', context)
#     # return render(request, 'kalaliso/d_person.html', context)
#

def report_person_id_pdf(request, person_id):
    list_person = Person.objects.filter(pk=person_id)
    # persons = Person.objects.all().order_by('-id')
    template_path = 'kalaliso/xhtml2pdf/info_person.html'
    context = {'list_person': list_person}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report_person_id.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    status = pisa.CreatePDF(html, dest=response)

    if status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def report_order_pdf(request, order_id):
    order = Order.objects.filter(pk=order_id)
    # persons = Person.objects.all().order_by('-id')
    template_path = 'kalaliso/xhtml2pdf/report_order.html'
    context = {'order': order}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report_order.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    status = pisa.CreatePDF(html, dest=response)

    if status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



# def list(request):
#     list_person = Person.objects.all().order_by('-id')
#     paginator   = Paginator(list_person, 10)
#     page_number = request.GET.get('page')
#     page_object = paginator.get_page(page_number)
#     person_number = list_person.count()
#
#     message = f'{person_number } person :'
#     context = {
#         'list_person': page_object,
#         'message': message,
#     }
#     return render(request, 'kalaliso/person_list.html', context)

def paginator_list_mesure(request):
    list_mesure     = Mesure.objects.all().order_by('id')
    paginator       = Paginator(list_mesure, 5)
    page_number     = request.GET.get('page')
    page_object     = paginator.get_page(page_number)
    person_number   = list_mesure.count()
    message         = f'{ person_number } Nombre:'
    if page_number  ==1:
       message      = f'{ page_number } Nombre :'
    context = {
        'list_mesure': page_object,
        'person_number': person_number,
        'message': message,
    }
    return render(request, 'kalaliso/paginators/list_mesure_paginator.html', context)
    # return render(request, 'kalaliso/person_list.html', context)

# def info_person(request, id):
#     x = Person.objects.get(id=id)
#     context = {
#         'list_person': x
#     }
#     return render(request, 'kalaliso/info_person.html', context)


def user(request):
    user_list = User.objects
    return render(request, 'kalaliso/user_list.html', {'user_list':user_list})

# def detail_person(request, person_id):
#     detail = get_object_or_404(Person, pk=person_id)
#     return render(request, 'kalaliso/detail_person.html', {'detail': detail})

def product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('order'))
    else:
       form = ProductForm()
    return render(request, 'kalaliso/product.html', {'form': form})


def products_list(request):
    product = Product.objects.all().order_by('-id')

    context = {
        'list': product,
    }
    return render(request, 'kalaliso/products_list.html', context)


def product_detail(request, product_id):
    product_detail = get_object_or_404(Product, pk=product_id)
    return render(request, 'kalaliso/product_detail.html', {'product_detail': product_detail, })


def product_sum(request):
    product_sum = Product.objects
    return render(request, 'kalaliso/product_count.html', {'product_sum': product_sum, })


def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return render('kalaliso/order.html')
            # return HttpResponse('order')
    else:
        form=OrderForm()
    return render(request, 'kalaliso/order.html', {'form': form})


def order_list(request):
    o_l = Order.objects.all()

    context = {
        'order_list': o_l
    }
    return render(request, 'kalaliso/order_list.html', context)

def order_items(request, ):
    if request.method == 'POST':
        form=Order_ItemsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('order'))
            # return HttpResponseRedirect(reverse('order_items'))
    else:
        form = Order_ItemsForm()
    return render(request, 'kalaliso/order.html', {'form': form})
    # return render(request, 'kalaliso/order_items.html', {'form': form})

def orderdetail_detail(request,):

    qs = Order_Items.objects.all().order_by(Order)
    context = {'orderdetail': qs, }
    return render(request, 'kalaliso/orderdetail_detail.html', context)


# def order_list(request, order_id):
#     # qs = Order.objects.all().order_by(-id)
#     qs = get_object_or_404(Order, pk=order_id)
#     context = {'order_list': qs,}
#     # return render(request, 'kalaliso/order_list.html', context)
#     # return HttpResponse('order')
#     return render(request, 'kalaliso/order_list.html', context)

# research for OVER STACK FLOW this Bug
# response = wrapped_callback(request, *callback_args, **callback_kwargs)

def payment(request,):
        if request.method == 'POST':
          form = PaymentForm(request.POST)
          if form.is_valid():
              form.save()
              return HttpResponseRedirect(reverse('Order'))
        else:
            form = PaymentForm()
        return render(request, 'kalaliso/payment.html', {'form': form})

def payment_list(request, payment_id):
    qs = Payment.objects.all()

    context = {'payment_list': qs, }

    return render(request, 'kalaliso/payment_list.html', context)

def profile(request):
    #id,  *args,  **kwargs
    # list_person  = Person.objects.get(id=id)
    list_person  = Person.objects.all().order_by('-id')

    context = {
        'list_person': list_person,
    }
    return render(request, 'kalaliso/profile.html', context)

def show_video(request):
    all_video=Video.objects.all()
    if request.method == "POST":
        form=Video_form(data=request.POST,files=request.FILES)
        if form.is_valid():
         form.save()
        return HttpResponse("<h1> Uploaded successfully </h1>")
    else:
         form=Video_form()
         return render(request, 'kalaliso/add_videos.html', {"form":form, "all":all_video})

def home(request):
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '20.00',
        'item_name': 'Product 1',
        'invoice': str(uuid.uuid4()),
        'currency_code': 'USD',
        'notify_url': f'http://{host}{reverse("paypal-ipn")}',
        'return_url': f'http://{host}{reverse("kalaliso:paypal_return")}',
        'cancel_return': f'http://{host}{reverse("kalaliso:paypal_cancel")}',

    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    context={'form':form}
    return render(request, 'kalaliso/home.html', context)

def  paypal_return(request):
    messages.error(request, 'you order has canceled !')
    return redirect(request, 'home')

def  paypal_cancel(request):
    messages.error(request, 'you order has canceled !')
    return redirect(request, 'home')

# ===========================
#      VIEWS KALALISO
#          END
# ===========================

