# Generated by Django 3.2.7 on 2021-09-28 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orcamentos', '0002_alter_produto_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]
