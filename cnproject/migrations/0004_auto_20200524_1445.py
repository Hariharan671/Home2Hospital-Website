# Generated by Django 3.0.3 on 2020-05-24 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cnproject', '0003_userprofileinfo_secret'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='bp',
            new_name='blood_pressure',
        ),
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='bt',
            new_name='body_temperature',
        ),
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='hs',
            new_name='hand_sanitizer',
        ),
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='mk',
            new_name='mask',
        ),
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='pv',
            new_name='proper_ventilation',
        ),
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='wc',
            new_name='wheel_chair',
        ),
    ]
