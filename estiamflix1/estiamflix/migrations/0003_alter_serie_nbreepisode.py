# Generated by Django 4.1.2 on 2022-10-19 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estiamflix', '0002_alter_serie_nbreepisode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='nbreepisode',
            field=models.IntegerField(verbose_name='nombre episode'),
        ),
    ]