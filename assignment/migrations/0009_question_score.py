# Generated by Django 4.2.3 on 2024-02-15 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0008_quiz_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='score',
            field=models.IntegerField(default=1),
        ),
    ]