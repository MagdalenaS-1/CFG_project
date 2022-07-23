import random
import requests
from pprint import pprint


def card():
    id_card = random.randint(1, 100)
    url = 'http://hp-api.herokuapp.com/api/characters/'
    response = requests.get(url)
    character = response.json()
    return {'name': [character[id_card]['name'], len(character[id_card]['name'])],
            'house': [character[id_card]['house'], len(character[id_card]['house'])],
            'species': [character[id_card]['species'], len(character[id_card]['species'])],
            'wand': [character[id_card]['wand']['wood'], len(character[id_card]['wand']['wood'])]}


def compare(stat):
    if player_1[stat][1] > player_2[stat][1]:
        print('Player 1 won!')
        return 'Player1'
    elif player_1[stat][1] < player_2[stat][1]:
        print('Player 2 won!')
        return 'Player2'
    else:
        print("It's a draw!")


winners = []

for game in range(5):

    player_1 = card()
    player_2 = card()

    print('Player 1 has {} . '.format(player_1['name'][0]))
    stats_to_use = 1
    x = 1
    while x == 1:
        stats_to_use = input("Which stat would you like to use? name, wand, house or year of species? ")
        allowed = ['name', 'wand', 'species', 'house']
        if stats_to_use in allowed:
            x = 0
        else:
            print('Please review your answer. Put name, wand, house or species only.')
            x = 1

    print('Player 1 has {} with {} of {}'.format(player_1['name'][0], stats_to_use, player_1[stats_to_use][1]))
    print('Player 2 has {} with {} of {}'.format(player_2['name'][0], stats_to_use, player_2[stats_to_use][1]))

    winners.append(compare(stats_to_use))
print(winners)


def winner(winners):
    if winners.count('Player1') > winners.count('Player2'):
        print('Player 1 won the game by winning {} battles. '.format(winners.count('Player1')))
    elif winners.count('Player2') > winners.count('Player1'):
        print('Player 2 won the game by winning {} battles. '.format(winners.count('Player2')))
    else:
        print('It is a draw! ')


print(winner(winners))

#comment