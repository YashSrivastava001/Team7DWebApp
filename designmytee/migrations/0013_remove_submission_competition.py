# Generated by Django 2.2.17 on 2021-03-23 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('designmytee', '0012_auto_20210323_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='competition',
        ),
    ]