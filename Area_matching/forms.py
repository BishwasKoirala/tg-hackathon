from django import forms
from .models import Area,Group


##プロフィール作成、編集用Form
class AreaSelectionForm(forms.Form):
    name = forms.CharField(max_length=10, label="Nickname", required=True)
    area = forms.ModelChoiceField(queryset=Area.objects.all(), label="Select your area", required=True)


##Group作成用フォーム
class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields= ['group_name', 'area']