# Generated by Django 2.2 on 2019-04-12 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0044_sportstippingscoremodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sportstippingscoremodel',
            options={'ordering': ['total', '-time']},
        ),
    ]
