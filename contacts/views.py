from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
import io
# from contacts.models import Contact
import time
time.sleep(5)
from accounts.models import *
from kalaliso.models import *
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

def person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse('mesure_list')
            return redirect('contacts:list')
    else:
        form = PersonForm
    return render (request, 'person/person.html', {'form': form})

def list(request):
    list = Person.objects.order_by('-id')
    context = {
        'list_person': list,
    }
    return render (request, 'person/list_person.html', context)

def detail(request, id):
    person_detail = Person.objects.get(id=id)
    context = {
        'view_person': person_detail,
    }
    return render (request, 'person/person_detail.html', context)


# def search(request):
#     return render (request, 'person/search.html')

# def search(request):
#     search = request.GET.get('search')
#     search_contacts = Person.objects.filter(Q(prenom__icontains=search),
#                                             Q(nom__icontains=search),
#                                             Q(contact_1__icontains=search),
#                                             Q(status__icontains=search),
#                                             )
#     # person_number = list_person.count()
#     # message = f' results : {person_number }'
#     # if person_number == 1:
#     #       message = f' results : {person_number }'
#
#     context = {
#         'search_contacts': search_contacts,
#         # 'message': message
#     }
#     return render (request, 'person/search.html', context)

# SEARCH NAME OR CONTACT PERSON IN DATABASE
def search_person(request):
    search = request.GET.get('search')
    search_contacts = Person.objects.filter(Q(nom__icontains=search) |
                                        Q(code_person__icontains=search) |
                                        Q(prenom__icontains=search) |
                                        Q(contact_1__icontains=search) |
                                        Q(genre__icontains=search) |
                                        Q(status__icontains=search)
                                        )
    person_number = search_contacts.count()
    message = f' results : {person_number }'
    if person_number == 1:
          message = f' results : {person_number }'

    context = {
        'search_contacts': search_contacts,
        'message': message
    }
    return render(request, 'person/search.html', context)


def report_card(request):
    return render (request, 'person/person_detail.html')

def delete(request, id):
    del_contact = Person.objects.delete(id=id)

    context = {
        'delete_contact': del_contact,
    }
    return render (request, 'person/delete.html', context)