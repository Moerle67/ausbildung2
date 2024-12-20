# Generated by Django 5.1.1 on 2024-10-15 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0002_alter_gruppe_options_alter_gruppe_short_block'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='block',
            options={'ordering': ['group', 'year', 'kw', 'day', 'daytime'], 'verbose_name': 'Block', 'verbose_name_plural': 'Blöcke'},
        ),
        migrations.AddField(
            model_name='block',
            name='kw',
            field=models.IntegerField(default=1, verbose_name='Kalenderwoche'),
            preserve_default=False,
        ),
    ]
