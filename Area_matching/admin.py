from django.contrib import admin
from .models import Area,Chat,Group,UserProfile,UserChat
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Area)
admin.site.register(Group)
admin.site.register(Chat)
admin.site.register(UserChat)