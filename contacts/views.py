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
from contacts.models import *
from .forms import *
from django.contrib.gis.db import  *
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
            # return render(request, 'person/person.html')
            return redirect('contacts:person')
    else:
        form = PersonForm
    return render (request, 'person/person.html', {'form': form})

def list(request,):
    obj = Person.objects.all().order_by('-id')
    context = {'obj': obj,}
    return render(request, 'person/list_person.html', context)


def delete(request, id):
    del_contact = Person.objects.get(id=id).delete()
    # del_contact.delete()
    context = {
        'delete': del_contact
    }
    return render(request, 'person/list_person.html', context)

def detail(request, id):
    person_detail = Person.objects.get(id=id)
    context = {
        'view_person': person_detail,
    }
    return render (request, 'person/person_detail.html', context)


def person_paginator(request):
    persons        = Person.objects.all().order_by('id')
    paginator      = Paginator(persons, 5)
    page_number    = request.GET.get('page')
    page_object    = paginator.get_page(page_number)
    person_number  = persons.count()
    message        = f'{ person_number } Nombre:'
    if page_number == 1:
       message = f'{ page_number } Nombre :'
    context = {
        'persons': page_object,
        'person_number': person_number,
        'message': message,
    }
    return render(request, 'paginator/person_paginator.html', context)

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


# OUTPUT CARD ADDRESS PERSON ON PDF
def report_card(request, id):
    person_detail = Person.objects.get(id=id)
    template_path = 'pdf/report_card.html'
    context = {'view_person': person_detail}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="card_person.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    status = pisa.CreatePDF(html, dest=response)

    if status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# def delete(request, id):
#     del_contact = Person.objects.delete(id=id)
#
#     context = {
#         'delete_contact': del_contact,
#     }
#     return render (request, 'person/delete.html', context)

