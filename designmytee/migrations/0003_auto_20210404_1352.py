# Generated by Django 2.2.17 on 2021-04-04 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('designmytee', '0002_auto_20210404_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='competition',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='designmytee.Competition'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='participant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='designmytee.Designer'),
        ),
    ]