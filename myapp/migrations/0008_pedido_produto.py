# Generated by Django 3.0.1 on 2020-01-06 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_produto_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='produto',
            field=models.ManyToManyField(to='myapp.Produto'),
        ),
    ]
