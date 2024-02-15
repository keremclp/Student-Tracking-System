# Generated by Django 4.2.3 on 2024-02-15 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0006_useranswer_student_alter_useranswer_choice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice_set', to='assignment.question'),
        ),
    ]
