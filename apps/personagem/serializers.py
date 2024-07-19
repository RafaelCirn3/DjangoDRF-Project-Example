from rest_framework import serializers
from .models import Personagem

# Definindo o serializer para o modelo Personagem
class PersonagemSerializer(serializers.ModelSerializer):
    class Meta:
        # Especifica o modelo a ser serializado
        model = Personagem
        # Especifica os campos a serem incluídos na serialização
        fields = '__all__'
