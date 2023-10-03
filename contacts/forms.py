from crispy_forms.helper import FormHelper
from django import forms
from contacts.models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['nom', 'prenom',
                  'contact_1', 'status','genre',
                  'type_tailleur','category',
                  'code_person',
                  ]

        exclude = ['domicile','image', 'email','alias','contact_2',
                    'photo', 'profession',
                    'responsable','date_naissance','nationalite','tutuelle',
                    'telephonique_fix','nina',
                   'carte_biometrique',
                   'numero_reference','created_at']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper(self)