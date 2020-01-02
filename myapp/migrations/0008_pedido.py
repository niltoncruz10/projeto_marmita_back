# Generated by Django 3.0.1 on 2020-01-02 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_telefone_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
