# Generated by Django 2.2 on 2019-04-04 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20190403_2041'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rd1slotmodel',
            options={'ordering': ['-player_stbl', 'player_name__HC']},
        ),
        migrations.AddField(
            model_name='rd1slotmodel',
            name='player_rankscore',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]