from telegram import *
from telegram.ext import *

import template
import buttons
import data

async def query_reader(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    query = update.callback_query
    
    await query.answer()

    round_menu = {
    'Back 2': InlineKeyboardMarkup(buttons.round_start),
    'Riichi': InlineKeyboardMarkup(buttons.riichi),
    'End Round': InlineKeyboardMarkup(buttons.round_end),
    'End Game': InlineKeyboardMarkup(buttons.game_end),
    'Back 1': InlineKeyboardMarkup(buttons.development)
    }

    if query.data in round_menu:

        await query.edit_message_reply_markup(reply_markup = round_menu[query.data]) #edits the markup only

    ####################################################################################################
    ####################################################################################################
    ####################################################################################################
    ####################################################################################################
    ####################################################################################################

    if query.data == 'East Riichi':

        data.east.riichi_state = not data.east.riichi_state

        if data.east.riichi_state == True:

            data.riichi_player.append('Player 1')

            data.east.score -= 1000

            data.riichi_deposit += 1

            await query.edit_message_text(template.message(), parse_mode = 'Markdown', reply_markup = InlineKeyboardMarkup(buttons.round_start)) #edits text and markup

        elif data.east.riichi_state == False:

            data.riichi_player.remove('Player 1')

            data.east.score += 1000

            data.riichi_deposit -= 1

            await query.edit_message_text(template.message(), parse_mode = 'Markdown', reply_markup = InlineKeyboardMarkup(buttons.riichi))

    elif query.data == 'South Riichi':

        data.south.riichi_state = not data.south.riichi_state

        if data.south.riichi_state == True:

            data.riichi_player.append('Player 2')

            data.south.score -= 1000

            data.riichi_deposit += 1

            await query.edit_message_text(template.message(), parse_mode = 'Markdown', reply_markup = InlineKeyboardMarkup(buttons.round_start)) #edits text and markup

        elif data.south.riichi_state == False:

            data.riichi_player.remove('Player 2')

            data.south.score += 1000

            data.riichi_deposit -= 1

            await query.edit_message_text(template.message(), parse_mode = 'Markdown', reply_markup = InlineKeyboardMarkup(buttons.riichi))

    elif query.data == 'West Riichi':

        data.west.riichi_state = not data.west.riichi_state

        if data.west.riichi_state == True:

            data.riichi_player.append('Player 3')

            data.west.score -= 1000

            data.riichi_deposit += 1

            await query.edit_message_text(template.message(), parse_mode = 'Markdown', reply_markup = InlineKeyboardMarkup(buttons.round_start)) #edits text and markup

        elif data.west.riichi_state == False:

            data.riichi_player.remove('Player 3')

            data.west.score += 1000

            data.riichi_deposit -= 1

            await query.edit_message_text(template.message(), parse_mode = 'Markdown', reply_markup = InlineKeyboardMarkup(buttons.riichi))

    elif query.data == 'North Riichi':

        data.north.riichi_state = not data.north.riichi_state

        if data.north.riichi_state == True:

            data.riichi_player.append('Player 4')

            data.north.score -= 1000

            data.riichi_deposit += 1

            await query.edit_message_text(template.message(), parse_mode = 'Markdown', reply_markup = InlineKeyboardMarkup(buttons.round_start)) #edits text and markup

        elif data.north.riichi_state == False:

            data.riichi_player.remove('Player 4')

            data.north.score += 1000

            data.riichi_deposit -= 1

            await query.edit_message_text(template.message(), parse_mode = 'Markdown', reply_markup = InlineKeyboardMarkup(buttons.riichi))

# mapping this is more difficult than expected because you need to setattr() because dictionaries but cannot directly access the variable name

    ####################################################################################################
    ####################################################################################################
    ####################################################################################################
    ####################################################################################################
    ####################################################################################################

    outcome_menu = {
    'Ron': ('Ron', InlineKeyboardMarkup(buttons.ron)),
    'Tsumo': ('Tsumo', InlineKeyboardMarkup(buttons.tsumo)),
    'Draw': ('Draw', InlineKeyboardMarkup(buttons.draw)),
    'Random Draw': ('Random Draw', InlineKeyboardMarkup(buttons.random_draw)),
    'Nagashi': ('Nagashi', InlineKeyboardMarkup(buttons.nagashi_mangan)),
    'Chombo': ('Chombo', InlineKeyboardMarkup(buttons.chombo))
}

    if query.data in outcome_menu:

        data.round_outcome = outcome_menu[query.data][0]

        await query.edit_message_text(template.message(), parse_mode = 'Markdown', reply_markup = outcome_menu[query.data][1]) #edits text and markup

    ####################################################################################################
    ####################################################################################################
    ####################################################################################################
    ####################################################################################################
    ####################################################################################################

    round_end_menu = {
    'Winning Player': InlineKeyboardMarkup(buttons.winning_player),
    'Losing Player': InlineKeyboardMarkup(buttons.losing_player),
    'Tenpai Player': InlineKeyboardMarkup(buttons.tenpai_player),
    'Nagashi Player': InlineKeyboardMarkup(buttons.nagashi_mangan_player),
    'Chombo Player': InlineKeyboardMarkup(buttons.chombo_player),
    'Han': InlineKeyboardMarkup(buttons.han),
    'Fu': InlineKeyboardMarkup(buttons.fu)
    }

    if query.data in round_end_menu:

        await query.edit_message_text(template.message(), parse_mode = 'Markdown', reply_markup = round_end_menu[query.data]) #edits text and markup

    ####################################################################################################
    ####################################################################################################
    ####################################################################################################
    ####################################################################################################
    ####################################################################################################

# the buttons must return to their original ones (ron/tsumo) cannot just be ron

    elif query.data == 'East Won':

        data.winning_player = 'Player 1'

        await query.edit_message_text(template.message(), parse_mode = 'Markdown', reply_markup = InlineKeyboardMarkup(buttons.ron)) #edits text and markup

    elif query.data == 'South Won':

        data.winning_player = 'Player 2'
 
        await query.edit_message_text(template.message(), parse_mode = 'Markdown', reply_markup = InlineKeyboardMarkup(buttons.ron)) #edits text and markup

    elif query.data == 'West Won':

        data.winning_player = 'Player 3'

        await query.edit_message_text(template.message(), parse_mode = 'Markdown', reply_markup = InlineKeyboardMarkup(buttons.ron)) #edits text and markup

    elif query.data == 'North Won':

        data.winning_player = 'Player 4'

        await query.edit_message_text(template.message(), parse_mode = 'Markdown', reply_markup = InlineKeyboardMarkup(buttons.ron)) #edits text and markup

    ####################################################################################################
    ####################################################################################################
    ####################################################################################################
    ####################################################################################################
    ####################################################################################################

    losing_menu = {
    'East Lost': 'Player 1',
    'South Lost': 'Player 2',
    'West Lost': 'Player 3',
    'North Lost': 'Player 4'
    }

    if query.data in losing_menu:

        data.losing_player = losing_menu[query.data]

        await query.edit_message_text(template.message(), parse_mode = 'Markdown', reply_markup = InlineKeyboardMarkup(buttons.ron)) #edits text and markup
    
# this one is fine because only ron has a losing player

    ####################################################################################################
    ####################################################################################################
    ####################################################################################################
    ####################################################################################################
    ####################################################################################################

    han = {
        '1 Han': 1,
        '2 Han': 2,
        '3 Han': 3,
        '4 Han': 4,
        '5 Han': 5,
        'Haneman': 6,
        'Baiman': 8,
        'Sanbaiman': 11,
        'Yakuman': 13,
        '2 Yakuman': 26,
        '3 Yakuman': 39,
        '4 Yakuman': 52,
        '5 Yakuman': 65,
        '6 Yakuman': 78
    }

    if query.data in han:
        data.han = han[query.data]

        await query.edit_message_text(template.message(), parse_mode = 'Markdown', reply_markup = InlineKeyboardMarkup(buttons.ron))  # Edits text and markup

    ####################################################################################################
    ####################################################################################################
    ####################################################################################################
    ####################################################################################################
    ####################################################################################################

    fu = {
        '20 Fu': 20,
        '25 Fu': 25,
        '30 Fu': 30,
        '40 Fu': 40,
        '50 Fu': 50,
        '60 Fu': 60,
        '70 Fu': 70,
        '80 Fu': 80,
        '90 Fu': 90,
        '100 Fu': 100,
        '110 Fu': 110
    }

    if query.data in fu:
        data.fu = fu[query.data]

        await query.edit_message_text(template.message(), parse_mode = 'Markdown', reply_markup = InlineKeyboardMarkup(buttons.ron))  # Edits text and markup

    ####################################################################################################
    ####################################################################################################
    ####################################################################################################
    ####################################################################################################
    ####################################################################################################

    if query.data == 'Continue':

        data.cont_inue = 'Continue'

        await query.edit_message_text(template.message(), parse_mode = 'Markdown', reply_markup = InlineKeyboardMarkup(buttons.development))  # Edits text and markup

        data.east.score = data.east.score + template.score_change(data.east.name, data.east.oya_state)
        data.south.score = data.south.score + template.score_change(data.south.name, data.south.oya_state)
        data.west.score = data.west.score + template.score_change(data.west.name, data.west.oya_state)
        data.north.score = data.north.score + template.score_change(data.north.name, data.north.oya_state)

        template.reset()

        await context.bot.send_message(chat_id = update.effective_chat.id, text = template.message(), parse_mode = 'Markdown', reply_markup = InlineKeyboardMarkup(buttons.round_start))
