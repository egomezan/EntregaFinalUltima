# Generated by Django 4.2.9 on 2024-04-15 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autorental', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carro',
            name='descripcion',
        ),
        migrations.AlterField(
            model_name='carro',
            name='transmision',
            field=models.CharField(choices=[('manual', 'Manual'), ('automatic', 'Automatic')], max_length=100),
        ),
    ]
