# Generated by Django 2.2 on 2020-11-02 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_quizsubmission_is_correct'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizresult',
            name='achieved_score',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quizresult',
            name='attended',
            field=models.IntegerField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quizresult',
            name='correct_ans',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quizresult',
            name='incorrect_ans',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quizresult',
            name='total_score',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
