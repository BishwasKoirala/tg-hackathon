from django import forms
from .models import User,Area,Group

class UserForm(forms.ModelForm):
     class Meta:
        model = User
        fields = ['name', 'area']  # フォームに含めるフィールドを指定
        widgets = {
            'area': forms.Select(),  # エリアを選択フィールドにする
        }




class AreaForm(forms.ModelForm): #Area登録
    class Meta:
        model = Area
        fields = ['area_name']

class GroupForm(forms.ModelForm): #グループ登録
    class Meta:
        model = Group
        fields = ['group_name' , 'area']
        widgets = {
            'area': forms.Select(),  # エリアを選択フィールドにする
        }