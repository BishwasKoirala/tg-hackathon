from django.shortcuts import get_object_or_404, render
from .models import Area,Chat,Group,UserProfile
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from .forms import AreaSelectionForm, GroupForm,ChatForm
from django.core.exceptions import ObjectDoesNotExist



# Create your views here.


def index(request):
    users = User.objects.all()
    areas = Area.objects.all()
    return render(request,"Area_matching/index.html",{"users":users,"areas":areas})

def user_reg(request):
    user = User.objects.all()
    area = Area.objects.all()
    
    return render(request,"Area_matching/user_reg.html")

def user_reg_eng(request):
    user = User.objects.all()
    area = Area.objects.all()
    
    return render(request,"Area_matching/user_reg_eng.html")

def login_eng(request):
    return render(request,"registration/login_eng.html")

def group(request):
    group = Group.objects.all()
    return render(request,"Area_matching/group.html")

#def chat(request):
    #chat = Chat.objects.all()
    #return render(request,"Area_matching/chat.html")


def chat_eng(request):
    chat = Chat.objects.all()
    return render(request,"Area_matching/chat_eng.html")


###############ログイン機能まとめ#################

class CustomLoguinViews(LoginView): #ログイン機能
    template_name = "registration/login_eng.html"

def signup(request): #ユ－ザー登録機能
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid(): #form使えんの？
            user = form.save()
            login(request, user)
            return redirect('profle')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def profile(request): #プロフィール確認,編集機能(地域とかニックネーム)
    # UserProfileが存在するか確認
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    # UserProfileが新しく作成された場合、プロファイル作成ページにリダイレクト
    if created:
        return redirect('create_profile')  # 'create_profile'はプロファイル作成ページのURLパターン名

    if request.method == 'POST':
        form = AreaSelectionForm(request.POST)
        if form.is_valid():
            user_profile.area = form.cleaned_data['area']
            user_profile.nickname = form.cleaned_data['name']
            user_profile.save()
            return redirect('index')
    else:
        form = AreaSelectionForm()

    return render(request, 'accounts/profile.html', {
        'user_profile': user_profile,
        'form': form 
    })


@login_required
def create_profile(request): #プロフィール追加機能
    # 現在ログインしているユーザーを取得
    user = request.user

    # ユーザープロファイルがすでに存在するか確認
    try:
        user_profile = UserProfile.objects.get(user=user)
        return redirect('profile')  # プロファイルが存在する場合はプロフィールページへリダイレクト
    except UserProfile.DoesNotExist:
        # プロファイルが存在しない場合は新しいプロファイルを作成
        if request.method == 'POST':
            form = AreaSelectionForm(request.POST)
            if form.is_valid():
                user_profile = UserProfile(user=user,
                                            area=form.cleaned_data['area'],
                                            nickname =form.changed_data['name'])
                user_profile.save()
                return redirect('profile')  # 作成後はプロファイルページへリダイレクト
        else:
            form = AreaSelectionForm()

        return render(request, 'accounts/create_profile.html', {'form': form})

#################################################

##################Group作成######################同じエリアのグルーも撮ってくれる
@login_required
def create_group(request):
    user_profile = UserProfile.objects.get(user=request.user)
    user_area = user_profile.area
    groups = Group.objects.filter(area=user_area)  # ユーザーの地域に基づいてグループをフィルタリング

    user_profile = UserProfile.objects.get(user=request.user)
    user_area = user_profile.area
    matching_users = UserProfile.objects.filter(area = user_area)

    if request.method == 'POST':
        Group_form = GroupForm(request.POST)
        if Group_form.is_valid():
            group = Group_form.save(commit=False)
            group.admin_user = request.user
            group.save()
            return redirect('create_group')
    else:
        Group_form = GroupForm()
    # return render(request,'Area_matching/debug.html',{'Group_form':Group_form,'groups':groups,'matching_users':matching_users})
    return render(request,'Area_matching/debug.html',{'Group_form':Group_form,'groups':groups,'matching_users':matching_users})



def chatting(request,id):
    group = get_object_or_404(Group, id=id)
    chats = group.chat.all().order_by('posted_at') 
    form = ChatForm()
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.user = request.user
            chat.group = group
            chat.save()
            return redirect('group_chat',id=group.id)
        else:
            form.ChatForm()
    return render(request,'Area_matching/chat.html',{'form':form,'group': group, 'chats':chats})





#################################################

def group_user_matching(request):
    user_profile = UserProfile.objects.get(user=request.user)
    user_area = user_profile.area
    groups = Group.objects.filter(area=user_area)  # ユーザーの地域に基づいてグループをフィルタリング

    matching_users = UserProfile.objects.filter(area = user_area)

    if request.method == 'POST':
        Group_form = GroupForm(request.POST)
        if Group_form.is_valid():
            group = Group_form.save(commit=False)
            group.admin_user = request.user
            group.save()
            return redirect('group')
    else:
        Group_form = GroupForm()
    # return render(request,'Area_matching/debug.html',{'Group_form':Group_form,'groups':groups,'matching_users':matching_users})
    return render(request,'Area_matching/group.html',{'Group_form':Group_form,'groups':groups,'matching_users':matching_users})



# def people_matching(request):
#     user_profile = UserProfile.objects.get(user=request.user)
#     matching_users = UserProfile.objects.filter(area = user_area)

#     return render(request,"Area_matching/debug.html",{'matching_users':matching_users})