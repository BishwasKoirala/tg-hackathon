from django.shortcuts import render,redirect,get_object_or_404
from .models import Area,Chat,Group,User
from .forms import UserForm, AreaForm, GroupForm
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


################

def debug(request):
    users = User.objects.all()
    areas = Area.objects.all()
    return render(request,"Area_matching/makedata.html",{"users":users,"areas":areas})

def create_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            request.session['user_id'] = user.id
            return redirect('debug')  # ユーザーが作成されたらリダイレクト
    else:
        user_form = UserForm()
    
    return render(request, 'Area_matching/makedata.html', {'user_form': user_form})

def create_area(request):
    if request.method == 'POST':
        area_form = AreaForm(request.POST)
        if area_form.is_valid():
            area_form.save()
            return redirect('debug')  # エリアが作成されたらリダイレクト
    else:
        area_form = AreaForm()
    
    return render(request, 'Area_matching/makedata.html', {'area_form': area_form})


################
