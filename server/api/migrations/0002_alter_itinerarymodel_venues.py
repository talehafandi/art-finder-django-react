# Generated by Django 4.2.4 on 2024-03-14 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itinerarymodel',
            name='venues',
            field=models.ManyToManyField(related_name='itineraries', to='api.venuemodel'),
        ),
    ]