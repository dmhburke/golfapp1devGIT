# Generated by Django 2.2 on 2019-04-07 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0018_auto_20190407_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playerauthmodel',
            name='password',
        ),
    ]
