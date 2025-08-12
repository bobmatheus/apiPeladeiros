from django.db import models
from django.contrib.auth.models import AbstractUser

# Usuário customizado
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

# Espaços para alugar
class Espaco(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    valor = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome

# Reservas
class Reserva(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    espaco = models.ForeignKey(Espaco, on_delete=models.CASCADE)
    data = models.DateField()

    class Meta:
        unique_together = ['espaco', 'data']  # impede reservas duplicadas

    def __str__(self):
        return f"{self.usuario.email} reservou {self.espaco.nome} em {self.data}"

# Carrinho (opcional)
class ItemCarrinho(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    espaco = models.ForeignKey(Espaco, on_delete=models.CASCADE)
    data = models.DateField()

    def __str__(self):
        return f"Carrinho: {self.usuario.email} - {self.espaco.nome} em {self.data}"