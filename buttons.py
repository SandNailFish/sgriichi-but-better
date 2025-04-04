from telegram import *
from telegram.ext import *


round_start = [
    [
        InlineKeyboardButton('Riichi', callback_data = 'Riichi'),
        InlineKeyboardButton('End Round', callback_data = 'End Round')
    ],
    [
        InlineKeyboardButton('End Game', callback_data = 'End Game'),
        InlineKeyboardButton('Back', callback_data = 'Back 1')
    ]
]

riichi = [
    [
        InlineKeyboardButton('[Player 1]', callback_data = 'East Riichi'),
        InlineKeyboardButton('[Player 2]', callback_data = 'South Riichi')
    ],
    [
        InlineKeyboardButton('[Player 3]', callback_data = 'West Riichi'),
        InlineKeyboardButton('[Player 4]', callback_data = 'North Riichi')
    ],
    [
        InlineKeyboardButton('Back', callback_data = 'Back 2')
    ]
]

round_end = [
    [
        InlineKeyboardButton('Ron', callback_data = 'Ron'),
        InlineKeyboardButton('Tsumo', callback_data = 'Tsumo'),
        InlineKeyboardButton('Draw', callback_data = 'Draw')
    ],
    [
        InlineKeyboardButton('Random Draw', callback_data = 'Random Draw'),
        InlineKeyboardButton('Nagashi', callback_data = 'Nagashi'),
        InlineKeyboardButton('Chombo', callback_data = 'Chombo')
    ],
    [
        InlineKeyboardButton('Back', callback_data = 'Back 2')
    ]
]

game_end = [
    [
        InlineKeyboardButton('Confirm', callback_data = '1')
    ],
    [
        InlineKeyboardButton('Back', callback_data = 'Back 2')
    ]
]

development = [
    [
        InlineKeyboardButton('Back', callback_data = 'Back 2'),
    ]
]

####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################

ron = [
    [
        InlineKeyboardButton('Winning Player', callback_data = 'Winning Player'),
        InlineKeyboardButton('Losing Player', callback_data = 'Losing Player')
    ],
    [
        InlineKeyboardButton('Han', callback_data = 'Han'),
        InlineKeyboardButton('Fu', callback_data = 'Fu')
    ],
    [
        InlineKeyboardButton('Back', callback_data = 'Back 2'),
        InlineKeyboardButton('Continue', callback_data = 'Continue')
    ]
]

tsumo = [
    [
        InlineKeyboardButton('Winning Players', callback_data = 'Winning Player')
    ],
    [
        InlineKeyboardButton('Han', callback_data = 'Han'),
        InlineKeyboardButton('Fu', callback_data = 'Fu')
    ],
    [
        InlineKeyboardButton('Back', callback_data = 'Back 2'),
        InlineKeyboardButton('Continue', callback_data = 'Continue')
    ]
]

draw = [
    [
        InlineKeyboardButton('Tenpai Player', callback_data = 'Winning Player'),
    ],
    [
        InlineKeyboardButton('Back', callback_data = 'Back 2'),
        InlineKeyboardButton('Continue', callback_data = 'Continue')
    ]
]

random_draw = [
    [
        InlineKeyboardButton('Back', callback_data = 'Back 2'),
        InlineKeyboardButton('Continue', callback_data = 'Continue')
    ]
]

nagashi_mangan = [
    [
        InlineKeyboardButton('Nagashi Player', callback_data = 'Nagashi Player')
    ],
    [
        InlineKeyboardButton('Back', callback_data = 'Back 2'),
        InlineKeyboardButton('Continue', callback_data = 'Continue')
    ]
]

chombo = [
    [
        InlineKeyboardButton('Chombo Player', callback_data = 'Chombo Player')
    ],
    [
        InlineKeyboardButton('Back', callback_data = 'Back 2'),
        InlineKeyboardButton('Continue', callback_data = 'Continue')
    ]
]

####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################

# these backs send you too far back

winning_player = [
    [
        InlineKeyboardButton('Player 1', callback_data = 'East Won'),
        InlineKeyboardButton('Player 2', callback_data = 'South Won')
    ],
    [
        InlineKeyboardButton('Player 3', callback_data = 'West Won'),
        InlineKeyboardButton('Player 4', callback_data = 'North Won')
    ],
    [
        InlineKeyboardButton('Back', callback_data = 'Back 2')
    ]
]

