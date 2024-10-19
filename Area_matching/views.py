from django.shortcuts import render
from .models import Area,Chat,Group,UserProfile
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from .forms import AreaSelectionForm
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

def group(request):
    group = Group.objects.all()
    return render(request,"Area_matching/group.html")

def chat(request):
    chat = Chat.objects.all()
    return render(request,"Area_matching/chat.html")

###############ログイン機能まとめ#################

class CustomLoguinViews(LoginView):
    template_name = "registration/login.html"

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def profile(request):
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

# プロファイル作成用の新しいビュー
def create_profile(request):
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