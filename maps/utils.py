import random

import string
# from django.db.models import
# =================================
#         CADASTRE RANDOM
#             START
# =================================
def random_string_generator():
    characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    result = ''
    for i in range(0, 20):
        result += random.choice(characters)
    return result

def unique_matricule_id_generator(instance):
    matricule_new_id = random_string_generator()

    Klass = instance.__class__

    qs_exists = Klass.objects.filter(matricule=matricule_new_id).exists()
    if qs_exists:
        return unique_matricule_id_generator(instance)
    return matricule_new_id

# =================================
#         CADASTRE RANDOM
#             END
# =================================