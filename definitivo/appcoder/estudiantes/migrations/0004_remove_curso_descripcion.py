# Generated by Django 4.1.5 on 2023-01-22 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0003_curso_descripcion_alter_curso_duracion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='descripcion',
        ),
    ]