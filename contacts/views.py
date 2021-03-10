from .form import ContactForm
# SignUpForm, EditProfileForm
# from .forms import UploadFileForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template import context
from contacts.models import Contact
from .form import  SignUpForm, EditProfileForm
# from .forms import UploadFileForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import Http404
from .import views
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages



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

def thanks(request):
    return HttpResponse('Thanks, your form has been processed')

def contact(request):
    if request.method == 'POST':
        stat           = request.POST.get('status')
        sexe           = request.POST.get('sexe')
        nom            = request.POST.get('nom')
        prenom         = request.POST.get('prenom')
        # photo_identite = request.POST.get('photo_identite')
        contact        = request.POST.get('contact')
        n_cin          = request.POST.get('n_cin')
        nina           = request.POST.get('nina')
        profession     = request.POST.get('profession')
        rcimm          = request.POST.get('rcimm')
        nif            = request.POST.get('nif')
        siege_social   = request.POST.get('siege_social')
        responsable    = request.POST.get('responsable')
        email          = request.POST.get('email')
        created_at     = request.POST.get('created_at')
        # photo_identite = photo_identite,

        data  = Contact(status=stat, sexe=sexe, nom=nom, prenom=prenom,
                         contact=contact, n_cin=n_cin, nina=nina, profession=profession, rcimm=rcimm,
                         nif=nif, siege_social=siege_social, responsable=responsable, email=email,
                         created_at=created_at)
        data.save()
        return HttpResponseRedirect(reverse('thanks'))

    else:
       form = ContactForm()
    return render(request, 'contacts/contacts.html', {'form':form})


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


def home(request):
    return render(request, 'contacts/home.html', {})

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