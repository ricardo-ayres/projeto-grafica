from rest_framework import serializers

from orcamentos.models import Produto

class ProdutoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Produto
        fields = ('id',
                  'nome',
                  'descricao',
                  'preco',
                  'tipo_unidade',
                  'valor_unidade')

