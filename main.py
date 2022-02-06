from telegram import Bot
from telegram.ext import *
import response as R

print("Bot başladı..")

API_KEY = "5245067435:AAGOUPMqOXQJce7N-lYLE_QE_5QYWjIKHFo"


def start(update, context):
    update.message.reply_text(
        "/bilgi blokismi şeklinde kodular dökümanlarında kayıtlı olan blokların resimlerini getirebilirsin.")


def mesajGonder(update, context):
    input = str(update.message.text)
    mesaj = ""
    if "/bilgi " in input:
        mesaj = input.split("/bilgi ")[1]
    resim = R.blokGetir(mesaj)

    bot = Bot(API_KEY)
    chat_id = update.message.chat_id
    bot.send_document(chat_id, resim)


def mesajGelince():
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("bilgi", mesajGonder))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    mesajGelince()
