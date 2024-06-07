# Generated by Django 5.0.6 on 2024-06-07 19:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quizzes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='submitters',
            field=models.ManyToManyField(blank=True, null=True, related_name='quiz_submitters', to=settings.AUTH_USER_MODEL, verbose_name='Testni topshiradiganlar'),
        ),
        migrations.AddField(
            model_name='result',
            name='questions',
            field=models.ManyToManyField(blank=True, editable=False, null=True, related_name='result_questions', to='quizzes.question', verbose_name='Savollar'),
        ),
        migrations.AddField(
            model_name='result',
            name='quiz',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='quizzes.quiz', verbose_name='Test'),
        ),
        migrations.AddField(
            model_name='result',
            name='user',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.set', verbose_name="Test uchun savollar to'plami"),
        ),
        migrations.AddField(
            model_name='question',
            name='set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.set', verbose_name="To'plam"),
        ),
    ]
