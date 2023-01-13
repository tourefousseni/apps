from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
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
from . import forms
from .forms import *
# Create your views here.

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