from django import forms

class ContactForm(forms.Form):
    STATUS                = (
        ('PERSONNE',   'Personne'),
        ('SOCIETE',     'Societe'),)
    status                = forms.CharField(max_length=30, choices=STATUS, default='Personne')
    SEXE                  = (
        ('HOMME',      'Homme'),
        ('FEMME',      'Femme'),)
    sexe                  = forms.CharField(max_length=30, choices=STATUS, default='Sexe')
    nom                   = forms.CharField(max_length=50, null=True, blank=True, verbose_name='NOM')
    prenom                = forms.CharField(max_length=50, null=True, blank=True, verbose_name='PRENOM')
    photo_identite        = forms.ImageField(upload_at='photos/identite',   null=True, blank=True, verbose_name='PHOTO IDENTITE')
    contact               = forms.CharField(max_length=50, null=True, blank=True, verbose_name='NUMERO DE TELEPHONE')
    n_cin                 = forms.CharField(max_length=50, null=True, blank=True, verbose_name='NUMERO DE CARTE IDENTITE NATIONALE')
    nina                  = forms.CharField(max_length=50, null=True, blank=True, verbose_name='NUMERO DE CARTE NINA')
    profession            = forms.CharField(max_length=50, null=True, blank=True, verbose_name='PROFESSION')
    rcimm                 = forms.CharField(max_length=50, null=True, blank=True, verbose_name='REGISTRE DE COMMERCE')
    nif                   = forms.CharField(max_length=50, null=True, blank=True, verbose_name='NUMERO IDENTFICATION FISCAL')
    siege_social          = forms.CharField(max_length=50, null=True, blank=True, verbose_name='SIEGE SOCIAL')
    responsable           = forms.CharField(max_length=50, null=True, blank=True, verbose_name='RESPONSABLE')
    email                 = forms.EmailField(max_length=50, null=True, blank=True, verbose_name='ADRESSE EMAIL')
    created_at            = forms.DateTimeField(auto_now_add=True)
