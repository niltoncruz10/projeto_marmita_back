# Generated by Django 3.0.1 on 2019-12-31 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_cardapio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(max_length=8)),
                ('descricao', models.CharField(max_length=45)),
            ],
        ),
    ]
