from rest_framework import serializers
from .models import Avatar

# Definindo o serializer para o modelo Avatar
class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        # Especifica o modelo a ser serializado
        model = Avatar
        # Especifica os campos a serem incluídos na serialização
        fields = '__all__'
