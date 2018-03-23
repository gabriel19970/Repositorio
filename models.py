# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Fabricante(models.Model):
    nome = models.CharField(max_length=300, null=True)
    preco = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.nome

class Carro(models.Model):
    name = models.CharField(max_length = 300, null=True)
    valor = models.CharField(max_length = 300, null=True)
    ano = models.CharField(max_length = 300, null=True)
    modelo = models.CharField(max_length = 300, null=True)

    # Para receber a chave estrangeira.
    fabricante = models.ForeignKey(Fabricante, null=True)

# É para não mostrar informação de baixo nivel
    def __str__(self):
        return self.name

