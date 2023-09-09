"""
Домашнее задание №1

Использование библиотек: ephem
"""
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
from datetime import date
import ephem

logging.basicConfig(filename="bot.log", level=logging.DEBUG) #не обращайте внимание на уровень DEBUG (мне он был нужен во время попыток разобраться)

def greet_user(update, context):
    print("Введен /start")
    update.message.reply_text(f"Здравствуй, пользователь! Ты ввел команду /start\nНаш бот может показать текущее созвездие планеты, для этого введи команду /planet и название планеты в той же строке (пример: /planet Mars)")


def planett(update, context):
    planet_name = update.message.text.split()[-1]
    if planet_name in ["Mars", "Mercury", "Venus", "Saturn", "Jupiter", "Pluto", "Uranus", "Neptune"]:
        planet = getattr(ephem, planet_name)()
        planet.compute(ephem.Date(date.today()))
        const = ephem.constellation(planet)
        update.message.reply_text(const)
    else:
        update.message.reply_text("Не можем вычислить созвездие. Введите правильное название планеты")


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher

    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planett))


    logging.info("Бот начал работу")

    mybot.start_polling()

    mybot.idle()


if __name__ == "__main__":
    main()
