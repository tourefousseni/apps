from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
import datetime

# from contacts.models import contacts_contact

class ContactForm(forms.Form):
    # STATUS                = (
    #     ('PERSONNE',    'Personne'),
    #     ('SOCIETE',     'Societe'),)
    # status                = forms.ChoiceField(choices=STATUS,)
    # SEXE                  = (
    #     ('HOMME',      'H'),
    #     ('FEMME',      'F'),)
    # sexe                  = forms.ChoiceField(choices=SEXE,)
    nom                   = forms.CharField(max_length=50, label='inputFirstName')
    prenom                = forms.CharField(max_length=50, label='inputLastName')
    contact               = forms.CharField(max_length=8, label='TELEPHONE')
    n_cin                 = forms.CharField(max_length=50,  label='CIN')
    nina                  = forms.CharField(max_length=50,  label='NINA')
    profession            = forms.CharField(max_length=50,  label='PROFESSION')
    rcimm                 = forms.CharField(max_length=50,  label='REGISTRE DE COMMERCE')
    nif                   = forms.CharField(max_length=50,  label='NIF')
    siege_social          = forms.CharField(max_length=50,  label='SIEGE SOCIAL')
    responsable           = forms.CharField(max_length=50,  label='RESPONSABLE')
    email                 = forms.EmailField(max_length=50, label='ADRESSE EMAIL')
    created_at            = forms.DateTimeField()



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





    # def clean(self):
    #     data = self.cleaned_data
    #
    #     status            = data.get('status')
    #     sexe              = data.get('sexe')
    #     nom               = data.get('nom')
    #     prenom            = data.get('prenom')
    #     photo_identite    = data.get('photo_identite')
    #     contact           = data.get('contact')
    #     n_cin             = data.get('n_cin')
    #     nina              = data.get('nina')
    #     profession        = data.get('profession')
    #     rcimm             = data.get('rcimm')
    #     nif               = data.get('nif')
    #     siege_social      = data.get('siege_social')
    #     responsable       = data.get('responsable')
    #     email             = data.get('email')
    #     created_at        = data.get('created_at')
    #
    #     return data

    # class Meta:
    #     model = contacts_contact
    #     fields = ('status', 'sexe', 'nom', 'prenom','photo_identite',
    #         'contact','n_cin', 'nina','profession','rcimm','nif',
    #         'siege_social','responsable','email', 'created_at',)
    #(upload_at='photos/identite', label='PHOTO IDENTITE')
    # def __init__(self, *args, **kwargs):
    #     super(ContactForm, self).__init__(*args, **kwargs)
    #     self.fields['status'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'input-text',
    #     })
    #     self.fields['sexe'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'input-text',
    #     })
    #     self.fields['nom'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'input-text',
    #     })
    #     self.fields['prenom'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'input-text',
    #     })
    #     self.fields['photo_identite'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'input-text',
    #     })
    #     self.fields['contact'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'input-text',
    #     })
    #     self.fields['n_cin'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'input-text',
    #     })
    #     self.fields['nina'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'input-text',
    #     })
    #     self.fields['profession'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'input-text',
    #     })
    #     self.fields['rcimm'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'input-text',
    #     })
    #     self.fields['nif'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'input-text',
    #     })
    #     self.fields['siege_social'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'input-text',
    #     })
    #     self.fields['responsable'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'input-text',
    #     })
    #     self.fields['email'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'input-text',
    #     })
    #     self.fields['created_at'].widget.attrs.update({
    #         'type': 'text',
    #         'class': 'form-control',
    #         'id': 'input-text',
    #     })


