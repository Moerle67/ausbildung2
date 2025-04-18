# Generated by Django 5.1.1 on 2024-10-17 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0007_delete_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Bezeichnung')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Beschreibung')),
                ('activ', models.BooleanField(default=True, verbose_name='Aktiv')),
                ('groups', models.ManyToManyField(to='plan.gruppe', verbose_name='Gruppen')),
                ('members', models.ManyToManyField(to='plan.ausbilder', verbose_name='Ausbilder')),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
                'ordering': ['name'],
            },
        ),
    ]
