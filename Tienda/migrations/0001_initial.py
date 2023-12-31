# Generated by Django 4.1.7 on 2023-07-28 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria_Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=55)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Categoria Producto',
                'verbose_name_plural': 'Categorias Productos',
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=55)),
                ('precio', models.FloatField()),
                ('disponibilidad', models.BooleanField()),
                ('imagen', models.ImageField(upload_to='Tienda')),
                ('categorias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.categoria_producto')),
            ],
            options={
                'verbose_name': ' Producto',
                'verbose_name_plural': ' Productos',
            },
        ),
    ]
