from rest_framework import serializers
from .models import Arma

# Definindo o serializer para o modelo Arma
class ArmaSerializer(serializers.ModelSerializer):
    class Meta:
        # Especifica o modelo a ser serializado
        model = Arma
        # Especifica os campos a serem incluídos na serialização
        fields = '__all__'
