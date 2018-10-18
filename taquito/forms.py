from django import forms
from .models import Taco

class TacoAddForm(forms.Form):
    options = Taco.get_options()
    shell = forms.ChoiceField(choices=options['shell'])
    base_layer = forms.MultipleChoiceField(choices=options['base_layer'])
    mixin = forms.MultipleChoiceField(choices=options['mixin'])
    condiment = forms.MultipleChoiceField(choices=options['condiment'])
    seasoning = forms.MultipleChoiceField(choices=options['seasoning'])