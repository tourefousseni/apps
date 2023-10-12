from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import StrictButton
from crispy_forms.layout import Submit, Layout, Row, Column, Div, Field
from crispy_forms.bootstrap import TabHolder, Tab
from crispy_forms.bootstrap import InlineRadios, FormActions, StrictButton
from django import forms
# from .widgets import BootstrapDateTimePickerInput *
# from django_bootstrap_datetimepicker import *
# from crispy_bootstrap_datetime.widgets import DateTimePicker
from django_bootstrap_datetimepicker import *
from django.forms import widgets
import datetime
from .models import Commune, Region, Cercle, Village, Parcel, Zone

class ParcelForm(forms.ModelForm):
    class Meta:
        model = Parcel
        fields = '__all__'
        # exclude = ['id','id_reg']


class ZoneForm(forms.ModelForm):
    class Meta:
        model = Zone
        fields = '__all__'
        # exclude = ['id','id_reg']



class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = '__all__'
        exclude = ['id','id_reg']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

class CercleForm(forms.ModelForm):
    class Meta:
        model = Cercle
        fields = '__all__'

        exclude = ['id_cer', 'id_reg', 'id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

class CommuneForm(forms.ModelForm):
    class Meta:
        model = Commune
        fields = '__all__'
        exclude = ['com']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

class VillageForm(forms.ModelForm):
    class Meta:
        model = Village
        fields = '__all__'
        exclude = ['id_village', 'id','alt', 'long', 'lat']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)