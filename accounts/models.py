from django.contrib.gis.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser
# from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models.signals import pre_save
from .utils import unique_code_id_generator

# ==============================================
#                  MODELE ACCOUNTS
#                        START
# ==============================================
class My_manager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True,is_staff=False, is_admin=False, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        # user_obj = self.model(email=self.normalize_email(email))
        user_obj = self.model(email=email, **extra_fields)
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj


    # def _create_user(self, email, password=None, **extra_fields):
    #     """Create and save a User with the given email and password."""
    #     if not email:
    #         raise ValueError('The given email must be set')
    #     user = self.model(email=email, **extra_fields)
    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user

    def create_superuser(self, email, password=None,
                         is_active=True, is_staff=False, is_admin=False,
                          **extra_fields):
        user_obj = self.model(email=email, **extra_fields)
        # user_obj = self.model(email=self.normalize_email(email))
        user_obj.set_password(password)
        user_obj.set_is_staff=True
        user_obj.set_is_admin=True
        user_obj.set_is_active=is_active

        user_obj.save(using=self._db)

        return self.create_user(email, password, **extra_fields)

    # def create_superuser(self, email, password=None, **extra_fields):
    #     """Create and save a SuperUser with the given email and password."""
    #     extra_fields.setdefault('is_staff', True)
    #     extra_fields.setdefault('is_superuser', True)
    #
    #     if extra_fields.get('is_staff') is not True:
    #         raise ValueError('Superuser must have is_staff=True.')
    #     if extra_fields.get('is_superuser') is not True:
    #         raise ValueError('Superuser must have is_superuser=True.')
    #
    #     return self._create_user(email, password, **extra_fields)

    # def create_agent(self, username, phone,
    #                   password=None, **extra_fields):
    #     user = self.create_user(
    #         phone,
    #         username,
    #         password=password,
    #         is_staff=True,
    #     )
    #     return user

class User(AbstractBaseUser):
    objects = My_manager()
    # id = models.AutoField(primary_key=True)
    GENRE = (
        ('Homme', 'HOMME'),
        ('Femme', 'FEMME'),
        ('Autres', 'AUTRES'),
    )
    genre = models.CharField(max_length=20, choices=GENRE, default='')
    # user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='userone')
    phone        = models.CharField(max_length=20, blank=True, null=True)
    phone_fix    = models.CharField(max_length=20, blank=True, null=True)
    img          = models.ImageField(upload_to='img/', blank=True, null=True)
    code         = models.CharField(max_length=2000)
    username     = models.CharField(max_length=200, blank=True, null=True)
    first_name   = models.CharField(max_length=200, blank=True, null=True)
    last_name    = models.CharField(max_length=200, blank=True, null=True)
    email        = models.EmailField('email address', unique=True)
    date_birth   = models.DateField()
    date_joined  = models.DateTimeField(auto_now_add=True)

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'phone']



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

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

def pre_save_code_id(instance, sender, *args, **kwargs):
    if not instance.code:
            instance.code = unique_code_id_generator(instance)

pre_save.connect(pre_save_code_id, sender=User)









# ==============================================
#                  MODELE ACCOUNTS
#                        END
# ==============================================

