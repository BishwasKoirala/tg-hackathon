# Generated by Django 5.1.2 on 2024-10-19 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Area_matching', '0002_remove_user_hobby_group_area_delete_hobby'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='group_id',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='chat',
            old_name='user_id',
            new_name='user',
        ),
    ]
