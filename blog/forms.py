from blog.models import Annonce
from crispy_forms.helper import FormHelper
from django import forms

class AnnonceForm(forms.ModelForm):
    class Meta:
        model = Annonce
        fields = ('__all__')
        exclude = ['shared','like','comment']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper(self)

