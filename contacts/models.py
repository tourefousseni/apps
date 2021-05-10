from django.db import models

# Create your models here.


class Contact(models.Model):
    STATUS              = (
        ('PERSONNE',   'Personne'),
        ('SOCIETE',    'Societe'),
    )

    status              = models.CharField(max_length=30, choices=STATUS,)
    SEXE = (
        ('HOMME', 'Homme'),
        ('FEMME', 'Femme'),
    )
    sexe                = models.CharField(max_length=10, choices=SEXE,)
    nom                 = models.CharField(max_length=50, null=True, blank=True, verbose_name='NOM')
    prenom              = models.CharField(max_length=50, null=True, blank=True, verbose_name='PRENOM')
    matricule           = models.CharField(max_length=50, null=True, blank=True, verbose_name='N°MATRICULE')
    photo               = models.ImageField(upload_to='photos/identite', null=True, blank=True, verbose_name='PHOTO IDENTITE')
    contact             = models.CharField(max_length=8, null=True, blank=True, verbose_name='TELEPHONE')
    n_cin               = models.CharField(max_length=50, null=True, blank=True, verbose_name='CIN')
    nina                = models.CharField(max_length=50, null=True, blank=True, verbose_name='NINA')
    profession          = models.CharField(max_length=50, null=True, blank=True, verbose_name='PROFESSION')
    rcimm               = models.CharField(max_length=50, null=True, blank=True, verbose_name='REGISTRE DE COMMERCE')
    nif                 = models.CharField(max_length=50, null=True, blank=True, verbose_name='NIF')
    siege_social        = models.CharField(max_length=50, null=True, blank=True, verbose_name='SIEGE SOCIAL')
    responsable         = models.CharField(max_length=50, null=True, blank=True, verbose_name='RESPONSABLE')
    email               = models.EmailField(max_length=50, null=True, blank=True, verbose_name='ADRESSE EMAIL')
    created_at          = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  ('{} - {} - {}').format(self.nom, self.prenom, self.contact)




# class Parcel(models.Model):
#     TYPE              = (
#         ('BATI',   'Bati'),
#         ('NON BATIE',    'Non Bati'),)
#     type                = models.CharField(max_length=30, choices=TYPE,)
#     contact             = models.ForeignKey('Contact', on_delete=models.CASCADE)
#     superficie          = models.IntegerField()
#     code                = models.IntegerField()
#     created_at          = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return  ('{} - {} - {}').format(self.type, self.superficie, self.code)