# Generated by Django 4.2.3 on 2023-08-28 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_rename_student_studentclassroom_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentclassroom',
            old_name='teacher',
            new_name='responsible_teacher',
        ),
    ]
