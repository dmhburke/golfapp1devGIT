# Generated by Django 2.2 on 2019-04-07 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0019_remove_playerauthmodel_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerauthmodel',
            name='passwordset',
            field=models.CharField(default='password', max_length=30),
        ),
    ]
