from django.shortcuts import render, HttpResponse
from . models import Cartao


def home(request):
    return render(request, 'cartoes/pages/home.html')


def cartoes(request):
    usuario_cartoes = Cartao.objects.filter(titular=request.user.id)
    cartoes  = {
        'cartoes': usuario_cartoes,
    }
    return render(request, 'cartoes/pages/cartoes.html', cartoes)



