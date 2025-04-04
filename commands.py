from telegram import *
from telegram.ext import *

import template
import buttons

####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################

async def riichi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    await update.message.reply_text(template.message(), parse_mode = 'Markdown', reply_markup = InlineKeyboardMarkup(buttons.round_start))