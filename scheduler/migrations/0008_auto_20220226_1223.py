# Generated by Django 3.1.14 on 2022-02-26 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0007_auto_20220226_1221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goesto',
            old_name='client_id',
            new_name='client',
        ),
    ]