import math

import data

####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################

def formatted_riichi_player():

    return '\n'.join(data.riichi_player)

####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################

def formatted_score():

    player_data = [data.east,
                   data.south,
                   data.west,
                   data.north]

    player_sorted = sorted(player_data, key = lambda Player: Player.score, reverse = True)

    ScoreText = f'''{player_sorted[0].char} | {player_sorted[0].name} | {player_sorted[0].score} | {player_sorted[0].difference}
{player_sorted[1].char} | {player_sorted[1].name} | {player_sorted[1].score} | {player_sorted[1].difference}
{player_sorted[2].char} | {player_sorted[2].name} | {player_sorted[2].score} | {player_sorted[2].difference}
{player_sorted[3].char} | {player_sorted[3].name} | {player_sorted[3].score} | {player_sorted[3].difference}'''

    return ScoreText

####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################

def formatted_new_score():

    if data.cont_inue == '':

        return ''

    elif data.cont_inue == 'Continue':

        new_score_text = f'''{data.east.char} | {data.east.name} | {score_change(data.east.name, data.east.oya_state)}
{data.south.char} | {data.south.name} | {score_change(data.south.name, data.south.oya_state)}
{data.west.char} | {data.west.name} | {score_change(data.west.name, data.west.oya_state)}
{data.north.char} | {data.north.name} | {score_change(data.north.name, data.north.oya_state)}'''

        return new_score_text

####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################

def round_outcome_text():

    if data.round_outcome == '':

        return ''

    elif data.round_outcome == 'Ron':

        return rf'''Winning Player: {data.winning_player}
Losing Player: {data.losing_player}
Hand Value: {data.han} Han {data.fu} Fu'''

    elif data.round_outcome == 'Tsumo':

        return rf'''Winning Player: {data.winning_player}
Hand Value: {data.han} Han {data.fu} Fu'''
    
    elif data.round_outcome == 'Draw':

        return rf'''Tenpai Player: {data.tenpai_player}'''

    # elif data.round_outcome == 'Random Draw':

    #     return ''

    elif data.round_outcome == 'Nagashi':

        return rf'''Nagashi Mangan Player: {data.nagashi_mangan_player}'''

    elif data.round_outcome == 'Chombo':

        return rf'''Chombo Player: {data.chombo_player}'''

####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################

def message():

    return rf'''`Game ID: {data.game_id}
Hand Number: {data.hand_number}
Round: {data.round}
Honba: {data.honba}
Riichi Deposit: {data.riichi_deposit}
-----------------------------
{formatted_score()}
-----------------------------
Riichi Player:
{formatted_riichi_player()}
-----------------------------
Round Outcome: {data.round_outcome}
{round_outcome_text()}
-----------------------------
{formatted_new_score()}`'''

# you can add ` ` to every line to make it funky

####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################

def basic_score(han, fu):

    if (han == 1) or (han == 2) or (han == 3 and fu in (20, 25, 30, 40, 50, 60)) or (han == 4 and fu in (20, 25, 30)):

        return (fu * (2 ** (2 + han))) # cannot put the math.ceil here because sometimes you multiply 6 first then ceil

    elif han in (3, 4, 5):

        return 2000

    elif han == 6:

        return 3000

    elif han == 8:

        return 4000

    elif han == 11:

        return 6000

    elif han == 13:

        return 8000

    elif han == 26:

        return 16000

    elif han == 39:

        return 24000

    elif han == 52:

        return 32000

    elif han == 65:

        return 40000

    elif han == 78:

        return 48000

####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################

def score_change(name, oya_state):

    if data.winning_player == name:

        if data.round_outcome == 'Ron':

            if oya_state == True:

                return math.ceil(6 * basic_score(data.han, data.fu) / 100) * 100 + data.riichi_deposit * 1000

            elif oya_state == False:

                return math.ceil(4 * basic_score(data.han, data.fu) / 100) * 100 + data.riichi_deposit * 1000

        elif data.round_outcome == 'Tsumo':

            if oya_state == True:

                return 3 * math.ceil(2 * basic_score(data.han, data.fu) / 100) * 100 + data.riichi_deposit * 1000

            elif oya_state == False:

                return math.ceil(2 * basic_score(data.han, data.fu) / 100) * 100 + 2 * (math.ceil(basic_score(data.han, data.fu) / 100) * 100) + data.riichi_deposit * 1000

    elif data.losing_player == name: # its always ron if theres a losing player

        if data.winning_player == data.oya:

            return 0 - math.ceil(6 * basic_score(data.han, data.fu) / 100) * 100

        else:

            return 0 - math.ceil(4 * basic_score(data.han, data.fu) / 100) * 100 

    else:

        if data.round_outcome == 'Ron':

            return 0

        elif data.round_outcome == 'Tsumo':

            if oya_state == True:

                return 0 - math.ceil(2 * basic_score(data.han, data.fu) / 100) * 100

            elif oya_state == False:
 
                return 0 - math.ceil(basic_score(data.han, data.fu) / 100) * 100

def reset():
    data.east.riichi_state = False
    data.south.riichi_state = False
    data.west.riichi_state = False
    data.north.riichi_state = False

    data.hand_number += 1
    data.round = 'dong 2'
    data.honba = 0
    data.riichi_deposit = 0

    data.oya = 'Player 2'
    
    data.riichi_player = []

    data.winning_player = ''
    data.losing_player  = ''
    data.tenpai_player = ''
    data.nagashi_mangan_player = ''
    data.chombo_player = ''
    data.han = ''
    data.fu = ''

    data.round_outcome = ''

    data.cont_inue = ''