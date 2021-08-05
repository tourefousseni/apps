from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
# from django import forms
# from django.forms import forms
from django.forms import ModelForm
from django.forms import widgets
import datetime
from .models import Contact, \
                    Person, \
                    Product, \
                    Order, \
                    Mesure, \
                    OrderDetail, \
                    Payment


# from django_bootstrap_datetimepicker.widgets import BootstrapDateTimeInput


# ==============================================
#                  FORM CADASTRE
#                        START
# ==============================================
class ContactForm(forms.ModelForm):

    STATUS = (
        ('PERSONNE',    'Personne'),
        ('SOCIETE',     'Societe'))
    status = forms.ChoiceField(choices=STATUS)
    SEXE = (
        ('HOMME',      'Homme'),
        ('FEMME',      'Femme'))
    sexe = forms.ChoiceField(choices=SEXE, widget=forms.RadioSelect, initial='Homme')
    nom = forms.CharField(label="Nom", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}))

    prenom = forms.CharField(label="Prenom", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prenom'}))

    # matricule = forms.CharField(label="Matricule", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Matricule'}))
    photo = forms.ImageField()
    contact = forms.CharField(label="Contact", max_length=8, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact'}))
    n_cin = forms.CharField(label="Carte d'Indentite Nationale", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CIN'}))
    nina = forms.CharField(label="NINA", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NINA'}))
    profession = forms.CharField(label="Profession", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Profession'}))
    rcimm = forms.CharField(label="Registre Commerce", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Registre Commerce'}))
    nif = forms.CharField(label="NIF", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NIF'}))
    siege_social = forms.CharField(label="SIEGE SOCIAL", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Siege Social'}))
    responsable = forms.CharField(label="RESPONABLE", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Responsable'}))
    email = forms.EmailField(max_length=50, label='ADRESSE EMAIL', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    # created_at = forms.DateTimeField(widget=BootstrapDateTimeInput())
    created_at = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': 'datetimepicker1'
        })
    )
    class Meta:
            model = Contact
            fields = ['status', 'sexe', 'contact', 'nom', 'prenom', 'photo', 'nina', 'nif', 'siege_social',
                      'responsable', 'email', 'created_at']
            exclude = ['matricule']


class ParcelForm(forms.Form):
    TYPE = (
        ('BATI',   'Bati'),
        ('NON BATIE',    'Non Bati'),)
    type = forms.ChoiceField(choices=TYPE)
    contact = forms.ModelMultipleChoiceField(
        queryset=Contact.objects.all(),
        widget=forms.CheckboxSelectMultiple)
    # geom = forms.JSONField()
    area = forms.CharField(label="Area", max_length=8, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Area'}))
    perimeter = forms.CharField(label="Perimeter", max_length=8, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Perimeter'}))
    code = forms.CharField(label="Code", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code'}))
    created_at = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': 'datetimepicker1'
        })
    )
    update_at = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': 'datetimepicker1'
        })
    )
# ==============================================
#                  FORM CADASTRE
#                        END
# ==============================================




# ==============================================
#                  FORM KALALISO
#                        START
# ==============================================


class PersonForm(forms.Form):
    STATUS = (
                ('Client', 'CLIENT'),
                ('Ouvrier', 'OUVRIER'),
                ('Apprenti', 'APPRENTI'),
                ('Fournisseur', 'FOURNISSEUR'),
                ('Company', 'COMPANY'),)

    status = forms.ChoiceField(label='Status', choices=STATUS, widget=forms.RadioSelect, initial='Client')
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

    sex = forms.ChoiceField(label='Sex', choices=SEX, widget=forms.RadioSelect, initial='Homme')
    category = forms.ChoiceField(label='Category', choices=CATEGORY, widget=forms.RadioSelect, initial='Grande')
    type_tailleur = forms.ChoiceField(label='Type Tailleur', choices=TYPE_TAILLEUR, required='Grande')
    prenom = forms.CharField(label="Prenom", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prenom'}))
    nom = forms.CharField(label="Nom", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}))
    contact_1 = forms.IntegerField(label="Contact", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Contact'}))
    photo = forms.ImageField()
    domicile = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Domicile'}))
    alias = forms.CharField(label="Alias", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alias'}))
    # n_cin = forms.CharField(label="Carte d'Indentite Nationale", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CIN'}))
    nina = forms.CharField(label="NINA", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NINA'}))
    profession = forms.CharField(label="Profession", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Profession'}))
    nationnalite = forms.CharField(label="Nationnalite", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nationnalite'}))
    nif = forms.CharField(label="NIF", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NIF'}))
    siege_social = forms.CharField(label="SIEGE SOCIAL", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Siege Social'}))
    responsable = forms.CharField(label="RESPONABLE", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Responsable'}))
    email = forms.EmailField(max_length=50, label='ADRESSE EMAIL', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    created_at = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': 'datetimepicker1'
        })
    )
    class Meta:
        model = Person

    # image = models.ImageField(upload_to='profil/%d/%m/%Y', null=True, blank=True, verbose_name='Photo_commande')
    # STATUS = (
    #     ('Client', 'CLIENT'),
    #     ('Tailleur', 'TAILLEUR'),
    #     ('Apprenti', 'APPRENTI'),
    #     ('Fournisseur', 'FOURNISSEUR'),
    #     ('Company', 'COMPANY'),)
    # SEX = (
    #     ('H', 'Homme'),
    #     ('F', 'Femme'),
    #     ('A', 'Autres'),)
    # CATEGORY = (
    #     ('G', 'Grande'),
    #     ('M', 'Moyenne'),
    #     ('P', 'Petite'),)
    # status = models.CharField(max_length=20, choices=STATUS, default='CLIENT')
    # type_tailleur = models.CharField(max_length=20, choices=TYPE_TAILLEUR, default='TAILLEUR SIMPLE')
    # sex = models.CharField(max_length=20, choices=SEX, default='Homme')
    # category = models.CharField(max_length=20, choices=CATEGORY, default='Grande')
    # code_person = models.CharField(max_length=30, blank=True, verbose_name='Code person')
    # prenom = models.CharField(max_length=30, null=True, blank=True)
    # nom = models.CharField(max_length=30, null=True, blank=True)
    # contact_1 = models.IntegerField()
    # email = models.EmailField(max_length=100, null=True, blank=True)
    # domicile = models.CharField(max_length=30, null=True, blank=True, default='Lafiabougou')
    # alias = models.CharField(verbose_name='alias', max_length=30, null=True, blank=True)
    # profession = models.CharField(max_length=30, null=True, blank=True)
    # contact_2 = models.CharField(max_length=20, null=True, blank=True)
    # date_naissance = models.DateField(auto_now_add=True)
    # nationalite = models.CharField(max_length=30, null=True, blank=True)
    # tutuelle = models.CharField(max_length=30, null=True, blank=True)
    # telephonique_fix = models.CharField(max_length=30, null=True, blank=True)
    # numero_reference = models.PositiveIntegerField(null=True, blank=True)
    # nina = models.PositiveIntegerField(null=True, blank=True)
    # created_at = models.DateField(auto_now=True)

class MesureForm(forms.Form):
        person_mesure = forms.ModelChoiceField(queryset=Person.objects.all())
        coude = forms.IntegerField(label="Coude", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Coude'}))
        epaule = forms.IntegerField(label="Epaule", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Epaule'}))
        manche = forms.IntegerField(label="Manche", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Manche'}))
        tour_manche = forms.IntegerField(label="Tour Manche", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Tour Manche'}))
        taille = forms.IntegerField(label="Taille", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Taille'}))
        poitrine = forms.IntegerField(label="Poitrine", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Pointrine'}))
        longueur_boubou = forms.IntegerField(label="Longueur Boubou", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Longueur Boubou'}))
        longueur_patanlon = forms.IntegerField(label="Longueur Patanlon", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Longueur Patanlon'}))
        fesse = forms.IntegerField(label="Fesse", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Fesse'}))
        ceinture = forms.IntegerField(label="Ceinture", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ceinture'}))
        cuisse = forms.IntegerField(label="Cuisse", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cuisse'}))
        patte = forms.IntegerField(label="Patte", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Patte'}))
        create_at = forms.DateField()
        update_at = forms.DateField()

        class Meta:
            model = Mesure

class ProductForm(forms.Form):
        CATEGORY = (
            ('Homme', 'Homme'),
            ('Femme', 'Femme'),
            ('Fille', 'Fille'),
            ('Garçon', 'Garçon'),
            ('Autres', 'Autres'),
        )
        category = forms.ChoiceField(label='Category', choices=CATEGORY, required='HOMME')
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
        name = forms.ChoiceField(label='Name', choices=NAME, required='Boubou')
        # name = forms.CharField(label="Name Product", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name Product'}))
        photo = forms.ImageField(label='Photos', )
        # price = forms.DecimalField(label="Price", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}))
        create_at = forms.DateField()


        class Meta:
            model = Product

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


class OrderDetailForm(forms.Form):

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
    price = forms.IntegerField(label="price", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'price'}))
    quantity = forms.IntegerField(label="quantity", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'quantity'}))
    remise = forms.IntegerField(label="Remise", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Remise'}))
    create_at = forms.DateField()

    class Meta:
        models = OrderDetail


class PaymentForm(forms.Form):
    # id = forms.AutoField(primary_key=True)
    paymentOrder = forms.ModelChoiceField(queryset=Order.objects.all())
    person_id = forms.ModelChoiceField(queryset=Person.objects.all())
    montant_total = forms.DecimalField(label="Montant Total", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Montant Total'}))
    livre = forms.BooleanField(label='Livraison',)
    create_at = forms.DateField()

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
        email = forms.EmailField(label="", widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Your adress email'}))
        last_name = forms.CharField(label="", max_length=100,
                                    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}))
        first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'First name'}))

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

# tva = forms.IntegerField(label="Tva", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Tva'}))
# rendez_vous = forms.DateTimeField()