from django import forms
from .models import Area

class AreaSelectionForm(forms.Form):
    name = forms.CharField(max_length=10, label="Nickname", required=True)
    area = forms.ModelChoiceField(queryset=Area.objects.all(), label="Select your area", required=True)
