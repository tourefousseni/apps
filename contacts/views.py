# import hashlib
from math import sin, cos, tan, pi, ceil
# from reportlab import rl_config, ascii, xrange
from reportlab.pdfbase import pdfutils
from reportlab.pdfbase import pdfdoc
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen  import pdfgeom, pathobject
from reportlab.lib.utils import import_zlib, ImageReader, isSeq, isStr, isUnicode, _digester
from reportlab.lib.rl_accel import fp_str, escapePDF
from reportlab.lib.boxstuff import aspectRatioFix
from reportlab.pdfgen import canvas
from reportlab.platypus import Table
from django.http import FileResponse
import io
# import reportlab.pdfgen
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, A5
from reportlab.pdfgen import canvas
# import genHeaderTable
# import genBodyTable
# import genFooterTable
# import reportlab genFooterTable, genBodyTable, genHeaderTable
# from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table
# from .forms import UploadFileForm
from django.shortcuts import render
from django.urls import reverse
from django.template import context
from contacts.models import Contact
# from .forms import UploadFileForm
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from django.template import context
from django.template import defaulttags
from contacts.models import Contact, Parcel, Person, Mesure, Order, Product, Payment, OrderDetail
from .forms import SignUpForm, \
                   EditProfileForm, \
                   ContactForm, \
                   ParcelForm, \
                   PersonForm,\
                   MesureForm,\
                   ProductForm,\
                   OrderForm, \
                   PaymentForm, \
                   OrderDetailForm

def home(request):
    return render(request, 'contacts/home.html', {})



# ==============================================
#                  VIEWS CADASTRE
#                        START
# ==============================================


def contact(request):

    if request.method == 'POST':

        sta = request.POST.get('status')
        sx = request.POST.get('sexe')
        no = request.POST.get('nom')
        pre = request.POST.get('prenom')
        mle = request.POST.get('matricule')
        cont = request.POST.get('contact')
        cin = request.POST.get('n_cin')
        ni = request.POST.get('nina')
        prof = request.POST.get('profession')
        rci = request.POST.get('rcimm')
        nf = request.POST.get('nif')
        s_s = request.POST.get('siege_social')
        res = request.POST.get('responsable')
        ema = request.POST.get('email')
        cre = request.POST.get('created_at')

        data = Contact(status=sta,
                       sexe=sx,
                       nom=no,
                       prenom=pre,
                       matricule=mle,
                       contact=cont,
                       n_cin=cin,
                       nina=ni,
                       profession=prof,
                       rcimm=rci,
                       nif=nf,
                       siege_social=s_s,
                       responsable=res,
                       email=ema,
                       created_at=cre)

        data.save()

        return HttpResponseRedirect(reverse('parcel'))
    else:
        blog = ContactForm()
    return render(request, 'contacts/contacts.html', {'form': blog})


def contact_detail(request, contact_id):
        qs = Contact.objects.all()
        context = {'contacts': qs,}

        return render(request, 'contacts/contacts_detail.html', context)


def parcel(request):

    if request.method == 'POST':
        nat = request.POST.get('nature')
        sup = request.POST.get('superficie')
        pe = request.POST.get('perimeter')
        cod = request.POST.get('code')
        cre = request.POST.get('created_at')
        upd = request.POST.get('update_at')

        data = Parcel(
                      nature=nat,
                      superficie=sup,
                      perimeter=pe,
                      code=cod,
                      created_at=cre,
                      update_at=upd,)
        data.save()

        return HttpResponseRedirect(reverse('home'))
    else:
        blog = ParcelForm()
    return render(request, 'contacts/parcel.html', {'form': blog})


def parcel_detail(request, parcel_id):
    qs = Parcel.objects.all()
    context = {'detenteur': qs,}

    return render(request, 'contacts/parcel_detail.html', context)

# GENERATED FILE PROFIL PDF

