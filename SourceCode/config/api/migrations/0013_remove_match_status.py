# Generated by Django 2.2.10 on 2020-07-05 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20200524_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='status',
        ),
    ]