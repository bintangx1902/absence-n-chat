# Generated by Django 3.2.8 on 2021-12-22 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20211221_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcodegenerator',
            name='qr_code',
            field=models.SlugField(unique=True),
        ),
    ]