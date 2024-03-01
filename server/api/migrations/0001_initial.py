# Generated by Django 4.2.4 on 2024-03-01 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('eventCategory', models.CharField(choices=[('AR', 'ART'), ('PH', 'PHOTOGRAPHY'), ('SU', 'SCULPTURE'), ('CR', 'CRAFTS')], default='AR', max_length=2)),
                ('fee', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='VenueModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=200)),
                ('openTime', models.TimeField()),
                ('closeTime', models.TimeField()),
                ('contactEmail', models.EmailField(max_length=254)),
                ('venueCategory', models.CharField(blank=True, choices=[('MU', 'MUSEUM'), ('GA', 'GALLERY')], max_length=2, null=True)),
                ('hostingEvents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hosts', to='api.eventmodel')),
            ],
        ),
        migrations.AddField(
            model_name='eventmodel',
            name='venue',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hosted_in', to='api.venuemodel'),
        ),
    ]
