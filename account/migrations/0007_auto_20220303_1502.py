# Generated by Django 3.1.14 on 2022-03-03 15:02

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20220220_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile_picture',
            field=models.ImageField(default='profile_picetur/avatar.jpg', upload_to=account.models.upload_to, verbose_name='Image'),
        ),
    ]