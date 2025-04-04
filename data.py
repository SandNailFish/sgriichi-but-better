class PlayerInformation:
    def __init__(self, char, name, oya_state, score, difference, riichi_state):
        self.char = char
        self.name = name
        self.oya_state = oya_state
        self.score = score
        self.difference = difference
        self.riichi_state = riichi_state
    
east = PlayerInformation("东", 'Player 1', True, 25000, 0, False)
south = PlayerInformation("南", 'Player 2', False, 25000, 0, False)
west = PlayerInformation("西", 'Player 3', False, 25000, 0, False)
north = PlayerInformation("北", 'Player 4', False, 25000, 0, False)

game_id = 1
hand_number = 1
round = '东-1'
honba = 0
riichi_deposit = 0

oya = 'Player 1'

riichi_player = []

winning_player = ''
losing_player  = ''
tenpai_player = ''
nagashi_mangan_player = ''
chombo_player = ''
han = ''
fu = ''

round_outcome = ''

cont_inue = ''