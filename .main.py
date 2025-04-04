import logging

from telegram import *
from telegram.ext import *

import commands
import query_reader

# Enable logging
logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',level = logging.INFO)

# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger('httpx').setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

####################################################################################################

def main() -> None:
    application = Application.builder().token('TOKEN').build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler('riichi', commands.riichi))

    # on non command i.e message - echo the message on Telegram
    # application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, commands.echo))

    # whatever the fuck callbackquery is
    application.add_handler(CallbackQueryHandler(query_reader.query_reader))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates = Update.ALL_TYPES)

if __name__ == '__main__':
    main()