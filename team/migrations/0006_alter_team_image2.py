# Generated by Django 4.0.3 on 2022-09-27 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_team_image2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='images/team/'),
        ),
    ]
