# Generated by Django 2.2 on 2019-04-06 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_rd1scoremodel_ctp1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rd1scoremodel',
            old_name='ctp1',
            new_name='ctp1_score',
        ),
    ]