# Generated by Django 5.1.2 on 2024-10-19 10:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Area_matching', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='hobby',
        ),
        migrations.AddField(
            model_name='group',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='area', to='Area_matching.area'),
        ),
        migrations.DeleteModel(
            name='Hobby',
        ),
    ]
