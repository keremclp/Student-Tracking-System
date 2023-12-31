# Generated by Django 4.2.3 on 2023-08-10 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_user_is_parent_remove_user_is_student_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default=1, upload_to='profile_image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('student', 'Student'), ('teacher', 'Teacher'), ('parent', 'Parent')], max_length=200),
        ),
    ]
