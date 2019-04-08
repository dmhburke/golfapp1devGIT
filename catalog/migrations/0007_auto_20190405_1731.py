# Generated by Django 2.2 on 2019-04-05 21:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20190404_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rd1holemodel',
            name='CTP',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(4)]),
        ),
        migrations.CreateModel(
            name='CTPModel',
            fields=[
                ('CTPnumber', models.IntegerField(primary_key=True, serialize=False)),
                ('number', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Rd1HoleModel')),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.PlayerModel')),
            ],
            options={
                'ordering': ['CTPnumber'],
            },
        ),
    ]
