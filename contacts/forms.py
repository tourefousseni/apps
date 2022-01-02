from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import StrictButton
from crispy_forms.layout import Submit, Layout, Row, Column, Div, Field
from crispy_forms.bootstrap import TabHolder, Tab
from crispy_forms.bootstrap import InlineRadios
# from django import forms
# from django.forms import forms
from django.forms import ModelForm
from django.forms import widgets
import datetime
from .models import Person, \
                    Product, \
                    Order, \
                    Mesure, \
                    OrderDetail, \
                    Image
                    # Payment


# ==============================================
#                  FORM KALALISO
#                        START
# ==============================================
class ImageForm(forms.ModelForm):
    TYPE      = (
        ('Broderie', 'Broderie'),
        ('Couture simple', 'COUTURE SIMPLE'),
        ('Couture a main', 'COUTURE A MAIN'),
        ('Finition', 'FINITION'),)

    GENRE     = (
        ('H', 'Homme'),
        ('F', 'Femme'),
        ('A', 'Autres'),)

    CATEGORY  = (
        ('G', 'Grande'),
        ('M', 'Moyenne'),
        ('P', 'Petite'),)
    # id        = forms.AutoField(primary_key=True)
    title     = forms.CharField()
    slug      = forms.SlugField()
    tags      = forms.CharField()
    image     = forms.ImageField()
    type      = forms.ChoiceField( choices=TYPE, label='Broderie')
    category  = forms.ChoiceField( choices=CATEGORY, label='Grande')
    genre     = forms.ChoiceField( choices=GENRE, label='Homme')

    class Meta:
        model = Image
        fields = ('title',
                  'slug',
                  'tags',
                  'image',
                  'type',
                  'category',
                  'genre')

class PersonForm(forms.ModelForm):

    STATUS = (
                ('Client', 'CLIENT'),
                ('Ouvrier', 'OUVRIER'),
                ('Apprenti', 'APPRENTI'),
                ('Fournisseur', 'FOURNISSEUR'),
                ('Company', 'COMPANY'),)

    status = forms.ChoiceField(label='Status', choices=STATUS, initial='Client')
    SEX = (
                ('H', 'Homme'),
                ('F', 'Femme'),
                ('A', 'Autres'),)
    CATEGORY = (
        ('G', 'Grande'),
        ('M', 'Moyenne'),
        ('P', 'Petite'),
    )
    TYPE_TAILLEUR = (
        ('Brodeur', 'Brodeur'),
        ('Tailleur simple', 'TAILLEUR SIMPLE'),
        ('Tailleur simple', 'TAILLEUR SIMPLE'),
        ('Boutouman', 'BOUTOUMAN'),)

    sex = forms.ChoiceField(label='Sex', choices=SEX, initial='Homme')
    category = forms.ChoiceField(label='Category', choices=CATEGORY, initial='Grande')
    type_tailleur = forms.ChoiceField(label='Type Tailleur', choices=TYPE_TAILLEUR, required='')
    prenom = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    nom = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact_1 = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # photo = forms.ImageField()
    # domicile = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'Domicile'}))
    # alias = forms.CharField(label="Alias", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'Alias'}))
    # # n_cin = forms.CharField(label="Carte d'Indentite Nationale", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'CIN'}))
    # nina = forms.CharField(label="NINA", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'NINA'}))
    # profession = forms.CharField(label="Profession", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'Profession'}))
    # nationalite = forms.CharField(label="Nationalite", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'Nationalite'}))
    # nif = forms.CharField(label="NIF", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'NIF'}))
    # siege_social = forms.CharField(label="SIEGE SOCIAL", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'Siege Social'}))
    # responsable = forms.CharField(label="RESPONABLE", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'Responsable'}))
    # email = forms.EmailField(max_length=50, label='ADRESSE EMAIL', widget=forms.TextInput(attrs={'class': 'form-control', 'Email'}))
    # created_at = forms.DateField(
    #     input_formats=['%d/%m/%Y'],
    #     widget=forms.DateTimeInput(attrs={
    #         'class': 'form-control datetimepicker-input',
    #         'data-target': 'datetimepicker1'
    #     })
    # )

    class Meta:
        model = Person
        fields = ['status', 'sex', 'category', 'prenom', 'nom', 'contact_1']
        # exclude = ('domicile', 'email', 'alias', 'type_tailleur', 'code_person','photo', 'profession', 'responsable', 'numero_reference', 'created_at')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.helper = FormHelper()
            self.helper.form_method = 'POST'
            self.helper.add_input(Submit('submit', 'Save Person' ))
            self.helper.add_input(Submit('cancel', css_class='btn btn-danger'))
            self.helper.layout = Layout(
                Row(
                    Column('prenom'),
                    Column('nom'),
                ),
                InlineRadios('status'),
                InlineRadios('sex'),
                InlineRadios('category'),
                'contact_1',

            )

class MesureForm(forms.Form):
        person_mesure = forms.ModelChoiceField(queryset=Person.objects.all())
        coude = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
        epaule = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}))
        manche = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
        tour_manche = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}))
        taille = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
        poitrine = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
        longueur_boubou = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
        longueur_patanlon = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control'}))
        fesse = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
        ceinture = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
        cuisse = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
        patte = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
        # create_at = forms.DateField()
        # update_at = forms.DateField()

        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

                self.helper = FormHelper()
                self.helper.form_method = 'post'
                self.helper.layout = Layout(
                            Div(
                                Field('coude', wrapper_class='col-md-3'),
                                Field('epaule', wrapper_class='col-md-3'),
                    css_class='form-row')
                    )

                class Meta:
                        model = Mesure


