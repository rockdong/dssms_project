# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-26 13:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
            name='Organization',
            fields=[
                ('company_name', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='\u4f01\u4e1a\u540d\u79f0')),
                ('company_license', models.ImageField(upload_to='license/%s/', verbose_name='\u8425\u4e1a\u6267\u7167')),
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
            name='Role',
            fields=[
                ('role_name', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='\u89d2\u8272')),
                ('level', models.IntegerField(verbose_name='\u7ea7\u522b')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Organization', verbose_name='\u516c\u53f8')),
            ],
            options={
                'verbose_name': '\u804c\u6743',
                'verbose_name_plural': '\u804c\u6743',
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
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=20, verbose_name='\u59d3\u540d')),
                ('sex', models.CharField(choices=[('M', '\u7537'), ('F', '\u5973')], max_length=1, verbose_name='\u6027\u522b')),
                ('login_name', models.CharField(max_length=50, verbose_name='\u767b\u9646\u8d26\u53f7')),
                ('password', models.CharField(max_length=50, verbose_name='\u767b\u9646\u5bc6\u7801')),
                ('date_join', models.DateField(verbose_name='\u5165\u804c\u65f6\u95f4')),
                ('date_out', models.DateField(null=True, verbose_name='\u79bb\u804c\u65f6\u95f4')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Department', verbose_name='\u90e8\u95e8')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Organization', verbose_name='\u516c\u53f8')),
                ('skills', models.ManyToManyField(to='company.Skill', verbose_name='\u6280\u672f/\u80fd\u529b')),
            ],
            options={
                'verbose_name': '\u516c\u53f8\u6210\u5458',
                'verbose_name_plural': '\u516c\u53f8\u6210\u5458',
            },
        ),
        migrations.AddField(
            model_name='department',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Organization', verbose_name='\u516c\u53f8'),
        ),
        migrations.AddField(
            model_name='department',
            name='role',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='company.Role', verbose_name='\u804c\u6743'),
        ),
    ]
