# Generated by Django 5.0.4 on 2024-04-17 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iscrizioni', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studente',
            old_name='surname',
            new_name='cognome',
        ),
        migrations.RenameField(
            model_name='studente',
            old_name='name',
            new_name='nome',
        ),
    ]
