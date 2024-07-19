from django.db import models

# Definindo o modelo Arma
class Arma(models.Model):
    # Campo de nome da arma
    nome = models.CharField(max_length=100)
    # Campo de poder da arma (um inteiro representando a força da arma)
    nivel = models.IntegerField()

    # Método que retorna uma string representando o objeto
    def __str__(self):
        return f'{self.nome}, Nível: {self.nivel}'
