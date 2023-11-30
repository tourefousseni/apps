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

from gestion.models import  Depense,Video,Payment,Eau,Annonce

# ==============================================
#                  FORM GESTION
#                        START
# ==============================================

class GestionForm(forms.ModelForm):
    # start_eau = forms.DateTimeField(initial=datetime.date.today)
    # end_eau   = forms.DateTimeField(initial=datetime.date.today)

    debut_eau = forms.DateTimeField(label="Date Debut", widget=forms.DateTimeInput(attrs={
        'class': 'form-control',
        'type': 'date'}))
    fin_eau = forms.DateTimeField(label="Date Fin", widget=forms.DateTimeInput(attrs={
        'class': 'form-control',
        'type': 'date'}))

    class Meta:
        model = Eau
        template_name = 'gestion/eau.html'
        fields = [
                  'person',
                  'volume', 'litre',
                  'diff', 'quantity',
                  'debut_eau','fin_eau',
        ]
        exclude = ['update_at','created_at','duration']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        template_name = 'gestion/payment.html'
        fields = [
                  # 'person',
                  'mode_payment',
                  'code_payment',
                  # 'code_facture',
                  'payment',
                  'amount',
                  'taxe',
        ]
        # fields = ('__all__')

        exclude = [ 'create_at', 'confirmed', 'delivered',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('person'),
                Column('mode_payment'),
                Column('amount'),
                Column('payment'),
                Column('taxe'),
                ),
            Row(
                Column('code_payment'),
                # Column('create_at'),
                Column('delivered'),
                 ),
        )
class AnonceForm(forms.ModelForm):
    class Meta:
        model = Annonce
        template_name = 'gestion/annonce.html'
        fields = ('__all__')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class DepenseForm(forms.ModelForm):
    class Meta:
        model = Depense
        template_name = 'gestion/depense.html'
        fields = ('__all__')
        exclude=['create_at',]
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
        # self.helper = FormHelper(self)
        # self.helper.form_method = 'post'
        # self.helper.layout = Layout(
        #     Row(
        #         Column('mode_payment'),
        #         Column('amount'),
        #         Column('fees_commission'),
        #         ),
        #     Row(
        #         Column('code_payment'),
        #         Column('create_at'),
        #         Column('delivered'),
        #          ),
        # )



class Video_form(forms.ModelForm):
   class Meta:
         model=Video
         fields=("title","video")

# class UserForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields='__all__'

# class ProductForm(forms.ModelForm):
#     class Meta:
#          model = Product
#          template_name = 'gestion/product.html'
#          fields = ['name', 'description', 'price']
#          exclude = ['create_at']
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.layout = Layout(
#             Row(
#                 Column('name', ),
#                 Column('price', ),
#                 Column('description', ),
#             ),
#             Row(
#                 Column('code_product', ),
#                 # Column('create_at', ),
#             ),
#
#             FormActions(
#                 Submit('save_product', 'Save'),
#                 Submit('cancel', 'Cancel', css_class='btn btn-danger')
#             ),
#         )
#
# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         template_name = 'gestion/order.html'
#         fields = ['person_id',
#                   'reception',
#                   # 'localization',
#                   'confirmed',
#                   'cancelled',
#                   'rendez_vous',
#                   'create_at',
#                   'remise',
#                   'code_order',]
#
#         # exclude = []
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.layout = Layout(
#             Row(
#                 Column('person_id'),
#                 Column('order_items'),
#                 Column('localization'),
#                 ),
#             Row(
#                 Column('remise'),
#                 Column('rendez_vous'),
#                 Column('create_at'),
#             ),
#
#             Row(
#                 Column('reception'),
#                 Column('confirmed'),
#                 Column('cancelled'),
#             ),
#             #
#             # InlineRadios('confirmed'),
#             # InlineRadios('cancelled'),
#             # InlineRadios('rendez_vous'),
#
#             # FormActions(
#             #         Submit('save_product', 'Save'),
#             #         Submit('cancel', 'Cancel', css_class='btn btn-danger')
#             #     )
#             )
#
# class Order_ItemsForm(forms.ModelForm):
#     class Meta:
#         model = Order_Items
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper(self)
#         self.helper.form_method = 'post'
#         self.helper.layout = Layout(
#             Row(
#                 Column('category', ),
#                 Column('product_id', ),
#                 Column('quantity', ),
#                 Column('price', ),
#                 Column('submontant', ),
#             ),
#             Row(
#                 Column('product_id', ),
#                 # Column('create_at', ),
#             ),
#
#             # FormActions(
#             #     Submit('save_product', 'Save'),
#             #     Submit('cancel', 'Cancel', css_class='btn btn-danger')
#             # ),
#         )


# ==============================================
#                  FORM GESTION
#                        END
# ==============================================

