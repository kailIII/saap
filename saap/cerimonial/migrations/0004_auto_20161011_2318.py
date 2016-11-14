# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-12 02:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('cerimonial', '0003_auto_20160924_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='processo',
            name='bairro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bairro_set', to='core.Bairro', verbose_name='Bairro da solicitação'),
        ),
        migrations.AddField(
            model_name='processo',
            name='data_solucao',
            field=models.DateField(blank=True, null=True, verbose_name='Data da solução'),
        ),
        migrations.AddField(
            model_name='processo',
            name='instituicao',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Instituição'),
        ),
        migrations.AddField(
            model_name='processo',
            name='orgao',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Órgão responsável'),
        ),
        migrations.AddField(
            model_name='processo',
            name='proto_cam',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='Protocolo da Câmara'),
        ),
        migrations.AddField(
            model_name='processo',
            name='proto_pref',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Protocolo da Prefeitura'),
        ),
        migrations.AddField(
            model_name='processo',
            name='protocolo',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Protocolo do Gabinete'),
        ),
        migrations.AddField(
            model_name='processo',
            name='rua',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Rua da solicitação'),
        ),
        migrations.AddField(
            model_name='processo',
            name='urgente',
            field=models.BooleanField(default=False, verbose_name='Rápido'),
        ),
    ]