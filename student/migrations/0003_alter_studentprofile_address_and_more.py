# Generated by Django 4.2.3 on 2023-08-14 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_interest_studentprofile_address_studentprofile_bio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='birth_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='interests',
            field=models.ManyToManyField(blank=True, to='student.interest'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='student_id',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
