from src.extract import *
from src.transform import *
from src.load import *
from src.utils import utilities
from time import sleep

try:
    pokemonRangeInput = int(input("Quantos pokemons para processar: "))
    sleep(0.3)
    utilities.limpar()

    if processedPokemonFolder.exists():

        loadSaveData = loadPokemonData()

        if pokemonRangeInput < len(loadSaveData) or pokemonRangeInput - len(loadSaveData) == 0:
            for pokemonId, info in loadSaveData.items():
                print("Todos os dados já estão processados no cache local, exibindo:")
                print()
                print(f"Pokédex ID: {pokemonId}, Info: {info}")
                print()
                sleep(1)
       
        else:
            print(f"Foram encontrados {len(loadSaveData)} Pokémons salvos")
            sleep(1.5)
            utilities.limpar()

            print(f"Buscando Pokémons não armazenados...")
            print()
            sleep(1.5)

            IntervalPokemonsRawData = colect_pokemon_in_interval(pokemonRangeInput, len(loadSaveData))
            IntervalPokemonsProcessedData = processedPokemonData(IntervalPokemonsRawData)
            
            updatePokemonData(IntervalPokemonsProcessedData)
            updatePokemonRawData(IntervalPokemonsRawData)
            
    else:
        pokemonRawData = colect_pokemon_data(pokemonRangeInput)
        saveRawPokemonData(pokemonRawData)
        
        pokemonProcessedData = processedPokemonData(pokemonRawData)
        saveProcessedPokemonData(pokemonProcessedData)

except ValueError as e:
    print(e)
except ConnectionError as e:
    print(e)