# Generated by Django 3.2.9 on 2022-09-01 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapor', '0004_auto_20220901_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rapor',
            name='guncelleme_tarihi',
            field=models.DateField(auto_now=True),
        ),
    ]