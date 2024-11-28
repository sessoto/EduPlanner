# Generated by Django 5.1.3 on 2024-11-28 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Evento',
        ),
    ]
