# Generated by Django 4.0.4 on 2022-05-25 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stackusers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(max_length=999),
        ),
    ]
