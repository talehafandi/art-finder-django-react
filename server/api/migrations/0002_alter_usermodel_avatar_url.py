# Generated by Django 4.2.4 on 2024-03-03 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='avatar_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
