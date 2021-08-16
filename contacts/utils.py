import random

import string
# from django.db.models import



# =================================
#         CADASTRE RANDOM
#             START
# =================================
def random_string_generator():
    characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ-_'
    result = ''
    for i in range(0, 11):
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

# =================================
#         KALALISO RANDOM
#             START
# =================================
def random_string_generator():
    characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_'
    result = ''
    for i in range(0, 11):
        result += random.choice(characters)
    return result

def unique_product_id_generator(instance):
    code_produit_new_id = random_string_generator()

    Klass = instance.__class__

    qs_exists = Klass.objects.filter(code_produit=code_produit_new_id).exists()
    if qs_exists:
        return unique_product_id_generator(instance)
    return code_produit_new_id

def unique_order_id_generator(instance):
    code_order_new_id = random_string_generator()

    Klass = instance.__class__

    qs_exists = Klass.objects.filter(code_order=code_order_new_id).exists()
    if qs_exists:
        return unique_order_id_generator(instance)
    return code_order_new_id

def unique_person_id_generator(instance):
    code_person_new_id = random_string_generator()

    Klass = instance.__class__

    qs_exists = Klass.objects.filter(code_person=code_person_new_id).exists()
    if qs_exists:
        return unique_person_id_generator(instance)
    return code_person_new_id
# =================================
#         KALALISO RANDOM
#             END
# =================================