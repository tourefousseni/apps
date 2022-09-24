from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, A8
import time
# from xhtml2pdf import pisa
# from contacts.models import Mesure
from .models import *
from .forms import *
# from django.contrib.gis.db import models Mesure

# from django.views.generic import ListView, CreateView
from django.template import context
from django.template import defaulttags
from  django.db.models import *
import datetime
from django.forms import ModelForm
from io import BytesIO
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from reportlab.lib.utils import *

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

data = {
         "company": "Dennnis Ivanov Company",
         "address": "123 Street name",
         "city": "Vancouver",
         "state": "WA",
         "zipcode": "98663",

         "phone": "555-555-2345",
         "email": "youremail@dennisivy.com",
         "website": "dennisivy.com", }

# Opens up page as PDF
class ViewPDF(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('pdf/pdf_customer.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

# Automaticly downloads to PDF file
class DownloadPDF(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('app/pdf_customer.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Customer_%s.pdf" % ("12341231")
        content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response

    #END GENERATED PDF

def show_video(request):
    all_video=Video.objects.all()
    if request.method == "POST":
        form=Video_form(data=request.POST,files=request.FILES)
        if form.is_valid():
         form.save()
        return HttpResponse("<h1> Uploaded successfully </h1>")
    else:
         form=Video_form()
         return render(request,'kalaliso/add_videos.html',{"form":form,"all":all_video})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You Have been Logged In !'))
            return redirect('homepage')
        else:
            messages.success(request, ('Error you can try again !'))
            return redirect('login')
    else:
        return render(request, 'account/login.html', {})


def logout_user(request):
     logout(request)
     messages.success(request, ('You Have Been Logged out...'))
     return redirect('login')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,('You Have Registered now...'))
            return redirect('homepage')
    else:
        form = SignUpForm(request.POST)
    context = {'form': form}
    return render(request, 'account/register.html', context)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('You Have Edited Your Profiel...'))
            return redirect('homepage')
    else:
        form = EditProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'account/edit_profile.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request,('You Have Edited Your Password...'))
            return redirect('account/homepage.html')
    else:
        form = PasswordChangeForm(user=request.user)

    context = {'form': form}

    return render(request, 'account/change_password.html', context)



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

def homepage(request,):
    return render(request, 'kalaliso/homepage.html')

def person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('list')
    else:
       form=PersonForm()
    return render(request, 'kalaliso/person.html', {'form': form,})

def list(request):
    list_person = Person.objects.all()
    return render(request, 'kalaliso/person_list.html', {'list_person': list_person})

def detail_person(request, p_detail_id):
    detail_p = get_object_or_404(Person, pk=p_detail_id)
    # detail_p = Person.objects
    return render(request, 'kalaliso/d_person.html', {'detail_p': detail_p})

def user(request):
    user_list = User.objects
    return render(request, 'kalaliso/user_list.html', {'user_list':user_list})

# def detail_person(request, person_id):
#     detail = get_object_or_404(Person, pk=person_id)
#     return render(request, 'kalaliso/detail_person.html', {'detail': detail})

# def product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('order'))
#     else:
#        form = ProductForm()
#     return render(request, 'kalaliso/product.html', {'form': form})
def product(request):
    products = Product.objects
    return render(request, 'kalaliso/product.html', {'products':products})


def product_detail(request, product_id):
    product_detail = get_object_or_404(Product, pk=product_id)
    return render(request, 'kalaliso/product_detail.html', {'product_detail': product_detail,})


def product_sum(request):
    product_sum = Product.objects
    return render(request, 'kalaliso/product_count.html', {'product_sum': product_sum, } )


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

def order_items(request, ):
    if request.method == 'POST':
        form=Order_ItemsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('order_items'))
    else:
        form = Order_ItemsForm()
    return render(request, 'kalaliso/order_items.html', {'form': form})

def orderdetail_detail(request, orderdetail_id):

    qs = Order_Items.objects.all().order_by(Order)
    context = {'orderdetail': qs, }
    return render(request, 'kalaliso/orderdetail_detail.html', context)


def order_list(request, order_id):
    qs = Order.objects.all().order_by(-id)
    # qs = get_object_or_404(Order, pk=order_id)
    context = {'order_list': qs,}
    # return render(request, 'kalaliso/order_list.html', context)
    # return HttpResponse('order')
    return render(request, 'kalaliso/order_list.html', context)



def mesure(request):
    if request.method == 'POST':
        form = MesureForm(request.POST)
        if form.is_valid():
             form.save()
             return HttpResponseRedirect('mesure_list')
    else:
       form = MesureForm()
    return render(request, 'kalaliso/mesure.html', {'form': form})

# research for OVER STACK FLOW this Bug
# response = wrapped_callback(request, *callback_args, **callback_kwargs)


def mesure_list(request):
    qs = Mesure.objects
    return render(request, 'kalaliso/mesure_list.html', {'mesure_list': qs,})


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



def maps(request, ):
    return render(request, 'maps/maps.html',)


def region(request):
    if request.method == 'POST':
        form = RegionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('cercle')
    else:
            form = RegionForm()
    return render(request, 'localisation/region.html', {'form': form})

def cercle(request):
    if request.method == 'POST':
        form = CercleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('commune')
    else:
        form = CercleForm()
    return render(request, 'localisation/cercle.html', {'form': form})

def commune(request):
    if request.method == 'POST':
        form = CommuneForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('village')
    else:
        form = CommuneForm()
    return render(request, 'localisation/commune.html', {'form': form})

def village(request):
    if request.method == 'POST':
        form = VillageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('village'))
    else:
        form = VillageForm()
    return render(request, 'localisation/village.html', {'form': form})


def profile(request):
    return render(request, 'kalaliso/profile.html', {})

# ===========================
#      VIEWS KALALISO
#          END
# ===========================


def n_customers(request):
    customer = Person.objects.count()
    context = {'customer': customer, }
    return render(request, 'kalaliso/homepage.html', context)

def n_orders(request):
    order_count = Order.objects.count()
    context = {'order_count': order_count, }
    return render(request, 'kalaliso/homepage.html', context)

def n_products(request):
    product_count = Product.objects.count()
    context = {'product_count': product_count, }
    return render(request, 'kalaliso/homepage.html', context)


def report_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A8, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 10)
   # Designate The Model

    qs = Mesure.objects.all()
    # create blank list
    lines = []
    for mesure in qs:
        lines.append(mesure.id)
        lines.append(mesure.person_mesure)
        lines.append(mesure.coude)
        lines.append(mesure.epaule)
        lines.append(mesure.manche)
        lines.append(mesure.tour_manche)
        lines.append(mesure.taille)
        lines.append(mesure.poitrine)
        lines.append(mesure.longueur_boubou)
        lines.append(mesure.longueur_patanlon)
        lines.append(mesure.fesse)
        lines.append(mesure.ceinture)
        lines.append(mesure.cuisse)
        lines.append(mesure.patte)
        lines.append(mesure.created_at)
        lines.append(mesure.update_at)
        lines.append('=================')
    # for loop
    for line in lines:
        textob.textLine(line)
    # Finish Up
        c.drawText(textob)
        c.showPage()
        c.save()
        buf.seek(0)
    return FileResponse(buf,  as_attachment=True, filename="carnet_mesure_pdf")


def person_filter(request):
    p_f = Person.objects.filter(code_person="")
    return p_f
