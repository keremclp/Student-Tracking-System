# Generated by Django 4.2.3 on 2024-02-17 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0017_studentclassroom_slug'),
        ('assignment', '0014_alter_uploadedsolution_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignmentfile',
            name='classroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.studentclassroom'),
        ),
    ]