from utils.Translations import PTBR_STATS_LIST
from utils.Translations import PTBR_TYPES

# Transformar dados coletados em um dicionario estruturado e limpo
# Informando os dados relevantes do pokémon

def processedPokemonData(pokemonList):
    pokemonsDict = {}
    typesCounter = 0
    for rawData in pokemonList:
        pokemonsDict[f"{rawData['id']}"] = {
            'Nome': f"{rawData['name']}",
            'Peso': f"{rawData['weight']}",
            'Altura': f"{rawData['height']}",
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