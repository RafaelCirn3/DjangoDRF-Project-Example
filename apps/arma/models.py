from django.db import models

# Definindo as escolhas para o elemento da arma
TIPO_ARMA_CHOICES = [
    ('eletrico', 'Elétrico'),
    ('fogo', 'Fogo'),
    ('agua', 'Água'),
    ('sombrio', 'Sombrio'),
    ('neutro', 'Neutro'),
    ('solar', 'Solar'),
]

# Definindo as escolhas para o tipo de arma
TIPO_CHOICES = [
    ('espada', 'Espada'),
    ('machado', 'Machado'),
    ('arco', 'Arco'),
    ('foice', 'Foice'),
    ('lanca', 'Lança'),
]

# Definindo o modelo Arma
class Arma(models.Model):
    # Campo de nome da arma
    nome = models.CharField(max_length=100)
    # Campo de poder da arma (um inteiro representando a força da arma)
    nivel = models.IntegerField()
    # Campo de elemento da arma com choices
    elemento = models.CharField(max_length=10, choices=TIPO_ARMA_CHOICES, default='neutro')
    # Campo de tipo da arma com choices
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='espada')

    # Método que retorna uma string representando o objeto
    def __str__(self):
        return f'{self.nome}, Nível: {self.nivel}, Elemento: {self.elemento}, Tipo: {self.tipo}'
