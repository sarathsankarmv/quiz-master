# Generated by Django 2.2 on 2020-11-02 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizsubmission',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
    ]
