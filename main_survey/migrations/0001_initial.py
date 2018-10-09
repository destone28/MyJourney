# Generated by Django 2.1 on 2018-10-09 13:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domande',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lingua', models.TextField()),
                ('numero', models.PositiveSmallIntegerField()),
                ('testo_domanda', models.TextField()),
                ('categoria', models.TextField()),
                ('suggerimento', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Logtable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quando', models.DateTimeField(default=django.utils.timezone.now)),
                ('lingua', models.TextField()),
                ('uno', models.TextField()),
                ('due', models.TextField()),
                ('tre', models.TextField()),
                ('quattro', models.TextField()),
                ('cinque', models.TextField()),
                ('sei', models.DateField()),
                ('sette', models.DateField()),
                ('otto', models.BooleanField()),
                ('nove', models.TextField()),
                ('dieci', models.BooleanField()),
                ('undici', models.TextField()),
                ('dodici', models.BooleanField()),
                ('tredici', models.BooleanField()),
                ('quattordici', models.BooleanField()),
                ('quindici', models.TextField()),
                ('sedici', models.BooleanField()),
                ('diciassette', models.TextField()),
                ('diciotto', models.TextField()),
                ('diciannove', models.BooleanField()),
                ('venti', models.BooleanField()),
                ('ventuno', models.BooleanField()),
                ('ventidue', models.TextField()),
                ('ventitre', models.BooleanField()),
                ('ventiquattro', models.BooleanField()),
                ('venticinque', models.BooleanField()),
                ('idoneo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Risposte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lingua', models.TextField()),
                ('numero', models.PositiveSmallIntegerField()),
                ('testo', models.TextField()),
                ('data', models.DateField()),
                ('booleano', models.BooleanField()),
                ('intero', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='domande',
            name='risposta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_survey.Risposte'),
        ),
    ]
