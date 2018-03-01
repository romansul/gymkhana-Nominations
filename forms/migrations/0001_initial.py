# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-20 09:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FilledForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(blank=True, max_length=30000, null=True)),
                ('applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(choices=[('Short_answer', 'One Line Answer'), ('Paragraph', 'Multiple Line Answer'), ('Integer', 'Integer Answer'), ('ChoiceField', 'Choice'), ('MultipleChoiceField', 'Multiple-choice')], max_length=50, null=True)),
                ('question', models.CharField(max_length=1000, null=True)),
                ('question_choices', models.TextField(blank=True, help_text='make new line for new option', max_length=600, null=True)),
                ('required', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='questionnaire',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.Questionnaire'),
        ),
        migrations.AddField(
            model_name='filledform',
            name='questionnaire',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.Questionnaire'),
        ),
    ]
