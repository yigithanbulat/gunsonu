# Generated by Django 3.2.9 on 2022-09-01 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapor', '0016_alter_rapor_yapilan_is_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rapor',
            name='yapilan_is_foto',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]
