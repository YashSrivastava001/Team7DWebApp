# Generated by Django 2.2.17 on 2021-03-23 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('designmytee', '0009_auto_20210323_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='title',
        ),
    ]