import requests
from django.http import HttpResponse
from django.shortcuts import render

from .forms import PokeForm


# Create your views here.
def index(request):
    nome = None
    tipo = None
    foto = None
    form = PokeForm(request.GET)
    
    if form.is_valid():
        poke = form.cleaned_data['pokemon']
        r = requests.get('https://pokeapi.co/api/v2/pokemon/' + poke.lower())
        resposta = r.json()
        nome = resposta['name'].capitalize()
        tipo = resposta['types'][0]['type']['name'].capitalize()
        foto = resposta['sprites']['front_default']



    
    return render(request, 'pokedex_django/index.html', {'form': form,
                                                         'nome': nome,
                                                         'tipo': tipo,
                                                         'foto': foto})


