from django.db import models
from apps.personagem.models import Personagem
from apps.arma.models import Arma

# Definindo o modelo Avatar
class Avatar(models.Model):
    # Campo de nome do avatar
    nome = models.CharField(max_length=100)
    # Chave estrangeira referenciando um personagem
    personagem = models.ForeignKey(Personagem, on_delete=models.CASCADE)
    # Chave estrangeira referenciando uma arma
    arma = models.ForeignKey(Arma, on_delete=models.CASCADE)

    # Método que retorna uma string representando o objeto
    def __str__(self):
        return self.nome
