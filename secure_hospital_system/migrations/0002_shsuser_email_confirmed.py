# Generated by Django 3.2.5 on 2022-04-02 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secure_hospital_system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shsuser',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
