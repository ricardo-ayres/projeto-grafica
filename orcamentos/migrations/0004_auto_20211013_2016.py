# Generated by Django 3.2.7 on 2021-10-13 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orcamentos', '0003_alter_produto_preco'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='tipo_unidade',
            field=models.CharField(default='unidades', max_length=200),
        ),
        migrations.AddField(
            model_name='produto',
            name='valor_unidade',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
