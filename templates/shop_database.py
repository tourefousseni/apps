from gestion.models import *

class Product_shop(models.Model):
    name              = models.CharField(primary_key=True, max_length=50,)
    slug              = models.SlugField()
    def __str__(self):
        return'{}'.format(self.name)

class Sous_Product_shop(models.Model):
    name              = models.CharField(primary_key=True, max_length=50)
    ETAT              = (
        ('Nouveau', 'Nouveau'),
        ('Second main', 'Second main'),
        ('Reparer', 'Reparer'),)

    etat              = models.CharField(max_length=50, choices=ETAT, default='Nouveau',)
    photo_product     = models.ImageField(upload_to='photos_product/', blank=True)
    product_show      = models.ForeignKey(Product_shop, on_delete=models.CASCADE, verbose_name='Sous Produits')
    description       = models.CharField(max_length=400, blank=True, null=True)
    slug              = models.SlugField()
    status            = models.BooleanField(default=True, verbose_name='disponible')
    price             = models.DecimalField(decimal_places=2, max_digits=20, default=100.25, null=True, blank=True)
    create_at         = models.DateField(auto_now=True)

    def __str__(self):
        return'{}'.format(self.name)

class Poster_shop(models.Model):
    NAME_POSTER_SHOP  = (
        ('Person', 'Person'),
        ('Atelier', 'Atelier'),
        ('Usine', 'Usine'),
        ('Centre de formation', 'Centre de formation'),
        ('Boutique', 'Boutique'),
        ('commissionaire', 'commissionaire'),)
    name_poster_shop  = models.CharField(max_length=100, choices=NAME_POSTER_SHOP, default='',)
    contact           = models.CharField(max_length=50, blank=True, null=True)
    pseudo            = models.CharField(max_length=50, null=True, blank=True)
    description       = models.TextField(null=True, blank=True)
    status            = models.BooleanField(default=True)
    email             = models.EmailField()
    date_post         = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return'{}'.format(self.name_poster_shop)

class Acheteur_shop(models.Model):
    first_name_acheteur     = models.CharField(max_length=50, blank=True, null=True)
    last_name_acheteur      = models.CharField(max_length=50, blank=True, null=True)
    username_acheteur       = models.CharField(max_length=50, blank=True, null=True)
    quartier                = models.CharField(max_length=50, blank=True, null=True)
    email                   = models.EmailField()
    contact_1               = models.CharField(max_length=50, blank=True, null=True)
    contact_2               = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return'{}'.format(self.first_name_acheteur)

class Order_shop(models.Model):
    id_product        = models.ManyToManyField(Product_shop,  verbose_name='products')
    id_achecteur      = models.ForeignKey(Acheteur_shop, on_delete=models.CASCADE, verbose_name='acheteur')
    qty               = models.IntegerField()
    amount            = models.IntegerField()
    status            = models.BooleanField(default=True)
    taxe              = models.IntegerField()
    remise            = models.IntegerField()
    created_at        = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return'{}{}'.format(self.id_achecteur.first_name_acheteur, self.id_achecteur.email)

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
    id_achecteur      = models.ForeignKey(Acheteur_shop, on_delete=models.CASCADE)
    order_show        = models.ForeignKey(Order_shop, on_delete=models.CASCADE)
    status            = models.BooleanField(default=True)
    created_at        = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return'{}{}'.format(self.id_achecteur.first_name_acheteur, self.order_show.amount)

class Shipping_shop(models.Model):
    first_name        = models.CharField(max_length=30, blank=True, null=True)
    last_name         = models.CharField(max_length=30, blank=True, null=True)
    username          = models.CharField(max_length=30, blank=True, null=True)
    id_achecteur      = models.ForeignKey(Acheteur_shop, on_delete=models.CASCADE)
    ship_order_show   = models.ForeignKey(Order_shop, on_delete=models.CASCADE)
    price_shipping    = models.IntegerField(blank=True, null=True, verbose_name='commission')
    status_shipping   = models.BooleanField(default=True)
    create_at         = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return'{}'.format(self.first_name)
