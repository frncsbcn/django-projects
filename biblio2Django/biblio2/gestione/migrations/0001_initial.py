# Generated by Django 5.0.4 on 2024-04-14 22:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=200)),
                ('autore', models.CharField(max_length=50)),
                ('pagine', models.IntegerField(default=100)),
            ],
            options={
                'verbose_name_plural': 'Libri',
            },
        ),
        migrations.CreateModel(
            name='Copia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_prestito', models.DateField(default=None, null=True)),
                ('scaduto', models.BooleanField(default=False)),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='copie', to='gestione.libro')),
            ],
            options={
                'verbose_name_plural': 'Copie',
            },
        ),
    ]
