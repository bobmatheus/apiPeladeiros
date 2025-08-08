from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)  # pra armazenar senha (recomendo hash)

    def __str__(self):
        return self.email