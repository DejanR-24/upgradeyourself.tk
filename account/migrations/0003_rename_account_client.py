# Generated by Django 4.0.2 on 2022-02-07 20:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("account", "0002_account_delete_client"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Account",
            new_name="Client",
        ),
    ]
