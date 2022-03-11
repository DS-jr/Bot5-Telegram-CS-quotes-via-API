from telegram.ext import Updater, CommandHandler, InlineQueryHandler, MessageHandler, Filters
import requests
import json

bot5_token = "BOT_TOKEN"   # Enter your Bot's Token here. You get this Token when registering a new Bot on Telegram.

def get_url():
    a5 = requests.get("http://quotes.stormconsultancy.co.uk/random.json").json()
    url5 = a5["quote"]
    return url5

def random(update, context):
    url6 = get_url()
    chat_id5 = update.message.chat_id
    context.bot.send_message(chat_id=chat_id5, text=url6)

def main():
    updater5 = Updater(bot5_token)
    dp5 = updater5.dispatcher
    dp5.add_handler(CommandHandler("random", random))
    updater5.start_polling()
    updater5.idle()

if __name__ == "__main__":
    main()
