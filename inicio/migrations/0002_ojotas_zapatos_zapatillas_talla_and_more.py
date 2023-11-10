# Generated by Django 4.2.6 on 2023-11-08 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ojotas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_calzados', models.CharField(default='', max_length=45)),
                ('descripcion', models.TextField()),
                ('año', models.IntegerField()),
                ('marca', models.CharField(max_length=30)),
                ('talla', models.CharField(default='16', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Zapatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_calzados', models.CharField(default='', max_length=45)),
                ('descripcion', models.TextField()),
                ('año', models.IntegerField()),
                ('marca', models.CharField(max_length=30)),
                ('talla', models.CharField(default='16', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='zapatillas',
            name='talla',
            field=models.CharField(default='16', max_length=10),
        ),
        migrations.AddField(
            model_name='zapatillas',
            name='tipo_de_calzados',
            field=models.CharField(default='', max_length=45),
        ),
    ]
