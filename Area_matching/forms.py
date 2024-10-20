from django import forms
from .models import Area,Group,Chat,UserChat


##プロフィール作成、編集用Form
class AreaSelectionForm(forms.Form):
    name = forms.CharField(max_length=10, label="Nickname", required=True)
    area = forms.ModelChoiceField(queryset=Area.objects.all(), label="Select your area", required=True)


##Group作成用フォーム
class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields= ['group_name', 'area']

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['text']
    def __init__(self, *args, **kwargs):
        super(ChatForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs["placeholder"] = field.label
            field.widget.attrs["style"] = "width: 700px; height: 50px; padding: 10px; font-size: 16px;"  # フォームの幅とスタイルを指定