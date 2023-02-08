import telebot
from telebot import types
from datetime import datetime
import time

# get current datetime
dt = datetime.now()
weekday = dt.weekday()
now = datetime.now() 
current_time = now.strftime("%H:%M")

token='5657785114:AAEncE2ntbN6Cpb8L3m598hXg2NRU-a_U0Y'

bot=telebot.TeleBot(token)
admins = [117955336]

@bot.message_handler(commands=['start'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("АСОИ-1")
    item2=types.KeyboardButton("ПОВТ-1")
    item3=types.KeyboardButton("ПОВТ-2")
    item4=types.KeyboardButton("ПОВТ-3")
    item5=types.KeyboardButton("ПОВТ-4")
    item6=types.KeyboardButton("ПОАС-1")
    item7=types.KeyboardButton("ПОАС-2")
    item8=types.KeyboardButton("ПОАС-3")
    item9=types.KeyboardButton("ПОАС-4")
    item10=types.KeyboardButton("ДПО-1")
    item11=types.KeyboardButton("ДПО-2")
    item12=types.KeyboardButton("ПИ-1")
    item13=types.KeyboardButton("ПИ-2")
    item14=types.KeyboardButton("ПИ-3")
    item15=types.KeyboardButton("ПИ-4")
    item16=types.KeyboardButton("ПИ-5")
    item17=types.KeyboardButton("ПИ-6")
    item18=types.KeyboardButton("ЭУБД-1")
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15, item16, item17, item18,)
    bot.send_message(message.chat.id, "Привет, {0.first_name}! \nЯ бот, который будет тебе отпрaвлять расписание сегодняшнего дня-каждое утро".format(message.from_user, bot.get_me(),reply_markup=markup))
    bot.send_message(message.chat.id,'Выберите свою группу:',reply_markup=markup)

@bot.message_handler(message='ПОАС-1')
def message_reply(message):
    while weekday == 4:
        if hour == 14:
            if minute == 54:
                bot.send_message(message.chat.id,"Расписание среды:\n✅Русский язык 8:00 - 9:20\n✅Физика 9:30 - 10:50\n✅Экономика 11:00 - 12:20\n✅Бекэнд 12:50 - 14:00")

bot.polling(none_stop=True, interval=0)