# Generated by Django 4.0.3 on 2022-09-27 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_news_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='assets/images/news'),
        ),
    ]
