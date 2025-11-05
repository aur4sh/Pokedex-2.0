from src.extract import *
from src.transform import *
from src.load import *
from time import sleep

try:
    pokemonRangeInput = int(input("Quantos pokemons para processar: "))
    if processedPokemonFolder.exists():
        loadSaveData = loadPokemonData()
        if pokemonRangeInput < len(loadSaveData):
            for pokemonId, info in loadSaveData.items():
                print("Todos os dados já estão processados no cache local, exibindo:")
                print(f"Pokédex ID: {pokemonId}, Info: {info}")
                print()
                sleep(1)
        elif pokemonRangeInput - len(loadSaveData) == 0:
            for pokemonId, info in loadSaveData.items():
                print("Todos os dados já estão processados no cache local, exibindo:")
                print(f"Pokédex ID: {pokemonId}, Info: {info}")
                print()
                sleep(1)
        else:
            print(f"Foram encontrados {len(loadSaveData)} pokémons salvos, pesquisando os restantes...")
            IntervalPokemonsRawData = colect_pokemon_in_interval(pokemonRangeInput, len(loadSaveData))
            IntervalPokemonsProcessedData = processedPokemonData(IntervalPokemonsRawData)
            
            updatePokemonData(IntervalPokemonsProcessedData)
    else:
        pokemonRawData = colect_pokemon_data(pokemonRangeInput)
        saveRawPokemonData(pokemonRawData)

        pokemonProcessedData = processedPokemonData(pokemonRawData)

        saveProcessedPokemonData(pokemonProcessedData)

except ValueError as e:
    print(e)
except ConnectionError as e:
    print(e)