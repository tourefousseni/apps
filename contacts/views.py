from .forms import ContactForm, ParcelForm
# SignUpForm, EditProfileForm
# from .forms import UploadFileForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template import context
from contacts.models import Contact
from .forms import  SignUpForm, EditProfileForm
# from .forms import UploadFileForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import Http404
from .import views
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import context
from django.template import defaulttags
from contacts.models import Contact, Parcel


# Create your views here.

# def contact(request):
#           contacts = Contact.objects.all()
#
#           context = {
#             'contacts': contacts,
#           }
#
#           return render(request, 'contacts/contacts.html', context)


# def contact(request,):
#     contacts = Contact.objects.all()
#     context = {
#         'contacts': contacts,
# 	}
#     # return render(request, 'contacts/contacts.html', context)
#     form = ContactForm()
#     return render(request, 'contacts/contacts.html', {'form': form})
#
# def thanks(request):
#     return HttpResponse('Thanks, your form has been processed')

def home(request):
    return render(request, 'contacts/home.html', {})


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

        data = Contact(status=sta, sexe=sx, nom=no, prenom=pre, matricule=mle, contact=cont, n_cin=cin, nina=ni,
                       profession=prof, rcimm=rci, nif=nf, siege_social=s_s, responsable=res, email=ema, created_at=cre)

        data.save()
        # return HttpResponse(('adresses'))
        return HttpResponseRedirect(reverse('parcel'))
    else:
        blog = ContactForm()
    return render(request, 'contacts/contacts.html', {'form': blog})


def contact_detail(request, contact_id):
        qs = Contact.objects.all()
        context = {
            'contacts': qs,
        }
        return render(request, 'contacts/contacts_detail.html', context)


def profil(request,):
    ps = Contact.objects.all()
    context = {
        'contacts': ps,
    }
    return render(request, 'contacts/profil.html', context)


def about(request):
    return render(request, 'contacts/about.html', {})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,('You Have been Logged In !'))
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
            messages.success(request,('You Have Edited Your Profiel...'))
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
            messages.success(request, ('You Have Edited Your Password...'))
            return redirect('home')

    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form}

    return render(request, 'contacts/change_password.html', context)


def parcel(request):

    if request.method == 'POST':
        sty = request.POST.get('type')
        ar = request.POST.get('area')
        pe = request.POST.get('perimeter')
        cod = request.POST.get('code')
        cre = request.POST.get('created_at')
        upd = request.POST.get('update_at')

        data = Parcel(type=sty, area=ar, perimeter=pe, code=cod, update_at=upd, created_at=cre)

        data.save()
        # return HttpResponse(('adresses'))
        return HttpResponseRedirect(reverse('home'))
    else:
        blog = ParcelForm()
    return render(request, 'contacts/parcel.html', {'form': blog})