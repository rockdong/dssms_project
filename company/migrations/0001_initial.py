# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-09 10:03
from __future__ import unicode_literals

import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('staff_name', models.CharField(max_length=20, verbose_name='\u59d3\u540d')),
                ('sex', models.CharField(choices=[('M', '\u7537'), ('F', '\u5973')], max_length=1, verbose_name='\u6027\u522b')),
                ('date_join', models.DateField(auto_now_add=True, verbose_name='\u5165\u804c\u65f6\u95f4')),
                ('date_out', models.DateField(null=True, verbose_name='\u79bb\u804c\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u516c\u53f8\u6210\u5458',
                'verbose_name_plural': '\u516c\u53f8\u6210\u5458',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_name', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='\u90e8\u95e8\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u90e8\u95e8',
                'verbose_name_plural': '\u90e8\u95e8',
            },
        ),
        migrations.CreateModel(
            name='Duty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duty_name', models.CharField(max_length=20, verbose_name='\u804c\u4f4d\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u804c\u4f4d\u540d\u79f0',
                'verbose_name_plural': '\u804c\u4f4d\u540d\u79f0',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('company_name', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='\u4f01\u4e1a\u540d\u79f0')),
                ('corporation', models.CharField(max_length=20, verbose_name='\u6cd5\u4eba\u4ee3\u8868')),
                ('corporation_contact', models.CharField(max_length=20, verbose_name='\u8054\u7cfb\u65b9\u5f0f')),
                ('date_regedit', models.DateTimeField(auto_now_add=True, verbose_name='\u6ce8\u518c\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u4f01\u4e1a',
                'verbose_name_plural': '\u4f01\u4e1a',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('skill_name', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='\u6280\u672f')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Organization', verbose_name='\u516c\u53f8')),
            ],
            options={
                'verbose_name': '\u6280\u672f/\u80fd\u529b',
                'verbose_name_plural': '\u6280\u672f/\u80fd\u529b',
            },
        ),
        migrations.AddField(
            model_name='duty',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Organization', verbose_name='\u516c\u53f8'),
        ),
        migrations.AddField(
            model_name='department',
            name='duty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Duty', verbose_name='\u804c\u4f4d'),
        ),
        migrations.AddField(
            model_name='department',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Organization', verbose_name='\u516c\u53f8'),
        ),
        migrations.AddField(
            model_name='staff',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Department', verbose_name='\u90e8\u95e8'),
        ),
        migrations.AddField(
            model_name='staff',
            name='duty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Duty', verbose_name='\u804c\u4f4d'),
        ),
        migrations.AddField(
            model_name='staff',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='staff',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Organization', verbose_name='\u516c\u53f8'),
        ),
        migrations.AddField(
            model_name='staff',
            name='skills',
            field=models.ManyToManyField(to='company.Skill', verbose_name='\u6280\u672f/\u80fd\u529b'),
        ),
        migrations.AddField(
            model_name='staff',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
