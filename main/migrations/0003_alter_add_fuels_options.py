# Generated by Django 4.2.11 on 2024-03-19 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_add_fuels'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='add_fuels',
            options={'ordering': ['-time']},
        ),
    ]
