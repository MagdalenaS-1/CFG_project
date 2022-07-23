import random
import requests
from pprint import pprint

number_of_rounds = 2

def get_card(id_card):
    url = 'http://hp-api.herokuapp.com/api/characters/'
    response = requests.get(url)
    character = response.json()
    return {'name': [character[id_card]['name'], len(character[id_card]['name'])],
            'house': [character[id_card]['house'], len(character[id_card]['house'])],
            'species': [character[id_card]['species'], len(character[id_card]['species'])],
            'wand': [character[id_card]['wand']['wood'], len(character[id_card]['wand']['wood'])]}


def compare_cards(stat):
    if player_1[stat][1] > player_2[stat][1]:
        print('Player 1 won!')
        return 'Player1'
    elif player_1[stat][1] < player_2[stat][1]:
        print('Player 2 won!')
        return 'Player2'
    else:
        print("It's a draw!")


winners = []
allowed = ['name', 'wand', 'species', 'house']
for game in range(number_of_rounds):

    player_1 = get_card(random.randint(0, 100))
    player_2 = get_card(random.randint(0, 100))

    print('Player 1 has {} . '.format(player_1['name'][0]))
    stats_to_use = 1
    x = 1

    while x == 1:
        if game%2==0:
            stats_to_use = input("Which stat would you like to use? {}? ".format(allowed))
            if stats_to_use in allowed:
                x = 0
            else:
                print('Please review your answer. Put {} only.'.format(allowed))
                x = 1
        else:
            stats_to_use=allowed[random.randint(0,len(allowed)-1)]
            x = 0

    print('Player 1 has {} with {} of {}'.format(player_1['name'][0], stats_to_use, player_1[stats_to_use][1]))
    print('Player 2 has {} with {} of {}'.format(player_2['name'][0], stats_to_use, player_2[stats_to_use][1]))

    winners.append(compare_cards(stats_to_use))
print(winners)


def set_winner(winners):
    if winners.count('Player1') > winners.count('Player2'):
        print('Player 1 won the game by winning {} battles. '.format(winners.count('Player1')))
    elif winners.count('Player2') > winners.count('Player1'):
        print('Player 2 won the game by winning {} battles. '.format(winners.count('Player2')))
    else:
        print('It is a draw! ')

set_winner(winners)

#comment