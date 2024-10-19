
from django.contrib import admin
from django.urls import path
from Area_matching.views import index,user_reg,group,chat, signup, profile,create_profile,create_group
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index , name="index"),
    path('user_reg/',user_reg, name="user_reg"),
    path('group/',group, name="group"),
    path('chat/',chat,name='chat'),
    path('accounts/login/',auth_views.LoginView.as_view(), name = 'login'),
    path('accounts/logout/' , auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/signup/' , signup, name='signup'),
    path('accounts/profile/' , profile, name='profile'),
    path('accounts/profile/create/', create_profile, name='create_profile'),
    path('create-group/', create_group, name='create_group'),
]
