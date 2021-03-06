# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-20 09:38
from __future__ import unicode_literals

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('forms', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=100, null=True)),
                ('club_parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Club')),
            ],
        ),
        migrations.CreateModel(
            name='ClubCreate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=100, null=True)),
                ('club_parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Club')),
            ],
        ),
        migrations.CreateModel(
            name='Commment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Deratification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('end tenure', 'end tenure'), ('remove from post', 'remove from post'), ('deratified', 'deratified'), ('removed', 'removed')], default='safe', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='GroupNomination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000, null=True)),
                ('description', models.TextField(blank=True, max_length=5000, null=True)),
                ('status', models.CharField(choices=[('created', 'created'), ('out', 'out')], default='created', max_length=50)),
                ('opening_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('deadline', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nomination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=20000, null=True)),
                ('nomi_session', models.IntegerField(null=True)),
                ('status', models.CharField(choices=[('Nomination created', 'Nomination created'), ('Nomination out', 'Nomination out'), ('Interview period', 'Interview period'), ('Interview period and Reopening initiated', 'Interview period and Reopening initiated'), ('Interview period and Nomination reopened', 'Interview period and Nomination reopened'), ('Sent for ratification', 'Sent for ratification'), ('Work done', 'Work done')], default='Nomination created', max_length=50)),
                ('group_status', models.CharField(choices=[('normal', 'normal'), ('grouped', 'grouped')], default='normal', max_length=50)),
                ('opening_date', models.DateField(blank=True, null=True)),
                ('re_opening_date', models.DateField(blank=True, null=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('interview_panel', models.ManyToManyField(blank=True, related_name='panel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NominationInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default=None, max_length=20, null=True)),
                ('interview_status', models.CharField(blank=True, choices=[('Interview Not Done', 'Interview Not Done'), ('Interview Done', 'Interview Done')], default='Interview Not Done', max_length=20, null=True)),
                ('submission_status', models.BooleanField(default=False)),
                ('timestamp', models.DateField(default=django.utils.timezone.now)),
                ('edit_time', models.DateField(default=django.utils.timezone.now, null=True)),
                ('filled_form', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.FilledForm')),
                ('nomination', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Nomination')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.CharField(max_length=500, null=True)),
                ('status', models.CharField(choices=[('Post created', 'Post created'), ('Post approved', 'Post approved')], default='Post created', max_length=50)),
                ('perms', models.CharField(choices=[('normal', 'normal'), ('can ratify the post', 'can ratify the post'), ('can approve post and send nominations to users', 'can approve post and send nominations to users')], default='normal', max_length=200)),
                ('club', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Club')),
                ('elder_brother', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='little_bro', to='core.Post')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Post')),
                ('post_approvals', models.ManyToManyField(blank=True, related_name='approvals', to='core.Post')),
                ('post_holders', models.ManyToManyField(blank=True, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, related_name='club_posts', to='core.Club')),
                ('take_approval', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='give_approval', to='core.Post')),
            ],
        ),
        migrations.CreateModel(
            name='PostHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField(auto_now_add=True)),
                ('end', models.DateField(blank=True, null=True)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Post')),
            ],
        ),
        migrations.CreateModel(
            name='ReopenNomination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reopening_date', models.DateField(blank=True, null=True)),
                ('approvals', models.ManyToManyField(to='core.Post')),
                ('nomi', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Nomination')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_img', models.ImageField(blank=True, null=True, upload_to=core.models.user_directory_path)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('roll_no', models.IntegerField(null=True)),
                ('programme', models.CharField(choices=[('B.Tech', 'B.Tech'), ('B.S', 'B.S'), ('BS-MBA', 'BS-MBA'), ('BS-MS', 'BS-MS'), ('BS-MT', 'BS-MT'), ('BT-M.Des', 'BT-M.Des'), ('BT-MBA', 'BT-MBA'), ('BT-MS', 'BT-MS'), ('Exchng Prog.', 'Exchng Prog.'), ('MBA', 'MBA'), ('MDes', 'MDes'), ('MS-Research', 'MS-Research'), ('MSc(2 yr)', 'MSc(2 yr)'), ('MSc(Int)', 'MSc(Int)'), ('MT(Dual)', 'MT(Dual)'), ('MTech', 'MTech'), ('PGPEX-VLM', 'PGPEX-VLM'), ('PhD', 'PhD'), ('PhD(Dual)', 'PhD(Dual)'), ('Prep.', 'Prep.'), ('SURGE', 'SURGE')], default='B.Tech', max_length=100)),
                ('department', models.CharField(default='AE', max_length=200)),
                ('hall', models.CharField(default=1, max_length=10)),
                ('room_no', models.CharField(blank=True, max_length=10, null=True)),
                ('contact', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='posthistory',
            name='post_session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Session'),
        ),
        migrations.AddField(
            model_name='posthistory',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='nomination',
            name='nomi_approvals',
            field=models.ManyToManyField(blank=True, related_name='nomi_approvals', to='core.Post'),
        ),
        migrations.AddField(
            model_name='nomination',
            name='nomi_form',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.Questionnaire'),
        ),
        migrations.AddField(
            model_name='nomination',
            name='nomi_post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Post'),
        ),
        migrations.AddField(
            model_name='nomination',
            name='result_approvals',
            field=models.ManyToManyField(blank=True, related_name='result_approvals', to='core.Post'),
        ),
        migrations.AddField(
            model_name='nomination',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='club_nomi', to='core.Club'),
        ),
        migrations.AddField(
            model_name='groupnomination',
            name='approvals',
            field=models.ManyToManyField(blank=True, related_name='group_approvals', to='core.Post'),
        ),
        migrations.AddField(
            model_name='groupnomination',
            name='nominations',
            field=models.ManyToManyField(blank=True, to='core.Nomination'),
        ),
        migrations.AddField(
            model_name='groupnomination',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='club_group', to='core.Club'),
        ),
        migrations.AddField(
            model_name='deratification',
            name='deratify_approval',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_deratify', to='core.Post'),
        ),
        migrations.AddField(
            model_name='deratification',
            name='name',
            field=models.ForeignKey(max_length=30, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='deratification',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Post'),
        ),
        migrations.AddField(
            model_name='commment',
            name='nomi_instance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.NominationInstance'),
        ),
        migrations.AddField(
            model_name='commment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='clubcreate',
            name='requested_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='club_request', to='core.Post'),
        ),
        migrations.AddField(
            model_name='clubcreate',
            name='take_approval',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='give_club_approval', to='core.Post'),
        ),
    ]
