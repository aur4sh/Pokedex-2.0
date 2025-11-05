# Extrair dados da PokeAPI --> https://pokeapi.co
# Função de extração de pokemons baseado em intervalo, evitando requisições em dados
# Já existentes

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

def colect_pokemon_in_interval(numberOfPokemons, minimalPokemons):
    '''Função usada para evitar desperdicio de processamento e tempo,
        efetuando somente as requisições de pokemons que não existam no cache'''
    
    if not isinstance(numberOfPokemons, int) and not isinstance(minimalPokemons, int):
        raise ValueError("Erro. Passe um número valido!")

    pokemonsList = []
    for i in range(minimalPokemons + 1, numberOfPokemons + 1):
        requestAPI = requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}')
        if requestAPI.status_code == 200:
            print(f"Extraindo Pokémon {i}/{numberOfPokemons}")
            pokemonsList.append(requestAPI.json())
            sleep(0.3)
    
        else:
            raise requests.exceptions.ConnectionError("Erro de conexão com o Servidor")
    return pokemonsList
