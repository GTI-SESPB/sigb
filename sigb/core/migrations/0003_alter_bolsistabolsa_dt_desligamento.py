# Generated by Django 5.1.5 on 2025-02-21 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_bolsistabolsa_delete_relacaobolistabolsa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bolsistabolsa',
            name='dt_desligamento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
