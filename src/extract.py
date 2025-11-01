# Extrair dados da PokeAPI --> https://pokeapi.co

import requests
from time import sleep

def colect_pokemon_data(numberOfPokemons):
    ''' Coleta dados da API dos pokemons no range especificado pelo usuario
        adiciona em uma lista, e retorna essa lista para ser processada.
    '''
    if not isinstance(numberOfPokemons, int):
        raise ValueError("Erro. Passe um número valido!")
    
    counter = 1
    pokemonsList = []
    for i in range(numberOfPokemons):
        requestAPI = requests.get(f'https://pokeapi.co/api/v2/pokemon/{counter}')
        if requestAPI.status_code == 200:
            print(f"Extraindo Pokémon {counter}/{numberOfPokemons}")
            pokemonsList.append(requestAPI.json())
            counter += 1
            sleep(0.3)
        else:
            raise requests.exceptions.ConnectionError("Erro de conexão com o Servidor")
    return pokemonsList

