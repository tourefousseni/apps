from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template import context
from contacts.models import Contact
from .form import ContactForm, SignUpForm, EditProfileForm
# from .forms import UploadFileForm

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import Http404
from .import views
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
# from .form import



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
        stat         = request.POST.get('status')
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
        data           = Contact(status=stat, sexe=sexe, nom=nom, prenom=prenom,
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