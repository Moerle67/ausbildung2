# Generated by Django 4.2.7 on 2024-09-10 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('klausur', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teilnehmer',
            options={'ordering': ['name'], 'verbose_name': 'Teilnehmer', 'verbose_name_plural': 'Teilnehmer'},
        ),
        migrations.AlterModelOptions(
            name='thema',
            options={'ordering': ['titel'], 'verbose_name': 'Thema', 'verbose_name_plural': 'Themen'},
        ),
        migrations.AddField(
            model_name='frage',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='klausur',
            name='titel',
            field=models.CharField(max_length=50, verbose_name='Überschrift'),
        ),
    ]