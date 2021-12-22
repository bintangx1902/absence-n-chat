# Generated by Django 3.2.8 on 2021-12-22 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_alter_presencerecap_qr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presencerecap',
            name='qr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qr_c', related_query_name='qr_c', to='dashboard.qrcodegenerator'),
        ),
    ]
