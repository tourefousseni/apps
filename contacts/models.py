from django.db import models

# Create your models here.


class Contact(models.Model):
    STATUS              = (
        ('PERSONNE',   'Personne'),
        ('SOCIETE',    'Societe'),
    )

    status              = models.CharField(max_length=30, choices=STATUS, default='Personne')
    SEXE = (
        ('HOMME', 'Homme'),
        ('FEMME', 'Femme'),
    )
    sexe                = models.CharField(max_length=10, choices=SEXE, default='Sexe')
    nom                 = models.CharField(max_length=50, null=True, blank=True, verbose_name='NOM')
    prenom              = models.CharField(max_length=50, null=True, blank=True, verbose_name='PRENOM')
    photo               = models.ImageField(upload_to='photos/identite', null=True, blank=True, verbose_name='PHOTO IDENTITE')
    contact             = models.CharField(max_length=50, null=True, blank=True, verbose_name='NUMERO DE TELEPHONE')
    n_cin               = models.CharField(max_length=50, null=True, blank=True, verbose_name='NUMERO DE CARTE IDENTITE NATIONALE')
    nina                = models.CharField(max_length=50, null=True, blank=True, verbose_name='NUMERO DE CARTE NINA')
    profession          = models.CharField(max_length=50, null=True, blank=True, verbose_name='PROFESSION')
    rcimm               = models.CharField(max_length=50, null=True, blank=True, verbose_name='REGISTRE DE COMMERCE')
    nif                 = models.CharField(max_length=50, null=True, blank=True, verbose_name='NUMERO IDENTFICATION FISCAL')
    siege_social        = models.CharField(max_length=50, null=True, blank=True, verbose_name='SIEGE SOCIAL')
    responsable         = models.CharField(max_length=50, null=True, blank=True, verbose_name='RESPONSABLE')
    email               = models.EmailField(max_length=50, null=True, blank=True, verbose_name='ADRESSE EMAIL')
    created_at          = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  ('{} - {} - {}').format(self.nom, self.prenom, self.contact)