def profil_pdf(request,):
    # create Bytestream buffer
    buf = io.BytesIO()
    # Create a Canvas
    p = canvas.Canvas(buf,  pagesize=A5, bottomup=0)
    #Create a text object
    textob = p.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica', 14)

    contacts = Contact.objects.all()
    # Loop
    lines = []
    for contact in contacts:
        lines.append(contact.status)
        lines.append(contact.sexe)
        lines.append(contact.nom)
        lines.append(contact.prenom)
        lines.append(contact.matricule)
        lines.append(contact.contact)
        lines.append('===============')

    for line in lines:
        textob.textLine(line)
    # Finish Up
    p.drawText(textob)
    p.showPage()
    p.save()
    buf.seek(0)

    # Return something

    return FileResponse(buf, as_attachment=True, filename='profil.pdf')

    # context = {'contacts': ps,}

    # return render(request, 'contacts/profil.html', context)

#
# def fiche(request):
#     return None

# ==============================================
#                  VIEWS CADASTRE
#                        END
# ==============================================


def about(request):
    return render(request, 'contacts/about.html', {})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You Have been Logged In !'))
            return redirect('home')
        else:
            messages.success(request, ('Error you can try again !'))
            return redirect('login')
    else:
        return render(request, 'contacts/login.html', {})


def logout_user(request):
     logout(request)
     messages.success(request, ('You Have Been Logged out...'))
     return redirect('home')


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
            return redirect('home')
    else:
        form = SignUpForm(request.POST)
    context = {'form': form}
    return render(request, 'contacts/register.html', context)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('You Have Edited Your Profiel...'))
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)
        context = {'form': form}
    return render(request, 'contacts/edit_profile.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request,('You Have Edited Your Password...'))
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)

    context = {'form': form}

    return render(request, 'contacts/change_password.html', context)


# ===========================
#      VIEWS KALALISO
#          START
# ===========================


def homepage(request):
    return render(request, 'kalaliso/homepage.html')


def product(request):
    if request.method == 'POST':
            pri = request.POST.get("price")
            na = request.POST.get("name")
            cod = request.POST.get("code_product")
            des = request.POST.get("description")
            ph = request.POST.get("photo")
            dat = request.POST.get("create_at")

            data = Product(
                           price=pri,
                           name=na,
                           code_product=cod,
                           description=des,
                           photo=ph,
                           create_at=dat)
            data.save()

            return HttpResponseRedirect(reverse('order'))
    else:
        form = ProductForm()
    return render(request, 'kalaliso/product.html', {'form': form})


def product_detail(request, product_id):
    qs = Product.objects.all()
    context = {'product': qs,}

    return render(request, 'kalaliso/product_detail.html', context)


def order(request):
    if request.method == 'POST':
            ida = request.POST.get("id")
            cd = request.POST.get("code_order")
            recep = request.POST.get("reception")
            creat = request.POST.get("create_at")
            data = Order(id=ida,
                         code_order=cd,
                         reception=recep,
                         create_at=creat,)
            data.save()

            return HttpResponseRedirect(reverse('order_detail'))
    else:
        form = OrderForm()
    return render(request, 'kalaliso/order.html', {'form': form})


def order_detail(request, order_id):
    qs = Order.objects.all()

    context = {'detail_order': qs,}

    return render(request, 'kalaliso/order_detail.html', context)

def orderdetail(request):
    if request.method == 'POST':
        ca = request.POST.get("category")
        qt = request.POST.get("quantity")
        tv = request.POST.get("tva")
        rm = request.POST.get("remise")
        creat = request.POST.get("create_at")

        data = OrderDetail(
                           category=ca,
                           remise=rm,
                           quantity=qt,
                           tva=tv,
                           create_at=creat,)
        data.save()
        return HttpResponseRedirect(reverse('orderdetail'))
    else:
        form = OrderDetailForm()
    return render(request, 'kalaliso/orderdetail.html', {'form': form})
#
#
def orderdetail_detail(request, orderdetail_id):

    qs = OrderDetail.objects.all()
    context = {'orderdetail': qs, }

    return render(request, 'kalaliso/orderdetail_detail.html', context)

