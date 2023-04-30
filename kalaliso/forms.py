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

from .models import  Mesure, Product,  Video, Person
# Payment, \
#     Product, Order, Order_Items, \
#


# ==============================================
#                  FORM KALALISO
#                        START
# ==============================================

class MesureForm(forms.ModelForm):
    class Meta:
        model = Mesure
        template_name = 'kalaliso/mesure.html'
        fields = ['coude', 'epaule',
                  'manche_courte', 'manche_longue',
                  'tour_manche','taille',
                  'poitrine','longueur_boubou',
                  'longueur_patanlon','fesse',
                  'ceinture','cuisse','patte',
                  ]
        exclude = ['update_at','created_at',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)


class Video_form(forms.ModelForm):
   class Meta:
         model=Video
         fields=("title","video")

# class UserForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields='__all__'

class ProductForm(forms.ModelForm):
    class Meta:
         model = Product
         template_name = 'kalaliso/product.html'
         fields = ['name', 'code_product','description', 'price', 'create_at']
         exclude = ['create_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name', ),
                Column('price', ),
                Column('description', ),
            ),
            Row(
                Column('code_product', ),
                # Column('create_at', ),
            ),

            FormActions(
                Submit('save_product', 'Save'),
                Submit('cancel', 'Cancel', css_class='btn btn-danger')
            ),
        )
#
# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         template_name = 'kalaliso/order.html'
#         fields = ['person_id',
#                   'reception',
#                   'order_items',
#                   'localization',
#                   'confirmed',
#                   'cancelled',
#                   'rendez_vous',
#                   'create_at',
#                   'remise']
#
#         exclude = ['code_order']
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
#             FormActions(
#                     Submit('save_product', 'Save'),
#                     Submit('cancel', 'Cancel', css_class='btn btn-danger')
#                 )
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
#                 Column('submontant', ),
#             ),
#             Row(
#                 Column('product_id', ),
#                 # Column('create_at', ),
#             ),
#
#             FormActions(
#                 Submit('save_product', 'Save'),
#                 Submit('cancel', 'Cancel', css_class='btn btn-danger')
#             ),
#         )
#
# class PaymentForm(forms.ModelForm):
#     class Meta:
#         model = Payment
#         template_name = 'kalaliso/payment.html'
#         fields = ['mode_payment',
#                   'code_payment',
#                   'amount',
#                   'fees_commission',
#                   'delivered' ]
#
#         exclude = ['code_payment', 'create_at']
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper(self)
#         self.helper.form_method = 'post'
#         self.helper.layout = Layout(
#             Row(
#                 Column('mode_payment'),
#                 Column('amount'),
#                 Column('fees_commission'),
#                 ),
#             Row(
#                 Column('create_at'),
#                 Column('delivered'),
#                  ),
#         )
#

# ==============================================
#                  FORM KALALISO
#                        END
# ==============================================


