
from django.contrib import admin
from django.urls import path
from Area_matching.views import group_user_matching, index,user_reg,group,chat, signup, profile,create_profile,create_group,chatting
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index , name="index"),
    path('user_reg/',user_reg, name="user_reg"),
    #path('user_reg_eng/',user_reg_eng, name="user_reg_eng"),

    path('group/',group_user_matching, name="group"),
    #path('group_eng/',group_user_matching_eng, name="group_eng"),

    path('chat/',chat,name='chat'),
    #path('chat_eng/',chat_eng,name='chat_eng'),

    path('accounts/login/',auth_views.LoginView.as_view(), name = 'login'),
    path('accounts/login_eng/',auth_views.LoginView.as_view(),name='login_eng'),

    path('accounts/logout/' , auth_views.LogoutView.as_view(), name='logout'),

    path('accounts/signup/' , signup, name='signup'),
    #path('accounts/signup_eng/' , signup_eng, name='signup_eng'),

    path('accounts/profile/' , profile, name='profile'),
    #path('accounts/profile_eng/' , profile_eng, name='profile_eng'),

    path('accounts/profile/create/', create_profile, name='create_profile'),
    path('create-group/', create_group, name='create_group'),
    path('group/<int:id>/chat/', chatting, name='group_chat'),
    #path('group/<int:id>/chat/', chatting , name='group_chat'),
    #path('chat/<int:group>/chat/', chatting , name='group_chat'),
]