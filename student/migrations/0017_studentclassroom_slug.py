# Generated by Django 4.2.3 on 2023-10-03 13:17

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0016_studentprofile_phone_number_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentclassroom',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, null=True),
        ),
    ]
