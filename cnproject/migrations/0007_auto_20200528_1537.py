# Generated by Django 3.0.3 on 2020-05-28 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cnproject', '0006_auto_20200528_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='h2h',
            name='problem',
            field=models.CharField(max_length=5000),
        ),
    ]
