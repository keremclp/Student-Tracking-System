# Generated by Django 4.2.3 on 2023-09-15 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_remove_studentclassroom_student_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofile',
            name='classroom',
        ),
    ]