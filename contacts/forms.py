from crispy_forms.helper import FormHelper
from django import forms
from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

        exclude = ['domicile','email','image', 'contact_2','alias',
                    'code_person','photo', 'profession',
                    'responsable','date_naissance','nationalite','tutuelle',
                    'telephonique_fix','nina','numero_reference','created_at']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper(self)