def mesure(request, *args, **kwargs):
    if request.method == 'POST':
            id = request.POST.get("id")
            coud = request.POST.get("coude")
            epau = request.POST.get("epaule")
            ma = request.POST.get("manche")
            to_ma = request.POST.get("tour_manche")
            tail = request.POST.get("taille")
            poitr = request.POST.get("pointrine")
            lo_bo = request.POST.get("longueur_boubou")
            lo_pa = request.POST.get("longueur_patanlon")
            fes = request.POST.get("fesse")
            cei = request.POST.get("ceinture")
            cui = request.POST.get("cuisse")
            pat = request.POST.get("patte")
            cre = request.POST.get('created_at')
            upd = request.POST.get('update_at')
            pmid = request.POST.get('person_mesure_id')

            data = Mesure(id=id,
                          coude=coud,
                          epaule=epau,
                          manche=ma,
                          tour_manche=to_ma,
                          taille=tail,
                          poitrine=poitr,
                          longueur_boubou=lo_bo,
                          longueur_patanlon=lo_pa,
                          fesse=fes,
                          ceinture=cei,
                          cuisse=cui,
                          patte=pat,
                          update_at=upd,
                          created_at=cre,
                          person_mesure_id=pmid,
                          )
            data.save()
            return HttpResponseRedirect(reverse('Order'))
    else:
       form = MesureForm()
    return render(request, 'kalaliso/mesure.html', {'form': form})


def mesure_detail(request, mesure_id):
    qs = Mesure.objects.all()

    context = {'detail_mesure': qs,}

    return render(request, 'kalaliso/mesure_detail.html', context)


def person(request):
    if request.method == 'POST':
            sta = request.POST.get("status")
            se = request.POST.get("sex")
            cat = request.POST.get("category")
            pre = request.POST.get("prenom")
            no = request.POST.get("nom")
            cont = request.POST.get("contact_1")
            # cin = request.POST.get("n_cin")
            nn = request.POST.get("nina")
            prf = request.POST.get("profession")
            nat = request.POST.get("nationalite")
            # n_f = request.POST.get("n")
            # ss = request.POST.get("siege_social")
            # resp = request.POST.get("responsable")
            # ema = request.POST.get("email")
            cret = request.POST.get('created_at')

            data = Person(status=sta,
                          prenom=pre,
                          nom=no,
                          sex=se,
                          category=cat,
                          contact_1=cont,
                          # n_cin=cin,
                          nina=nn,
                          profession=prf,
                          nationalite=nat,
                          # n=n_f,
                          # siege_social=ss,
                          # responsable=resp,
                          # email=ema,
                          created_at=cret)
            data.save()

            return HttpResponseRedirect(reverse('mesure'))
    else:
        form = PersonForm()
    return render(request, 'kalaliso/person.html', {'form': form})


def person_detail(request, person_id):
    qs = Person.objects.all()

    context = {'detail_person': qs,}

    return render(request, 'kalaliso/person_detail.html', context)



def payment(request,):
        if request.method == 'POST':
            subm = request.POST.get("submontant")
            rm = request.POST.get("remise")
            tv = request.POST.get("tva")
            mt = request.POST.get("montant_total")
            rd = request.POST.get("rendez_vous")
            lv = request.POST.get("livre")
            creat = request.POST.get("create_at")
            data = Payment(submontant=subm,
                           remise=rm,
                           tva=tv,
                           montant_total=mt,
                           rendez_vous=rd,
                           livre=lv,
                           create_at=creat,)
            data.save()
            return HttpResponseRedirect(reverse('Order'))
        else:
            form = PaymentForm()
        return render(request, 'kalaliso/payment.html', {'form': form})

def payment_detail(request, payment_id):
    qs = Payment.objects.all()

    context = {'detail_payment': qs, }

    return render(request, 'kalaliso/payment_detail.html', context)


# ===========================
#      VIEWS KALALISO
#          END
# ===========================
