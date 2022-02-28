# Generated by Django 3.2.9 on 2022-02-16 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220204_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcel',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, default=0.0, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='parcel',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, default=0.0, max_digits=9, null=True),
        ),
    ]