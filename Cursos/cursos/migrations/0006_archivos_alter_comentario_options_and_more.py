# Generated by Django 4.0.5 on 2022-08-03 19:59

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0005_comentario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archivos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Clave')),
                ('nombre', models.CharField(max_length=100, null=True, verbose_name='Nombre')),
                ('email', models.CharField(max_length=100, null=True, verbose_name='Correo')),
                ('mensaje', models.TextField(null=True, verbose_name='Mensaje')),
                ('archivo', models.FileField(blank=True, null=True, upload_to='archivos')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('update', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Actualizacion')),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contacto',
                'ordering': ['-created'],
            },
        ),
        migrations.AlterModelOptions(
            name='comentario',
            options={'ordering': ['-created'], 'verbose_name': 'Comentario', 'verbose_name_plural': 'Comentarios'},
        ),
        migrations.AlterField(
            model_name='comentario',
            name='coment',
            field=ckeditor.fields.RichTextField(verbose_name='Comentario'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.cursos', verbose_name='Curso Elegido'),
        ),
    ]
