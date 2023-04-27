from django.contrib.gis.db import models
# from django.contrib.gis.db.models
import random
from random import randint
# from django.db.models.AutoField import *
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from .utils import unique_code_id_generator

from .validators import file_size


# ==============================================
#                  MODELE ACCOUNTS
#                        START
# ==============================================
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    # user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='userone')
    phone = models.CharField(max_length=20, blank=True, null=True)
    img = models.ImageField(upload_to='img/', blank=True, null=True)
    code = models.CharField(max_length=2000)

    def __str__(self):
        return str(self.email)

def pre_save_code_id(instance, sender, *args, **kwargs):
    if not instance.code:
            instance.code = unique_code_id_generator(instance)

pre_save.connect(pre_save_code_id, sender=User)
# ==============================================
#                  MODELE ACCOUNTS
#                        END
# ==============================================

