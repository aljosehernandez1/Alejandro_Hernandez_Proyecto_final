# Generated by Django 4.1.5 on 2023-01-29 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0005_curso_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('contenido', models.CharField(max_length=200)),
                ('image', models.URLField()),
                ('autor', models.CharField(max_length=50)),
            ],
        ),
    ]
