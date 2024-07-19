from rest_framework import viewsets
from .models import Avatar
from .serializers import AvatarSerializer

# Definindo o ViewSet para o modelo Avatar
class AvatarViewSet(viewsets.ModelViewSet):
    # Define o conjunto de dados (queryset) a ser usado nesta view
    queryset = Avatar.objects.all()
    # Especifica o serializer a ser usado nesta view
    serializer_class = AvatarSerializer
