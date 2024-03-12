# Generated by Django 4.2.4 on 2024-03-12 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_eventmodel_lat_eventmodel_long_venuemodel_lat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmodel',
            name='lat',
            field=models.DecimalField(decimal_places=6, default=55.8686, max_digits=9),
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='long',
            field=models.DecimalField(decimal_places=6, default=4.2906, max_digits=9),
        ),
        migrations.AlterField(
            model_name='venuemodel',
            name='lat',
            field=models.DecimalField(decimal_places=6, default=55.8686, max_digits=9),
        ),
        migrations.AlterField(
            model_name='venuemodel',
            name='long',
            field=models.DecimalField(decimal_places=6, default=4.2906, max_digits=9),
        ),
    ]
