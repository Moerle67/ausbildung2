# Generated by Django 5.1.1 on 2024-11-18 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0025_alter_log_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='daytime',
            field=models.CharField(choices=[('gr', 'Ganztags'), ('am', 'Vormittag'), ('pm', 'Nachmittag')], max_length=2, verbose_name='Tageszeit'),
        ),
    ]