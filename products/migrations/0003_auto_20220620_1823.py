# Generated by Django 3.2 on 2022-06-20 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220611_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='control_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='power_score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
