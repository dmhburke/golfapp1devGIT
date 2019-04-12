# Generated by Django 2.2 on 2019-04-12 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0043_sportstippingresultsmodel_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='SportsTippingScoreModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.PlayerModel')),
            ],
        ),
    ]
