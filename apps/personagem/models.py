from django.db import models

# Definindo o modelo Personagem
class Personagem(models.Model):
    # Campo de nome do personagem
    nome = models.CharField(max_length=100)
    # Campo de descrição do personagem
    descricao = models.TextField()

    # Método que retorna uma string representando o objeto
    def __str__(self):
        return self.nome
