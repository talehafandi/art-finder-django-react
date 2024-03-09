# Generated by Django 4.1 on 2024-03-03 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=16, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('role', models.CharField(choices=[('user', 'User'), ('organiser', 'Organiser'), ('admin', 'Admin')], default='user', max_length=20)),
                ('avatar_url', models.URLField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('event_category', models.CharField(choices=[('AR', 'ART'), ('PH', 'PHOTOGRAPHY'), ('SU', 'SCULPTURE'), ('CR', 'CRAFTS')], default='AR', max_length=2)),
                ('fee', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='VenueModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=200)),
                ('address', models.CharField(default='', max_length=40)),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('contact_email', models.EmailField(default='example@example.com', max_length=254, unique=True)),
                ('contact_phone_number', phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128, region=None)),
                ('venue_category', models.CharField(blank=True, choices=[('MU', 'MUSEUM'), ('GA', 'GALLERY')], max_length=2, null=True)),
                ('hosting_events', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hosts', to='api.eventmodel')),
            ],
        ),
        migrations.CreateModel(
            name='WishlistModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('events', models.ManyToManyField(related_name='wishlists', to='api.eventmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('venues', models.ManyToManyField(related_name='wishlists', to='api.venuemodel')),
            ],
        ),
        migrations.CreateModel(
            name='ItineraryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('description', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('events', models.ManyToManyField(related_name='itineraries', to='api.eventmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itineraries', to=settings.AUTH_USER_MODEL)),
                ('venues', models.ManyToManyField(related_name='itineraries', to='api.venuemodel')),
            ],
        ),
        migrations.AddField(
            model_name='eventmodel',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hosted_in', to='api.venuemodel'),
        ),
        migrations.CreateModel(
            name='BookingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_tickets', models.IntegerField()),
                ('booking_date', models.DateField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.eventmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'event')},
            },
        ),
    ]
