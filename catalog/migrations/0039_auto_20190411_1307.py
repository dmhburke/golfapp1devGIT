# Generated by Django 2.2 on 2019-04-11 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0038_touragendamodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touragendamodel',
            name='time',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
