# Generated by Django 5.1.1 on 2024-11-26 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0028_alter_team_groups_alter_team_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aubiblock',
            name='daytime',
            field=models.CharField(choices=[('gt', 'Ganztag'), ('am', 'Vormittag'), ('pm', 'Nachmittag')], default='gt', max_length=2, verbose_name='Tageszeit'),
        ),
    ]
