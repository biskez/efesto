# Generated by Django 3.2.7 on 2021-11-16 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='display',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='role',
            name='order',
            field=models.IntegerField(default=99),
        ),
    ]
