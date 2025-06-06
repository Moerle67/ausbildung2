# Generated by Django 5.1.1 on 2025-04-07 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klausur', '0004_alter_klausurthema_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bewertung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.IntegerField(verbose_name='Note')),
                ('bewertung', models.CharField(max_length=50, verbose_name='Bewertung')),
            ],
            options={
                'verbose_name': 'Bewertung',
                'verbose_name_plural': 'Bewertungen',
            },
        ),
        migrations.CreateModel(
            name='IHK_key',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('punkte', models.IntegerField(verbose_name='Punkte/Prozent')),
                ('note', models.FloatField(verbose_name='Note')),
            ],
            options={
                'verbose_name': 'IHK Notenschlüssel',
                'verbose_name_plural': 'IHK Notenschlüssel',
            },
        ),
        migrations.AlterField(
            model_name='frage',
            name='inhalt',
            field=models.CharField(default='?', max_length=50, verbose_name='Überschrift'),
        ),
        migrations.AlterField(
            model_name='frage',
            name='titel',
            field=models.CharField(max_length=250, verbose_name='Thema'),
        ),
    ]
