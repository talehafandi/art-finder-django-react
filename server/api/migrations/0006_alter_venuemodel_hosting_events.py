# Generated by Django 4.2.4 on 2024-03-12 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_venuemodel_hosting_events_alter_venuemodel_lat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venuemodel',
            name='hosting_events',
            field=models.ManyToManyField(null=True, related_name='hosts', to='api.eventmodel'),
        ),
    ]