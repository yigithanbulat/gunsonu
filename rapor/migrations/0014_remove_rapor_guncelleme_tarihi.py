# Generated by Django 3.2.9 on 2022-09-01 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rapor', '0013_auto_20220901_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rapor',
            name='guncelleme_tarihi',
        ),
    ]