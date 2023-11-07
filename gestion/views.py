import io
import time
import uuid
time.sleep(5)
from django.urls import reverse_lazy
from django.urls import reverse
from .forms import *
from accounts.models import *
from gestion.models import *
from contacts.models import *
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from django.template import context
from django.template import defaulttags
from django.db.models import *
from django.conf import settings
import datetime
from django.forms import ModelForm
from io import BytesIO
from django.template.loader import get_template, select_template
# from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from django.core.paginator import Paginator
from django.db.models import Q
import xhtml2pdf.default
from xhtml2pdf.util import getSize
from paypal.standard.forms import PayPalPaymentsForm


# from .forms import PaymentForm, OrderForm, Order_ItemsForm

def gestion(request):
    if request.method == 'POST':
        form = GestionForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success( f'votre registrement est fait avec succes !')
            # return HttpResponse('mesure_list')
            # return redirect('/')
            messages.success(request, 'Les donnees sont registrées avec succès !')
            return redirect('gestion:gestion')
    else:
        form = GestionForm()
        # form = PersonForm()
    return render(request, 'gestion/html/mesure.html', {'form': form, })


def list(request, *args, **kwargs):
    list_gest  = Gestion.objects.all().order_by('-id')
    paginator    = Paginator(list_gest, 5)
    page_number  = request.GET.get('page')
    page_obj     = paginator.get_page(page_number)
    person_number= list_gest.count()

    message = f'{person_number} Nombre:'
    if page_number == 1:
            message   = f'{page_number} Nombre :'

    context = {
        'list_gest': page_obj,
        'person_number': person_number,
        'message': message,
    }
    return render(request, 'gestion/html/list.html', context)


def detail(request, id):
    detail_view = Gestion.objects.get(pk=id)
    context = {
        'gestion': detail_view,
    }
    return render(request, 'gestion/html/gestion_detail.html', context)


def update_mesure(request, id):
    mesure       = Gestion.objects.get(id=id)
    form         = GestionForm(instance=mesure)
    if request.method == 'POST':
        form     = GestionForm(request.POST, instance=gestion)
        if form.is_valid():
            form.save()
    context      = {'form':form }
    return render(request, 'gestion/html/mesure.html', context)

def update(request, id):
    update_gest = Gestion.objects.get(pk=id)
    obj           = Person.objects.get(pk=id)
    context       = {
        'update_gest': update_gest,
        'obj': obj,
    }
    return render(request, 'gestion/html/list.html', context)

def delete_mesure(request, id):
    gestion = Gestion.objects.get(id=id)
    if request.method == 'POST':
        gestion.delete()
        return redirect('gestion:list')
    context = { 'gestion': gestion }
    return render(request, 'gestion/html/delete_gestion.html', context)

def report_carnet(request, id):
    detail_view = Gestion.objects.get(id=id)
    template_path = 'gestion/xhtml2pdf/report_carnet_gestion.html'
    context = { 'gestion': detail_view,}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="carnet_gestion.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    status = pisa.CreatePDF(html, dest=response)

    if status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def report_all_mesure(request):
    page_obj = Gestion.objects.all()
    template_path = 'gestion/xhtml2pdf/report_all_gestions.html'
    context = {'list_gest': page_obj,}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report_all_gestions.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    status = pisa.CreatePDF(html, dest=response)

    if status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def search_products_list(request):
    search = request.GET.get('search')
    search_products = Product.objects.filter(
        Q(code_product__contains=search) |
        Q(price__icontains=search) |
        Q(name__icontains=search) |
        Q(description__icontains=search) |
        Q(create_at__icontains=search)
    )
    search_products_list = search_products.count()
    message = f' results : {search_products}'
    if search_products == 1:
        message = f' results : {search_products}'

    context = {
        'search_products_list': search_products_list,
        'message': message
    }
    return render(request, 'gestion/html/search_products_list.html', context)


