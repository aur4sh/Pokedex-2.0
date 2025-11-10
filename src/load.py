# Funções para carregamento dos dados processados e crús dentro de um arquivo json
# Função para cache local, carregando dados que já estão salvos
# Função para atualização do cache, usada para adicionar novos valores sem repetir requisições a API

from pathlib import Path
import json
from time import sleep


processedPokemonFolder = Path(__file__).parents[1] / "data/processed/pokedex.json"
rawPokemonFolder = Path(__file__).parents[1] / "data/raw/rawPokemonInfo.jsonl"

processedPokemonFolder.parent.mkdir(parents=True, exist_ok=True)
rawPokemonFolder.parent.mkdir(parents=True, exist_ok=True)

def saveProcessedPokemonData(pokemonsDict):
    ''' Recebe o dicionario transformado e processado 
            Armazena ele em um arquivo json '''
    print(f"Salvando dados processados para --> {processedPokemonFolder}")
    sleep(2)
    print()
    with open(processedPokemonFolder, 'w', encoding='UTF-8') as pokeArq:
        json.dump(pokemonsDict, pokeArq, indent=4, ensure_ascii=False)
    
def saveRawPokemonData(pokemonsList):
    ''' Recebe lista não processada e transformada
        E armazena em um json '''
    print(f"Salvando dados crús para --> {rawPokemonFolder}")
    sleep(2)
    with open(rawPokemonFolder, 'a', encoding='UTF-8') as rawPokeArq:
        for pokemon in pokemonsList:
            json.dump(pokemon, rawPokeArq, ensure_ascii=False)
            rawPokeArq.write("\n")

def loadPokemonData():
    '''Carrega dados já salvos previamente'''
    print("Carregando dados existentes. . .")
    print()
    with open(processedPokemonFolder, 'r', encoding='UTF-8') as pokedex:
        savedPokemonData = json.load(pokedex)
    return savedPokemonData

def updatePokemonData(newPokemonData):
    '''Recebe os novos dados a ser integrados, apenas adicionando eles
            sem repetir todos os processos de reescrita no json'''
    print("Atualizando dados do Cache. . .")
    sleep(1.5)
    with open(processedPokemonFolder, 'r', encoding='UTF-8') as pokedex:
        loadedPokemonData = json.load(pokedex)

    with open(processedPokemonFolder, 'w', encoding='UTF-8') as updatedPokedexArq:
        for chave, valor in newPokemonData.items():
            loadedPokemonData[f'{chave}'] = {
                'Nome': valor['Nome'],
                'Peso': valor['Peso'],
                'Altura': valor['Altura'],
                'Tipos': valor['Tipos'],
                'Stats': valor['Stats'],
            }
        json.dump(loadedPokemonData, updatedPokedexArq, indent=4, ensure_ascii=False)
    print("Dados salvos com sucesso :)")

def updatePokemonRawData(rawDataList):
    ''' Atualiza o arquivo dos dados não processados
     utilizando os dados dos pokemons novos adicionaddos '''
    with open(rawPokemonFolder, 'a', encoding='UTF-8') as updatedRawData:
        for newRawPokemon in rawDataList:
            json.dump(newRawPokemon, updatedRawData, ensure_ascii=False)
            updatedRawData.write("\n")