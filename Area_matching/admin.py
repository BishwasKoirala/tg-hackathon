from django.contrib import admin
from .models import Area,Chat,Group,User
# Register your models here.

admin.site.register(User)
admin.site.register(Area)
admin.site.register(Group)
admin.site.register(Chat)