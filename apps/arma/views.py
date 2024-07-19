from rest_framework import viewsets
from .models import Arma
from .serializers import ArmaSerializer

# Definindo o ViewSet para o modelo Arma
class ArmaViewSet(viewsets.ModelViewSet):
    # Define o conjunto de dados (queryset) a ser usado nesta view
    queryset = Arma.objects.all()
    # Especifica o serializer a ser usado nesta view
    serializer_class = ArmaSerializer
