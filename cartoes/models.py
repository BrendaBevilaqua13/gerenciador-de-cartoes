from django.db import models
from django.contrib.auth.models import User


class Cartao(models.Model):
    titular = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=15)
    def __str__(self):
        return self.nome
