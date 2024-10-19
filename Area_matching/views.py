from django.shortcuts import render
from .models import Area,Chat,Group,User
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