class ProductForm(forms.Form):

        NAME = (
            ('Boubou', 'Boubou'),
            ('Grand Boubou', 'Grand Boubou'),
            ('Chemise Complet', 'Chemise Complet'),
            ('Chemise Manche Long', 'Chemise Manche Long'),
            ('Chemise Manche Court', 'Chemise Manche Court'),
            ('Pagne Jupe', 'Pagne Jupe'),
            ('Pagne Complet', 'Pagne Complet'),
            ('Pagne Maniere', 'Pagne Maniere'),
            ('Patanlon', 'Patanlon'),
            ('Tenu Scolaire', 'Tenu Scolaire'),
            ('Tenu Securite', 'Tenu Securite'),
            ('AUTRES', 'AUTRES'),)
        name = forms.ChoiceField( choices=NAME, required='Boubou')
        code_product = forms.CharField(
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
        # price = forms.IntegerField(label="price", widget=forms.NumberInput(attrs={'class': 'form-control', 'price'}))
        # name = forms.CharField(label="Name Product", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'Name Product'}))
        photo = forms.ImageField()
        price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
        # create_at = forms.DateField()

        class Meta:
            model = Product
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)


class OrderForm(forms.Form):
            PRODUIT = [
                ('Boubou', 'Boubou'),
                ('Grand Boubou', 'Grand Boubou'),
                ('Chemise Complet', 'Chemise Complet'),
                ('Chemise Manche Long', 'Chemise Manche Long'),
                ('Chemise Manche Court', 'Chemise Manche Court'),
                ('Pagne Jupe', 'Pagne Jupe'),
                ('Pagne Complet', 'Pagne Complet'),
                ('Pagne Maniere', 'Pagne Maniere'),
                ('Patanlon', 'Patanlon'),
                ('Tenu Scolaire', 'Tenu Scolaire'),
                ('Tenu Securite', 'Tenu Securite'),
                ('AUTRES', 'AUTRES'),]
            id_person = forms.ModelChoiceField(queryset=Person.objects.all())
            # produit = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=PRODUIT)
            reception = forms.DateField()

            rendez_vous = forms.DateField()

            class Meta:
                models = Order

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)


class OrderDetailForm(forms.Form):
    CATEGORY = (
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
        ('Fille', 'Fille'),
        ('Garçon', 'Garçon'),
        ('Autres', 'Autres'),
    )
    category = forms.ChoiceField(label='Category', choices=CATEGORY, required='HOMME')

    PRODUIT = [
        ('Boubou', 'Boubou'),
        ('Grand Boubou', 'Grand Boubou'),
        ('Chemise Complet', 'Chemise Complet'),
        ('Chemise Manche Long', 'Chemise Manche Long'),
        ('Chemise Manche Court', 'Chemise Manche Court'),
        ('Pagne Jupe', 'Pagne Jupe'),
        ('Pagne Complet', 'Pagne Complet'),
        ('Pagne Maniere', 'Pagne Maniere'),
        ('Patanlon', 'Patanlon'),
        ('Tenu Scolaire', 'Tenu Scolaire'),
        ('Tenu Securite', 'Tenu Securite'),
        ('AUTRES', 'AUTRES'), ]
    person_id = forms.ModelChoiceField(queryset=Person.objects.all())
    order_id = forms.ModelChoiceField(queryset=Order.objects.all())
    produit = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=PRODUIT)
    submontant = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    remise = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    create_at = forms.DateField()


    class Meta:
        models = OrderDetail

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PaymentForm(forms.Form):
    # id = forms.AutoField(primary_key=True)
    paymentOrder = forms.ModelChoiceField(queryset=Order.objects.all())
    person_id = forms.ModelChoiceField(queryset=Person.objects.all())
    montant_total = forms.DecimalField( widget=forms.NumberInput(attrs={'class': 'form-control'}))
    livre = forms.BooleanField()
    create_at = forms.DateField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# ==============================================
#                  FORM KALALISO
#                        END
# ==============================================


class EditProfileForm(UserChangeForm):
        password = forms.CharField(label="", widget=forms.TextInput(attrs={'type': 'hidden'}))

        class Meta:
            model = User
            fields = ('username',
                      'first_name',
                      'last_name',
                      'email',
                      'password')

class SignUpForm(UserCreationForm):
        email = forms.EmailField(widget=forms.EmailInput(
            attrs={'class': 'form-control'}))
        last_name = forms.CharField( max_length=100,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
        first_name = forms.CharField(max_length=100, widget=forms.TextInput(
            attrs={'class': 'form-control'}))

        class Meta:
            model = User
            fields = ('username',
                      'first_name',
                      'last_name',
                      'email',
                      'password1',
                      'password2')

        def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)

            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['placeholder'] = 'Pseudo'
            self.fields['username'].label = ''
            self.fields['username'].help_text = '<span class= "form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['placeholder'] = 'Password'
            self.fields['password1'].label = ''
            self.fields['password1'].help_text = '<ul class ="form-text text-muted small" ><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\' t be a commonly used password.</li><li>Your password can\' t be entirely numeric.</li></ul>'

            self.fields['password2'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['placeholder'] = 'Comfirm password'
            self.fields['password2'].label = ''
            self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

# tva = forms.IntegerField(label="Tva", widget=forms.NumberInput(attrs={'class': 'form-control', 'Tva'}))
# rendez_vous = forms.DateTimeField()