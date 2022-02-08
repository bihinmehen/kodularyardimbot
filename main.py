from telegram import Bot, ParseMode
from telegram.ext import *
import response as R

print("Bot başladı..")

API_KEY = "5245067435:AAGOUPMqOXQJce7N-lYLE_QE_5QYWjIKHFo"


def start(update, context):
    update.message.reply_text(
        "/bilgi blokismi şeklinde kodular dökümanlarında kayıtlı olan blokların resimlerini getirebilirsin. Veya /durum yazarak sunucuların durumunu öğrenebilirsin")


def mesajGonder(update, context):
    input = str(update.message.text)
    mesaj = input.split("/bilgi ")[1]
    resim = R.blokGetir(mesaj)

    bot = Bot(API_KEY)
    chat_id = update.message.chat_id
    bot.send_document(chat_id, resim)


def durumGonder(update, context):
    durumlar = R.durumGetir()
    if "TinyWebDB Service" in durumlar:
        del durumlar["TinyWebDB Service"]

    if not durumlar:
        update.message.reply_text("Tüm sunucular aktif")
    else:
        durumText = ""
        for isim, zaman in durumlar.items():
            durumText = durumText + \
                f"\n<b>{isim}</b> pasif. Son aktiflik : {R.zamanHesapla(zaman)}"
        update.message.reply_text(durumText, parse_mode=ParseMode.HTML)


def main():
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("bilgi", mesajGonder))
    dp.add_handler(CommandHandler("durum", durumGonder))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