# def report_mesure(request):
#     mesure_detail = Mesure.objects.get(pk=id)
#     list_person = Person.objects.get(pk=id)
#     context = {
#         'mesure_detail': mesure_detail,
#         'list_person': list_person,
#     }
#     return render(request, 'gestion/gestion_detail.html', context)

def report_mesure(request):
    gestions = Gestion.objects.all().order_by('id')
    template_path = 'gestion/xhtml2pdf/report_mesure.html'
    context = {'list_gest': page_obj}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report_gestion.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    status = pisa.CreatePDF(html, dest=response)

    if status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def carnet(request, id):
    mesure = Gestion.objects.get(pk=id)
    # list_person = Person.objects.get(pk=id)

    template_path = 'gestion/xhtml2pdf/carnet_mesure.html'
    context = {
        'mesure_list': mesure,
        # 'person': list_person
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="carnet.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    status = pisa.CreatePDF(html, dest=response)

    if status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def search_mesure(request):
    search = request.GET.get('search')
    filter_data = Gestion.objects.filter(Q(coude__icontains=search)|
                                          Q(epaule__icontains=search)|
                                          Q(poitrine__icontains=search)
    )
    person_number = filter_data.count()
    message = f' results : {filter_data }'
    if person_number == 1:
          message = f' results : {filter_data }'

    context = {
        'filter_data': filter_data,
        'message': message
    }
    return render(request, 'gestion/html/search_mesure.html', context)


# def mesure_custom(request, mesure_id,):
#     qs = Mesure.objects.get(pk=mesure_id)
#     context = {
#         'mesure_list': qs, }
#     return render(request, 'gestion/mesure_custom.html', context)

def album(request):
    album = Album.objects.all()

    context = {
        'img': album,
    }
    return render(request, 'gestion/html/album.html', context)


# def annonce(request):
#     annonce = Annonce.objects.all()
#
#     context = {
#         'ann': annonce,
#     }
#     return render(request, 'gestion/annonce.html', context)


# def list(request):
#     list_person = Person.objects.all().order_by('id')
#     return render(request, 'gestion/person_list.html', {'list_person': list_person})


# def detail_person(request, person_id):
#
#     list_person = Person.objects.filter(pk=person_id)
#     context = {
#         'list_person': list_person,
#     }
#
#     return render(request, 'gestion/detail_person.html', context)
#     # return render(request, 'gestion/d_person.html', context)
#

def report_person_id_pdf(request, person_id):
    list_person = Person.objects.filter(pk=person_id)
    # persons = Person.objects.all().order_by('-id')
    template_path = 'gestion/xhtml2pdf/info_person.html'
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
    template_path = 'gestion/xhtml2pdf/report_order.html'
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
#     return render(request, 'gestion/person_list.html', context)

# def paginator_list_mesure(request):
#     list_mesure = Mesure.objects.all().order_by('id')
#     paginator = Paginator(list_mesure, 5)
#     page_number = request.GET.get('page')
#     page_object = paginator.get_page(page_number)
#     person_number = list_mesure.count()
#     message = f'{person_number} Nombre:'
#     if page_number == 1:
#         message = f'{page_number} Nombre :'
#     context = {
#         'list_mesure': page_object,
#         'person_number': person_number,
#         'message': message,
#     }
#     return render(request, 'gestion/paginators/list_mesure_paginator.html', context)
#     # return render(request, 'gestion/person_list.html', context)


# def info_person(request, id):
#     x = Person.objects.get(id=id)
#     context = {
#         'list_person': x
#     }
#     return render(request, 'gestion/info_person.html', context)


def user(request):
    user_list = User.objects
    return render(request, 'gestion/html/user_list.html', {'user_list': user_list})


# def detail_person(request, person_id):
#     detail = get_object_or_404(Person, pk=person_id)
#     return render(request, 'gestion/detail_person.html', {'detail': detail})

def product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('order'))
    else:
        form = ProductForm()
    return render(request, 'gestion/html/product.html', {'form': form})


def products_list(request):
    product = Product.objects.all().order_by('-id')

    context = {
        'list': product,
    }
    return render(request, 'gestion/html/products_list.html', context)


