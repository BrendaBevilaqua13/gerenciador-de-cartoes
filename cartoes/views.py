from django.shortcuts import render
from .models import Cartao
from pessoas.models import Pessoa


def home(request):

    return render(request, 'cartoes/pages/home.html')


def cartoes(request):
    pass
