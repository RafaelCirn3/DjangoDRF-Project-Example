from rest_framework import serializers
from .models import Avatar

# Definindo o serializer para o modelo Avatar
class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        # Especifica o modelo a ser serializado
        model = Avatar
        # Especifica os campos a serem incluídos na serialização
        fields = '__all__'
    
    def validate(self, sttrs):
    # Pega o nickname do avatar
        nickname = sttrs.get('nickname')

        # Verifica se já existe um avatar com o mesmo nickname
        if Avatar.objects.filter(nickname=nickname).exists():
            # Se existe, lança uma validação de erro
            raise serializers.ValidationError(f"Um avatar com o nome {nickname} já existe.")

        # Se o nickname for único, chama o método validate da superclasse
        return super().validate(sttrs)
