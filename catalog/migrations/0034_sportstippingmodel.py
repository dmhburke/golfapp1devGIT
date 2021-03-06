# Generated by Django 2.2 on 2019-04-10 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0033_delete_sportstippingmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SportsTippingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, max_length=30, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('game1', models.CharField(blank=True, choices=[('PLAYER_1', 'Player 1'), ('PLAYER_2', 'Player 2'), ('TIED', 'Tied')], max_length=10, null=True)),
                ('game2', models.CharField(blank=True, choices=[('PLAYER_1', 'Player 1'), ('PLAYER_2', 'Player 2'), ('TIED', 'Tied')], max_length=10, null=True)),
                ('game3', models.CharField(blank=True, choices=[('PLAYER_1', 'Player 1'), ('PLAYER_2', 'Player 2'), ('TIED', 'Tied')], max_length=10, null=True)),
                ('game4', models.CharField(blank=True, choices=[('PLAYER_1', 'Player 1'), ('PLAYER_2', 'Player 2'), ('TIED', 'Tied')], max_length=10, null=True)),
                ('game5', models.CharField(blank=True, choices=[('PLAYER_1', 'Player 1'), ('PLAYER_2', 'Player 2'), ('TIED', 'Tied')], max_length=10, null=True)),
                ('game6', models.CharField(blank=True, choices=[('PLAYER_1', 'Player 1'), ('PLAYER_2', 'Player 2'), ('TIED', 'Tied')], max_length=10, null=True)),
                ('game7', models.CharField(blank=True, choices=[('PLAYER_1', 'Player 1'), ('PLAYER_2', 'Player 2'), ('TIED', 'Tied')], max_length=10, null=True)),
                ('game8', models.CharField(blank=True, choices=[('PLAYER_1', 'Player 1'), ('PLAYER_2', 'Player 2'), ('TIED', 'Tied')], max_length=10, null=True)),
                ('game9', models.CharField(blank=True, choices=[('PLAYER_1', 'Player 1'), ('PLAYER_2', 'Player 2'), ('TIED', 'Tied')], max_length=10, null=True)),
                ('game10', models.CharField(blank=True, choices=[('PLAYER_1', 'Player 1'), ('PLAYER_2', 'Player 2'), ('TIED', 'Tied')], max_length=10, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.PlayerModel')),
            ],
        ),
    ]
