# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-11 01:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_content', models.CharField(max_length=50, verbose_name='\u884c\u4e3a')),
                ('action_type', models.CharField(choices=[('0', '\u4e00\u822c\u884c\u4e3a'), ('1', '\u8bbe\u8ba1\u56fe'), ('3', '\u62a5\u4ef7'), ('4', '\u5408\u540c')], max_length=20, verbose_name='\u884c\u4e3a\u7c7b\u578b')),
            ],
            options={
                'verbose_name': '\u884c\u4e3a',
                'verbose_name_plural': '\u884c\u4e3a',
            },
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '\u9879\u76ee\u53c2\u4e0e\u8005',
                'verbose_name_plural': '\u9879\u76ee\u53c2\u4e0e\u8005',
            },
        ),
        migrations.CreateModel(
            name='Actual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('act_st_date', models.DateField(verbose_name='\u9879\u76ee\u5b9e\u9645\u5f00\u59cb\u65f6\u95f4')),
                ('act_ed_date', models.DateField(verbose_name='\u9879\u76ee\u5b9e\u9645\u7ed3\u675f\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u9879\u76ee\u5b9e\u9645\u65f6\u95f4',
                'verbose_name_plural': '\u9879\u76ee\u5b9e\u9645\u65f6\u95f4',
            },
        ),
        migrations.CreateModel(
            name='PlanFlow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pre_st_date', models.DateField(verbose_name='\u9879\u76ee\u9884\u8ba1\u5f00\u59cb\u65f6\u95f4')),
                ('pre_ed_date', models.DateField(verbose_name='\u9879\u76ee\u9884\u8ba1\u7ed3\u675f\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u9879\u76ee\u8ba1\u5212\u65f6\u95f4',
                'verbose_name_plural': '\u9879\u76ee\u8ba1\u5212\u65f6\u95f4',
            },
        ),
        migrations.CreateModel(
            name='Pro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=50, verbose_name='\u9879\u76ee\u7f16\u53f7')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Organization', verbose_name='\u516c\u53f8')),
            ],
            options={
                'verbose_name': '\u9879\u76ee',
                'verbose_name_plural': '\u9879\u76ee',
            },
        ),
        migrations.CreateModel(
            name='ProFlowBlank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_flow_name', models.CharField(max_length=50, verbose_name='\u9879\u76ee\u6d41\u7a0b\u5757')),
                ('pro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Pro', verbose_name='\u9879\u76ee')),
            ],
            options={
                'verbose_name': '\u9879\u76ee\u6d41\u7a0b\u5757',
                'verbose_name_plural': '\u9879\u76ee\u6d41\u7a0b\u5757',
            },
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='QuotationTemp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='planflow',
            name='pro_flow_blank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.ProFlowBlank', verbose_name='\u9879\u76ee\u6d41\u7a0b\u5757'),
        ),
        migrations.AddField(
            model_name='actual',
            name='pro_flow_blank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.ProFlowBlank', verbose_name='\u9879\u76ee\u6d41\u7a0b\u5757'),
        ),
        migrations.AddField(
            model_name='actor',
            name='pro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Pro', verbose_name='\u9879\u76ee'),
        ),
        migrations.AddField(
            model_name='actor',
            name='pro_actors',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='\u9879\u76ee\u53c2\u4e0e\u8005'),
        ),
        migrations.AddField(
            model_name='action',
            name='pro_flow_blank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.ProFlowBlank', verbose_name='\u9879\u76ee\u6d41\u7a0b\u5757'),
        ),
    ]
