import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    # Loop through the json_data
    for game in json_data["games"] :
        print(game)
        # Create a new Game object from the json_data by reading
        new_game = test_data.Game

        # load JSONgame data into object
        new_game.title = game["title"]
        new_game.year = game["year"]
        new_game.platform = test_data.Platform
        platform = game["platform"]
        new_game.platform.name = platform["name"]
        new_game.platform.launch_year = platform["launch year"]

        print(new_game)

        game_library.add_game(new_game) # Add that Game object to the game_library
    
    return game_library # Return the completed game_library
