# Generated by Django 3.0.4 on 2020-03-31 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20200331_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encryptedprofile',
            name='data',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='historicalencryptedprofile',
            name='data',
            field=models.TextField(blank=True),
        ),
    ]
