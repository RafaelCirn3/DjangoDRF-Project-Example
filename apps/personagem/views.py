from rest_framework import viewsets
from .models import Personagem
from .serializers import PersonagemSerializer

# Definindo o ViewSet para o modelo Personagem
class PersonagemViewSet(viewsets.ModelViewSet):
    # Define o conjunto de dados (queryset) a ser usado nesta view
    queryset = Personagem.objects.all()
    # Especifica o serializer a ser usado nesta view
    serializer_class = PersonagemSerializer
