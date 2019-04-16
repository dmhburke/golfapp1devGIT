# Generated by Django 2.2 on 2019-04-16 20:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0056_auto_20190416_1352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rd3HoleModel',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('par', models.IntegerField(blank=True, null=True)),
                ('index', models.IntegerField(blank=True, null=True)),
                ('meters', models.IntegerField(blank=True, null=True)),
                ('CTP', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(4)])),
                ('LD', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(2)])),
                ('tussle', models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10, null=True)),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Rd3StablefordModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot1_stbl', models.IntegerField(blank=True, null=True)),
                ('slot2_stbl', models.IntegerField(blank=True, null=True)),
                ('slot3_stbl', models.IntegerField(blank=True, null=True)),
                ('slot4_stbl', models.IntegerField(blank=True, null=True)),
                ('slot5_stbl', models.IntegerField(blank=True, null=True)),
                ('slot6_stbl', models.IntegerField(blank=True, null=True)),
                ('slot7_stbl', models.IntegerField(blank=True, null=True)),
                ('slot8_stbl', models.IntegerField(blank=True, null=True)),
                ('slot9_stbl', models.IntegerField(blank=True, null=True)),
                ('slot10_stbl', models.IntegerField(blank=True, null=True)),
                ('slot11_stbl', models.IntegerField(blank=True, null=True)),
                ('slot12_stbl', models.IntegerField(blank=True, null=True)),
                ('hole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Rd3HoleModel')),
            ],
        ),
        migrations.CreateModel(
            name='Rd3SlotModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_slot', models.IntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)])),
                ('player_holesplayed', models.IntegerField(blank=True, null=True)),
                ('player_score', models.IntegerField(blank=True, null=True)),
                ('player_stbl', models.IntegerField(blank=True, null=True)),
                ('player_rankscore', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('player_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.PlayerModel')),
            ],
            options={
                'ordering': ['-player_rankscore', 'player_name__HC'],
            },
        ),
        migrations.CreateModel(
            name='Rd3ScoreModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot1_score', models.IntegerField(blank=True, null=True)),
                ('slot2_score', models.IntegerField(blank=True, null=True)),
                ('slot3_score', models.IntegerField(blank=True, null=True)),
                ('slot4_score', models.IntegerField(blank=True, null=True)),
                ('slot5_score', models.IntegerField(blank=True, null=True)),
                ('slot6_score', models.IntegerField(blank=True, null=True)),
                ('slot7_score', models.IntegerField(blank=True, null=True)),
                ('slot8_score', models.IntegerField(blank=True, null=True)),
                ('slot9_score', models.IntegerField(blank=True, null=True)),
                ('slot10_score', models.IntegerField(blank=True, null=True)),
                ('slot11_score', models.IntegerField(blank=True, null=True)),
                ('slot12_score', models.IntegerField(blank=True, null=True)),
                ('ctp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='RD3ctp', to='catalog.PlayerModel')),
                ('hole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Rd3HoleModel')),
                ('ld', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='RD3ld', to='catalog.PlayerModel')),
            ],
        ),
    ]
