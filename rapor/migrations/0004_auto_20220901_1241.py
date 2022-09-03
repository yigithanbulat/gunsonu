# Generated by Django 3.2.9 on 2022-09-01 09:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rapor', '0003_auto_20220901_0113'),
    ]

    operations = [
        migrations.AddField(
            model_name='rapor',
            name='ekleme_tarihi',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rapor',
            name='guncelleme_tarihi',
            field=models.DateTimeField(auto_now=True),
        ),
    ]