def product_detail(request, product_id):
    product_detail = get_object_or_404(Product, pk=product_id)
    return render(request, 'gestion/html/product_detail.html', {'product_detail': product_detail, })


def product_sum(request):
    product_sum = Product.objects
    return render(request, 'gestion/html/product_count.html', {'product_sum': product_sum, })


# def order(request):
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('gestion:order_list')
#             # return HttpResponse('order')
#     else:
#         form = OrderForm()
#     return render(request, 'gestion/order.html', {'form': form})

def order(request):
    if request.method == 'POST':
        form1 = OrderForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('gestion:order_list')
    else:
        form1 = OrderForm()
            # return HttpResponse('order')

    if request.method=='POST':
        form =Order_ItemsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion:order')
    else:
        form = Order_ItemsForm()

    return render(request, 'gestion/html/order.html', {'form1': form1, 'form':form})


def order_list(request):
    o_l = Order.objects.all()

    context = {
        'order_list': o_l
    }
    return render(request, 'gestion/html/order_list.html', context)


def order_items(request, ):
    if request.method == 'POST':
        form = Order_ItemsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion:order_list')
            # return HttpResponseRedirect(reverse('order_items'))
    else:
        form = Order_ItemsForm()
    # return render(request, 'gestion/order.html', {'form': form})
    return render(request, 'gestion/html/order_items.html', {'form': form})


def orderdetail_detail(request, ):
    qs = Order_Items.objects.all().order_by(Order)
    context = {'orderdetail': qs, }
    return render(request, 'gestion/html/orderdetail_detail.html', context)


# def order_list(request, order_id):
#     # qs = Order.objects.all().order_by(-id)
#     qs = get_object_or_404(Order, pk=order_id)
#     context = {'order_list': qs,}
#     # return render(request, 'gestion/order_list.html', context)
#     # return HttpResponse('order')
#     return render(request, 'gestion/order_list.html', context)

# research for OVER STACK FLOW this Bug
# response = wrapped_callback(request, *callback_args, **callback_kwargs)

def payment(request, ):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:homepage')
    else:
        form = PaymentForm()
    return render(request, 'gestion/html/payment.html', {'form': form})


def payment_list(request, payment_id):
    qs = Payment.objects.all(id=payment_id)

    context = {'payment_list': qs, }

    return render(request, 'gestion/html/payment_list.html', context)


def profile(request):
    # id,  *args,  **kwargs
    # list_person  = Person.objects.get(id=id)
    list_person = Person.objects.all().order_by('-id')

    context = {
        'list_person': list_person,
    }
    return render(request, 'gestion/html/profile.html', context)


def show_video(request):
    all_video = Video.objects.all()
    if request.method == "POST":
        form = Video_form(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponse("<h1> Uploaded successfully </h1>")
    else:
        form = Video_form()
        return render(request, 'gestion/html/add_videos.html', {"form": form, "all": all_video})


def home(request):
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '20.00',
        'item_name': 'Product 1',
        'invoice': str(uuid.uuid4()),
        'currency_code': 'USD',
        'notify_url': f'http://{host}{reverse("paypal-ipn")}',
        'return_url': f'http://{host}{reverse("gestion:paypal_return")}',
        'cancel_return': f'http://{host}{reverse("gestion:paypal_cancel")}',

    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {'form': form}
    return render(request, 'gestion/html/home.html', context)


def paypal_return(request):
    messages.error(request, 'you order has canceled !')
    return redirect(request, 'home')


def paypal_cancel(request):
    messages.error(request, 'you order has canceled !')
    return redirect(request, 'home')


def depense(request, ):
    if request.method == 'POST':
        form = DepenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion:annonce')
    else:
        form = DepenseForm()
    return render(request, 'gestion/html/depense.html', {'form': form})

def anonce(request,):
    if request.method == 'POST':
        form = AnonceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion:annonce')
    else:
        form = AnonceForm()
    return render(request, 'gestion/html/annonce.html', {'form': form})

# ===========================
#      VIEWS KALALISO
#          END
# ===========================
