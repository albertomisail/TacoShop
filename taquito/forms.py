from django import forms
from .models import Taco

class TacoAddForm(forms.Form):
    options = Taco.get_options()
    shell = forms.ChoiceField(choices=options['shell'])
    # Multiple of the following ingredients can be chosen so MultipleChoiceField is used
    base_layer = forms.MultipleChoiceField(choices=options['base_layer'])
    mixin = forms.MultipleChoiceField(choices=options['mixin'])
    condiment = forms.MultipleChoiceField(choices=options['condiment'])
    seasoning = forms.MultipleChoiceField(choices=options['seasoning'])