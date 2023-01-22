from django.shortcuts import render
from .models import Cartao
from pessoas.models import Pessoa


def home(request):
    pessoa = Pessoa.objects.get(nome='João')
    cartoes = Cartao.objects.filter(titular=pessoa)
    cartoes_buscados = {
        'cartoes': cartoes,
        'pessoa': pessoa
    }
    return render(request, 'cartoes/pages/home.html', cartoes_buscados)
