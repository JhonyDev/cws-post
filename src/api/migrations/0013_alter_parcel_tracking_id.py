# Generated by Django 4.0.5 on 2022-06-28 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20220325_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcel',
            name='tracking_id',
            field=models.CharField(blank=True, default='04bf7652', max_length=100, unique=True),
        ),
    ]
