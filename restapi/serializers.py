from rest_framework import serializers

from orcamentos.models import Produto

class ProdutoSerializer(serializers.HyperlinkedModeSerializer):
    class Meta:
        model = Produto
        fields = ('nome',
                  'descricao',
                  'preco',
                  'tipo_unidade',
                  'valor_unidade')

