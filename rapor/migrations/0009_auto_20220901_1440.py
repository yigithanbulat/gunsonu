# Generated by Django 3.2.9 on 2022-09-01 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapor', '0008_rapor_raporss'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rapor',
            name='raporss',
        ),
        migrations.AddField(
            model_name='rapor',
            name='görüntüle',
            field=models.CharField(default='Raporu Görüntüle', max_length=5),
        ),
    ]
