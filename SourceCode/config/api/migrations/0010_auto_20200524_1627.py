# Generated by Django 2.2.10 on 2020-05-24 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_league_league_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='region_rank',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='world_rank',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
