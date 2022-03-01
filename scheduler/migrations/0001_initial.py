# Generated by Django 3.1.14 on 2022-03-01 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0006_auto_20220220_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfirmationStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30, unique='True')),
            ],
        ),
        migrations.CreateModel(
            name='WorkingHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Therapy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('title', models.CharField(default='', max_length=50)),
                ('start', models.CharField(default='', max_length=20)),
                ('end', models.CharField(default='', max_length=50)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.client')),
                ('confirmation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.confirmationstatus')),
                ('psychologist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.psychologist')),
                ('workinghours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.workinghours')),
            ],
            options={
                'unique_together': {('date', 'workinghours', 'psychologist')},
            },
        ),
        migrations.CreateModel(
            name='GoesTo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.client')),
                ('psychologist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.psychologist')),
            ],
            options={
                'unique_together': {('client', 'psychologist')},
            },
        ),
    ]
