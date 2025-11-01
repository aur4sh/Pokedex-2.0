import json

# Transformar dados coletados em um dicionario estruturado e limpo
# Informando os dados relevantes do pokémon

def processedPokemonData(pokemonList):
    pokemonsDict = {}
    for rawData in pokemonList:
        pokemonsDict[f"{rawData['id']}"] = {
            'Nome': f"{rawData['name']}",
            'Peso': f"{rawData['weight']}",
            'Altura': f"{rawData['height']}",
            'Tipos': f"{rawData['name']}",
            'Stats': {

            }
        }
        for stat in rawData['stat']:
            newStatKey = stat['stat']['name']
            pokemonsDict[rawData['id']]['Stats'][newStatKey] = stat['base_stat']