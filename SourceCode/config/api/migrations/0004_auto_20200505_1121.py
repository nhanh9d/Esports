# Generated by Django 2.2.10 on 2020-05-05 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='display_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
