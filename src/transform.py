from src.utils.Translations import *

# Transformar dados coletados em um dicionario estruturado e limpo
# Informando os dados relevantes do pokémon

def processedPokemonData(pokemonList):
    ''' Recebe os dados Extraidos da pokeAPI, filtra os relevantes,
            transforma strings e converte valores, adicionando tudo
                a um dicionario com daddos transformados e filtrados
       '''
    pokemonsDict = {}
    typesCounter = 0
    for rawData in pokemonList:
        pokemonsDict[f"{rawData['id']}"] = {
            'Nome': f"{rawData['name']}",
            'Peso': float(f"{rawData['weight'] / 10:.2f}"),
            'Altura': float(f"{rawData['height'] / 10:.2f}"),
            'Tipos': [],
            'Stats': {
                
            }
        }
        for stat in rawData['stats']:
            stat['stat']['name'] = PTBR_STATS_LIST[typesCounter]
            newStatKey = stat['stat']['name']
            pokemonsDict[f'{rawData['id']}']['Stats'][newStatKey] = stat['base_stat']
            typesCounter += 1
        for tipo in rawData['types']:
            tipo['type']['name'] = PTBR_TYPES[tipo['type']['name']]
            pokemonsDict[f"{rawData['id']}"]['Tipos'].append(tipo['type']['name'])
        typesCounter = 0
    return pokemonsDict