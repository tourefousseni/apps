from .models import *

class Product_shop(models.Model):
    name              = models.CharField(primary_key=True, max_length=50,)
    def __str__(self):
        return'{}'.format(self.name)

class Sous_Product_shop(models.Model):
    name              = models.CharField(primary_key=True, max_length=50)
    ETAT              = (
        ('Nouveau', 'Nouveau'),
        ('Second main', 'Second main'),
        ('Reconditionned', 'Reconditionned'),)

    etat              = models.CharField(max_length=50, choices=ETAT, default='Nouveau',)
    photo             = models.ImageField(upload_to='photos_shop/')
    id_product        = models.ManyToManyField(Product_shop)
    description       = models.CharField(max_length=200, blank=True, null=True)
    slug              = models.SlugField()
    status            = models.BooleanField(default=True)
    price             = models.DecimalField(decimal_places=2, max_digits=20, default=100.25, null=True, blank=True)
    create_at         = models.DateField(auto_now=True)

    def __str__(self):
        return'{}'.format(self.name)

class Poster_shop(models.Model):
    NAME_POSTER_SHOP = (
        ('Nouveau', 'Nouveau'),
        ('Second main', 'Second main'),
        ('Reconditionned', 'Reconditionned'),)

    name_poster_shop  = models.CharField(max_length=50, choices=NAME_POSTER_SHOP, default='Nouveau', )
    contact           = models.CharField(max_length=50, blank=True, null=True)
    pseudo            = models.CharField(max_length=50, null=True, blank=True)
    email             = models.EmailField()
    date_post = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return'{}'.format(self.name_poster_shop)

class Acheteur_shop(models.Model):
    name_acheteur     = models.CharField(max_length=50, blank=True, null=True)
    email             = models.EmailField()
    contact_1         = models.CharField(max_length=50, blank=True, null=True)
    contact_2         = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return'{}'.format(self.name_acheteur)

class Order_shop(models.Model):
    id_product        = models.ForeignKey(Product_shop, on_delete=models.CASCADE, verbose_name='product')
    id_achecteur      = models.ForeignKey(Acheteur_shop, on_delete=models.CASCADE, verbose_name='acheteur')
    contact           = models.CharField(max_length=50, blank=True, null=True)
    qty               = models.IntegerField()
    amount            = models.IntegerField()
    status            = models.BooleanField(default=True)
    email             = models.EmailField()
    date_post = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return'{}'.format(self.id_achecteur.name_acheteur)

class Paiement_shop(models.Model):
    MODE_PAYMENT = (
        ('Espece', 'Espece'),
        ('Orange Money', 'Orange Money'),
        ('Mobi Cash', 'Mobi Cash'),
        ('Sama Money', 'Sama Money'),
        ('Wave', 'Wave'),
        ('Virement', 'Virement'),
        ('Transaction', 'Transaction'),)
    mode_payment      = models.CharField(max_length=50, choices=MODE_PAYMENT, default='Espece', )
    id_achecteur       = models.ForeignKey(Acheteur_shop, on_delete=models.CASCADE)
    qty               = models.IntegerField()
    price             = models.IntegerField()
    amount            = models.IntegerField()
    taxe              = models.IntegerField()
    remise            = models.IntegerField()
    status            = models.BooleanField(default=True)
    date              = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return'{}'.format(self.id_achecteur.name_acheteur)

class Shipping_shop(models.Model):
    First_name        = models.CharField(max_length=30, blank=True, null=True)
    last_name         = models.CharField(max_length=30, blank=True, null=True)
    username          = models.CharField(max_length=30, blank=True, null=True)
    id_achecteur      = models.ForeignKey(Acheteur_shop, on_delete=models.CASCADE)
    id_order          = models.ForeignKey(Order_shop, on_delete=models.CASCADE)
    price_shipping    = models.IntegerField()
    status_shipping   = models.BooleanField(default=True)
    date              = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return'{}'.format(self.First_name)
