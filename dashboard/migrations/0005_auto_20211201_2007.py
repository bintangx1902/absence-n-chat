# Generated by Django 3.2.8 on 2021-12-01 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20211126_0101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userextended',
            name='is_upper',
        ),
        migrations.AddField(
            model_name='agencyname',
            name='img',
            field=models.FileField(blank=True, upload_to='agency/'),
        ),
    ]
