# Generated by Django 4.2.2 on 2023-08-05 14:02

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0002_alter_usuario_apellidos_alter_usuario_nombres'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='usuario',
            managers=[
                ('objeto', django.db.models.manager.Manager()),
            ],
        ),
    ]