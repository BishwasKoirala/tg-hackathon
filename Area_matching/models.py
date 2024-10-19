from django.db import models

# Create your models here.



class Area(models.Model) :
    area_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.area_name


# class Hobby(models.Model):
#     hobby_name = models.CharField(max_length=20)

#     def __str__(self):
#         return self.hobby_name


class User(models.Model):
    name = models.CharField(max_length=20) 
    area = models.ForeignKey(Area, on_delete=models.SET_NULL,null=True,related_name='user')
    # hobby = models.ManyToManyField(Hobby)

    def __str__(self):
        return self.name
    
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
