# Generated by Django 2.2.6 on 2019-12-20 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0002_auto_20191220_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date'),
        ),
    ]
