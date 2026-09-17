import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Logging module: helps in debugging / writing logs
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# This is the function that defines bot behaviour on the /start command, 2 params: the type of request(update) and the body/message of the request.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Howdy. This is runLog.")

async def howami(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="im a bot man, what do you expect?")

if __name__ == '__main__':
    # Setup step: Essentially an abstracted/high level method of the ApplicationBuilder class that handles listening and other bot events
    application = ApplicationBuilder().token('8905062795:AAFOK1libGTrrJR-gwufVop908s_lOjMdJg').build()

    # Listners
    start_handler = CommandHandler('start', start)
    howami_handler = CommandHandler('whoami', howami)

    # Handler objects
    application.add_handler(start_handler)
    application.add_handler(howami_handler)

    # Runs the bot till I close the server (Ctrl + C)
    application.run_polling()