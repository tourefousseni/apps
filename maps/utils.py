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
    for i in range(0, 10):
        result += random.choice(characters)
    return result

def unique_parcel_id_generator(instance):
    parcel_new_id = random_string_generator()

    Klass = instance.__class__

    qs_exists = Klass.objects.filter(code_parcel=parcel_new_id).exists()
    if qs_exists:
        return unique_parcel_id_generator(instance)
    return parcel_new_id

# =================================
#         CADASTRE RANDOM
#             END
# =================================