# Generated by Django 2.2.17 on 2021-03-31 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designmytee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='competitionImage',
            field=models.ImageField(blank=True, upload_to='competition_images/'),
        ),
    ]
