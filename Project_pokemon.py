import random
import requests
from pprint import pprint

number_of_rounds = 4

# Required: Using the Pokemon API get a Pokemon based on its ID number
# Required: Create a dictionary that contains the returned Pokemon's name, id, height and weight (★ https://pokeapi.co/)


def get_card(id_card):
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(id_card)
    response = requests.get(url)
    pokemon = response.json()
    # Extension: Use different stats for the Pokemon from the API
    return {'name': pokemon['name'],
            'id': pokemon['id'],
            'height': pokemon['height'],
            'weight': pokemon['weight'],
            'moves': len(pokemon['moves']),
            'abilities': len(pokemon['abilities'])}

# Required: Compare the player's and opponent's Pokemon on the chosen stat to decide who wins


def compare_cards(stat):
    if players_pokemon[stat] > computers_pokemon[stat]:
        print('You won!')
        return 'players_pokemon'
    elif players_pokemon[stat] < computers_pokemon[stat]:
        print('Computer won!')
        return 'computers_pokemon'
    else:
        print("It's a draw!")

# Extension: Play multiple rounds and record the outcome of each round. The player with most number
# of rounds won, wins the game - part2


def set_winner(winner):
    if winner.count('players_pokemon') > winners.count('computers_pokemon'):
        print('You won the game by winning {} battles. '.format(winner.count('players_pokemon')))
    elif winner.count('computers_pokemon') > winners.count('players_pokemon'):
        print('Computer won the game by winning {} battles. '.format(winner.count('computers_pokemon')))
    else:
        print('It is a draw! ')


winners = []

allowed = ['height', 'weight', 'moves', 'abilities']

# Extension: Play multiple rounds and record the outcome of each round. The player with most number
# of rounds won, wins the game - by using for loop

stats_to_use = 1    # variable defined to hold chosen stat
for game in range(number_of_rounds):
    # Required: Generate a random number between 1 and 151 to use as the Pokemon ID number
    # Required: Get a random Pokemon for the player and another for their opponent
    players_pokemon = get_card(random.randint(1, 151))
    print('You have {}. '.format(players_pokemon['name']))
    computers_pokemon = get_card(random.randint(1, 151))

    # Required: Ask the user which stat they want to use (id, height or weight)
    # Extension: Allow the opponent (computer) to choose a stat that they would like to compare
    x = 1
    while x == 1:
        if game % 2 == 0:
            stats_to_use = input("Which stat would you like to use? {}? ".format(allowed))
            if stats_to_use in allowed:
                x = 0
            else:
                print('Please review your answer. Put {} only.'.format(allowed))
                x = 1
        else:
            stats_to_use = allowed[random.randint(0, len(allowed) - 1)]
            x = 0
    print('You have {} with {} of {}'.format(players_pokemon['name'], stats_to_use, players_pokemon[stats_to_use]))
    print('Computer has {} with {} of {}'.format(computers_pokemon['name'], stats_to_use,
                                                 computers_pokemon[stats_to_use]))

    winners.append(compare_cards(stats_to_use))

set_winner(winners)
