# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Carro

# Create your views here.

def index(request):

    #Pega todos os registros.
    todos_carros = Carro.objects.all()

    #Jogamos a informação aqui
    template = loader.get_template('carros/index.html')

    return HttpResponse(
        template.render({'carros':todos_carros}, request))

# Busca no banco o id
'''
    def detail(request, carro_id):
    carro = Carro.objects.get(id=carro_id)
    return HttpResponse(carro)
'''

def detail(request, carro_id):

    carro = get_object_or_404(Carro, pk=carro_id)
    return render(request, 'carros/details.html', {'item':carro})
