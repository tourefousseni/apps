from django.contrib.gis.db import models
from django.contrib.auth.base_user import AbstractBaseUser,  BaseUserManager
from django.db.models.signals import pre_save
from .utils import unique_code_id_generator
from pyblog import settings
# from phonenumber_field.modelfields import PhoneNumberField

# ==============================================
#                  MODELE ACCOUNTS
#                        START
# ==============================================
class My_manager(BaseUserManager):
    def create_user(self, email, first_name,  last_name,username, phone, password=None, ):
        if not email:
            raise ValueError("vous devez entre une adresse email ici !")
        user = self.model( first_name=first_name, last_name=last_name, phone=phone,
                           password=password,email=self.normalize_email(email))
        user.first_name    = first_name
        user.last_name     = last_name
        user.username      = username
        user.phone         = phone
        user.set_password(password)
        user.staff         = True
        user.admin         = True
        user.active        = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name,username, phone, password=None, ):
        user = self.create_user(email, first_name,last_name,username, phone, password,)
        user.set_password(password)
        user.staff      =   True
        user.admin      =   True
        user.active     =  True

        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    objects = My_manager()
    # id = models.AutoField(primary_key=True)
    GENRE = (
        ('Homme', 'HOMME'),
        ('Femme', 'FEMME'),
        ('Autres', 'AUTRES'),
    )
    genre = models.CharField(max_length=50, choices=GENRE, default='')
    # user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='userone')
    phone        = models.CharField(max_length=50, blank=False,)
    phone_fix    = models.CharField(max_length=50, blank=True, null=True)
    # phone_number = models.PhoneNumberField()
    img          = models.ImageField(upload_to='img/', blank=True, null=True)
    code         = models.CharField(max_length=2000)
    username     = models.CharField(max_length=200, blank=False, )
    first_name   = models.CharField(max_length=200, blank=False)
    last_name    = models.CharField(max_length=200, blank=False, null=True)
    email        = models.EmailField('email address', unique=True,blank=False)
    # date_birth   = models.DateField( blank=True, null=True)
    date_joined  = models.DateTimeField(auto_now_add=True)

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'phone', ]

    def get_full_name(self):
        # The user is identified by their email address
        return str(self.email)

    def get_short_name(self):
        # The user is identified by their email address
        return str(self.email)

    def __str__(self):  # __unicode__ on Python 2
        return str(self.email)

    @staticmethod
    def has_perm(perm, obj=None):
        # "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    @staticmethod
    def has_module_perms(app_label):
        # "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        # "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        # "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        # "Is the user active?"
        return self.active

    # class Meta:
    #     verbose_name = "user"
    #     verbose_name_plural = "users"

def pre_save_code_id(instance, sender, *args, **kwargs):
    if not instance.code:
            instance.code = unique_code_id_generator(instance)

pre_save.connect(pre_save_code_id, sender=User)

# class Profile(models.Model):
#     profile   = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     vendor_id = models.IntegerField()
#     visitor   = models.IntegerField()


# ==============================================
#                  MODELE ACCOUNTS
#                        END
# ==============================================

