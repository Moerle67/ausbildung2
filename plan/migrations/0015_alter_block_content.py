# Generated by Django 5.1.1 on 2024-10-22 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0014_alter_gruppe_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='content',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Fach'),
        ),
    ]
