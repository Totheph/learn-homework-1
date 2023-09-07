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
  text = update.message.text.split()
  planet = text[-1]
  if planet.lower() == "mars":
      mars = ephem.Mars()
      mars.compute(ephem.Date(date.today()))
      const = ephem.constellation(mars)
      update.message.reply_text(const)
  elif planet.lower() == "venus":
      venus = ephem.Venus()
      venus.compute(ephem.Date(date.today()))
      const = ephem.constellation(venus)
      update.message.reply_text(const)
  elif planet.lower() == "mercury":
      mercury = ephem.Mercury()
      mercury.compute(ephem.Date(date.today()))
      const = ephem.constellation(mercury)
      update.message.reply_text(const)
  elif planet.lower() == "jupiter":
      jupiter = ephem.Jupiter()
      jupiter.compute(ephem.Date(date.today()))
      const = ephem.constellation(jupiter)
      update.message.reply_text(const)
  elif planet.lower() == "saturn":
      saturn = ephem.Saturn()
      saturn.compute(ephem.Date(date.today()))
      const = ephem.constellation(saturn)
      update.message.reply_text(const)
  elif planet.lower() == "uranus":
      uranus = ephem.Uranus()
      uranus.compute(ephem.Date(date.today()))
      const = ephem.constellation(uranus)
      update.message.reply_text(const)
  elif planet.lower() == "neptune":
      neptune = ephem.Neptune()
      neptune.compute(ephem.Date(date.today()))
      const = ephem.constellation(neptune)
      update.message.reply_text(const)
  else:
      update.message.reply_text("Не можем вычислить созвездие")


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
