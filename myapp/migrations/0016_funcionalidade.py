# Generated by Django 3.0.1 on 2020-01-04 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionalidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
            ],
        ),
    ]
