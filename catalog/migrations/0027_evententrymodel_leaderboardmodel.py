# Generated by Django 2.2 on 2019-04-09 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0026_auto_20190409_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaderBoardModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_points', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.PlayerModel')),
            ],
            options={
                'ordering': ['total_points'],
            },
        ),
        migrations.CreateModel(
            name='EventEntryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True)),
                ('event', models.CharField(max_length=30)),
                ('points', models.IntegerField(blank=True, null=True)),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.PlayerModel')),
            ],
        ),
    ]
