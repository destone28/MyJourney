# Generated by Django 2.1 on 2018-10-09 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_survey', '0003_auto_20181009_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domande',
            name='numero',
        ),
        migrations.RemoveField(
            model_name='risposte',
            name='numero_domanda',
        ),
    ]