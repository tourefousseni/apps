from django.contrib.gis.db import models
import random
from random import randint
# from django.db.models.AutoField import *
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models.signals import pre_save
from .utils import unique_code_id_generator
# from .managers import

# ==============================================
#                  MODELE ACCOUNTS
#                        START
# ==============================================
class My_manager(BaseUserManager):
    def create_user(self, username, first_name, phone,
                    last_name, email, password=None, is_active=True,is_staff=False, is_admin=False, **extra_fields):
        if not first_name:
            raise ValueError("Users must have an first name")
        if not last_name:
            raise ValueError("Users must have an last name")
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        user = self.model(
            email=self.normalize_email(email)
        )
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.phone = phone
        user.set_password(password)
        user.staff = is_staff
        user.admin = is_admin
        user.active = is_active
        user.save(using=self._db)

        return user

        # user  = self.create_user(
        #     email,
        #     first_name,
        #     phone,
        #     last_name,
        #     username,
        #     password=password,
        #     is_staff=True,
        # )
        # return user

    def create_superuser(self, username, first_name, last_name,email, phone,
                           password=None, **extra_fields):
        user = self.create_user(
            phone,
            first_name,
            last_name,
            phone,
            password=password,
            is_staff=True,
            is_admin=True,
        )
        return user

    def create_agent(self, username, phone, email,
                     first_name, last_name, password=None, **extra_fields):
        user = self.create_user(
            email,
            first_name,
            last_name,
            phone,
            username,
            password=password,
            is_staff=True,
        )
        return user

class User(AbstractBaseUser):
    # id = models.AutoField(primary_key=True)
    # user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='userone')
    phone = models.CharField(max_length=20, blank=True, null=True)
    img = models.ImageField(upload_to='img/', blank=True, null=True)
    code = models.CharField(max_length=2000)
    username = models.CharField(max_length=200, blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField('email address', unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']

    objects= My_manager()

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

