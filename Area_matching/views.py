from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,"Area_matching/index.html")

def user_reg(request):
    return render(request,"Area_matching/user_reg.html")

def group(request):
    return render(request,"Area_matching/group.html")

def chat(request):
    return render(request,"Area_matching/chat.html")