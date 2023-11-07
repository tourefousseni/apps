# from geo.Geoserver import Geoserver

# Initialize the library
# geo = Geoserver('http://127.0.0.1:8080/geoserver', username='admin', password='geoserver')
from django.shortcuts import render, redirect
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
from contacts.models import Person
from gestion.models import Order, Order_Items, Product, Payment, Depense
# Create your views here.

def maps(request):
    parcel=Parcel.objects.all()

    context={
        'parcel':parcel
    }

    return render(request, 'maps/maps.html', context)

# def locate(request, pk):
#     data_region = Region.objects.filter(id=pk)
#     data_cercle = Cercle.objects.filter(id=pk)
#     data_commune = Commune.objects.filter(id=pk)
#     data_village = Village.objects.filter(id=pk)
#     context={
#         'data_region': data_region,
#         'data_cercle': data_cercle,
#         'data_commune': data_commune,
#         'data_village': data_village,
#     }
#     return render(request, 'localisation/locate.html', context)


def parcel(request):
    if request.method == 'POST':
        form = ParcelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
            form = ParcelForm()
    return render(request, 'maps/parcel.html', {'form': form})

# def zone(request):
#     if request.method == 'POST':
#         form = ZoneForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#             form = ZoneForm()
#     return render(request, 'maps/zone.html', {'form': form})


def localization(request):
    if request.method == 'POST':
        form = LocalizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
            form = LocalizationForm()
    return render(request, 'localisation/locate.html', {'form': form})


# def region(request):
#     if request.method == 'POST':
#         form = RegionForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('maps:cercle')
#     else:
#             form = RegionForm()
#     return render(request, 'localisation/cercle.html', {'form': form})
#
# def cercle(request):
#     if request.method == 'POST':
#         form = CercleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('maps:commune')
#     else:
#         form = CercleForm()
#     return render(request, 'localisation/cercle.html', {'form': form})
#
# def commune(request):
#     if request.method == 'POST':
#         form = CommuneForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('maps:village')
#     else:
#         form = CommuneForm()
#     return render(request, 'localisation/cercle.html', {'form': form})
#
# def village(request):
#     if request.method == 'POST':
#         form = VillageForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('maps:village')
#     else:
#         form = VillageForm()
#     return render(request, 'localisation/cercle.html', {'form': form})