from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Area(models.Model) :
    area_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.area_name


# class Hobby(models.Model):
#     hobby_name = models.CharField(max_length=20)

#     def __str__(self):
#         return self.hobby_name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname=models.CharField(max_length=10)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL,null=True,related_name='user')
    # hobby = models.ManyToManyField(Hobby)

    def __str__(self):
        return f"{self.user.username}'s profile"
    
class Group(models.Model) : 
    group_name = models.CharField(max_length=20)
    admin_user = models.ForeignKey(User, on_delete=models.SET_NULL , null=True , related_name='group')
    area = models.ForeignKey(Area, on_delete=models.CASCADE,null=True,related_name='area')
    
    # hobby = models.ManyToManyField(Hobby)

    def __str__(self):
        return self.group_name
    



class Chat(models.Model) :
    group = models.ForeignKey(Group, on_delete=models.CASCADE , related_name='chat')
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user')
    text = models.TextField(default=None)
    posted_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat by {self.user.username} in {self.group.group_name}"
    

class UserChat(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_chats')
    text = models.TextField(default=None)
    posted_at=models.DateTimeField(auto_now_add=True)