losing_player = [
    [
        InlineKeyboardButton('Player 1', callback_data = 'East Lost'),
        InlineKeyboardButton('Player 2', callback_data = 'South Lost')
    ],
    [
        InlineKeyboardButton('Player 3', callback_data = 'West Lost'),
        InlineKeyboardButton('Player 4', callback_data = 'North Lost')
    ],
    [
        InlineKeyboardButton('Back', callback_data = 'Back 2')
    ]
]

tenpai_player = [
    [
        InlineKeyboardButton('Player 1', callback_data = 'East Tenpai'),
        InlineKeyboardButton('Player 2', callback_data = 'South Tenpai')
    ],
    [
        InlineKeyboardButton('Player 3', callback_data = 'West Tenpai'),
        InlineKeyboardButton('Player 4', callback_data = 'North Tenpai')
    ],
    [
        InlineKeyboardButton('Back', callback_data = 'Back 2')
    ]
]

nagashi_mangan_player = [
    [
        InlineKeyboardButton('Player 1', callback_data = 'East Nagashi'),
        InlineKeyboardButton('Player 2', callback_data = 'South Nagashi')
    ],
    [
        InlineKeyboardButton('Player 3', callback_data = 'West Nagashi'),
        InlineKeyboardButton('Player 4', callback_data = 'North Nagashi')
    ],
    [
        InlineKeyboardButton('Back', callback_data = 'Back 2')
    ]
]

chombo_player = [
    [
        InlineKeyboardButton('Player 1', callback_data = 'East Chombo'),
        InlineKeyboardButton('Player 2', callback_data = 'South Chombo')
    ],
    [
        InlineKeyboardButton('Player 3', callback_data = 'West Chombo'),
        InlineKeyboardButton('Player 4', callback_data = 'North Chombo')
    ],
    [
        InlineKeyboardButton('Back', callback_data = 'Back 2')
    ]
]

####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################

han = [
    [
        InlineKeyboardButton('1', callback_data = '1 Han'),
        InlineKeyboardButton('2', callback_data = '2 Han'),
        InlineKeyboardButton('3', callback_data = '3 Han'),
        InlineKeyboardButton('4', callback_data = '4 Han'),
        InlineKeyboardButton('5', callback_data = '5 Han')
    ],
    [
        InlineKeyboardButton('6/7', callback_data = 'Haneman'),
        InlineKeyboardButton('8/9/10', callback_data = 'Baiman'),
        InlineKeyboardButton('11/≥12*', callback_data = 'Sanbaiman')
    ],
    [
        InlineKeyboardButton('≥13*/Yakuman', callback_data = 'Yakuman'),
        InlineKeyboardButton('2 × Yakuman', callback_data = '2 Yakuman'),
        InlineKeyboardButton('3 × Yakuman', callback_data = '3 Yakuman')
    ],
    [
        InlineKeyboardButton('4 × Yakuman', callback_data = '4 Yakuman'),
        InlineKeyboardButton('5 × Yakuman', callback_data = '5 Yakuman'),
        InlineKeyboardButton('6 × Yakuman', callback_data = '6 Yakuman')
    ],
]

# theres no back button

fu = [
    [
        InlineKeyboardButton('20', callback_data = '20 Fu'),
        InlineKeyboardButton('25', callback_data = '25 Fu'),
        InlineKeyboardButton('30', callback_data = '30 Fu')
    ],
    [
        InlineKeyboardButton('40', callback_data = '40 Fu'),
        InlineKeyboardButton('50', callback_data = '50 Fu'),
        InlineKeyboardButton('60', callback_data = '60 Fu'),
        InlineKeyboardButton('70', callback_data = '70 Fu')
    ],
    [
        InlineKeyboardButton('80', callback_data = '80 Fu'),
        InlineKeyboardButton('90', callback_data = '90 Fu'),
        InlineKeyboardButton('100', callback_data = '100 Fu'),
        InlineKeyboardButton('110', callback_data = '110 Fu')
    ],
    [
        InlineKeyboardButton('Back', callback_data = 'Back 2')
    ]
]

# im leaving dealing with plurality later 