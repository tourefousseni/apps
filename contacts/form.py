from django import forms
import datetime
# from contacts.models import contacts_contact

class ContactForm(forms.Form):
    STATUS                = (
        ('PERSONNE',   'Personne'),
        ('SOCIETE',     'Societe'),)
    status                = forms.ChoiceField(choices=STATUS,)
    SEXE                  = (
        ('HOMME',      'H'),
        ('FEMME',      'F'),)
    sexe                  = forms.ChoiceField(choices=SEXE)
    nom                   = forms.CharField(max_length=50, label='NOM')
    prenom                = forms.CharField(max_length=50, label='PRENOM')
    # photo_identite        = forms.FileField()
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


