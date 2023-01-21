from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, 'cartoes/pages/home.html', {'cartao': 'nubank'} )



