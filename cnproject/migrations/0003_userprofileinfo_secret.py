# Generated by Django 3.0.3 on 2020-05-23 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cnproject', '0002_remove_userprofileinfo_secret'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='secret',
            field=models.CharField(default='Yet to Fil', max_length=10),
        ),
    ]
