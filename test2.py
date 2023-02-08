import telebot
import time
import datetime

API_TOKEN = '5657785114:AAEncE2ntbN6Cpb8L3m598hXg2NRU-a_U0Y'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет, {0.first_name}! \nЯ бот, который будет тебе отпрaвлять расписание сегодняшнего дня-каждое утро")

def get_time():
    return datetime.datetime.now().strftime("%H:%M")

def monday():
    now = get_time()
    if now == "19:10":
        bot.send_message(chat_id='1179455336', text='Расписание среды:\n✅Математика 8:00 - 9:20\n✅Астраномия 9:30 - 10:50\n✅Бэкенд 11:00 - 12:20')

def tuesday():
    now = get_time()
    if now == "19:09":
        bot.send_message(chat_id='1179455336', text='Good night!')

while True:
    try:
        monday()
        tuesday()
        time.sleep(60)
    except Exception as e:
        print(e)
        time.sleep(60)
