# Generated by Django 2.1 on 2020-04-26 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('fullname', models.CharField(max_length=255)),
            ],
        ),
    ]
