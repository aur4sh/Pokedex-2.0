from src.extract import *
from src.transform import *
from src.load import *
from time import sleep

try:
    if processedPokemonFolder.exists():
        loadSaveData = loadPokemonData()
        for pokemonId, info in loadSaveData.items():
            print(f"Pokédex ID: {pokemonId}, Info: {info}")
            print()
            sleep(1)
    else:
        pokemonRawData = colect_pokemon_data(152)
        saveRawPokemonData(pokemonRawData)

        pokemonProcessedData = processedPokemonData(pokemonRawData)

        saveProcessedPokemonData(pokemonProcessedData)

except ValueError as e:
    print(e)
except ConnectionError as e:
    print(e)