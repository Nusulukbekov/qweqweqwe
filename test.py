import telebot
import time
import datetime

API_TOKEN = '5657785114:AAEncE2ntbN6Cpb8L3m598hXg2NRU-a_U0Y'

bot = telebot.TeleBot(API_TOKEN)

def send_message():
    current_time = datetime.datetime.now()
    day_of_week = current_time.strftime("%A")
    message = "Расписание среды:\n✅Математика 8:00 - 9:20\n✅Астраномия 9:30 - 10:50\n✅Бэкенд 11:00 - 12:20" + day_of_week
    bot.send_message(chat_id='1179455336', text=message)

while True:
    current_time = datetime.datetime.now()
    if current_time.strftime("%A") == "Monday" and current_time.hour == 6 and current_time.minute == 30:
        send_message()
        time.sleep(60 * 60 * 24)
    elif current_time.strftime("%A") == "Tuesday" and current_time.hour == 6 and current_time.minute == 30:
        send_message()
        time.sleep(60 * 60 * 24)
    elif current_time.strftime("%A") == "Wednesday" and current_time.hour == 6 and current_time.minute == 30:
        send_message()
        time.sleep(60 * 60 * 24)
    elif current_time.strftime("%A") == "Thursday" and current_time.hour == 6 and current_time.minute == 30:
        send_message()
        time.sleep(60 * 60 * 24)
    elif current_time.strftime("%A") == "Friday" and current_time.hour == 6 and current_time.minute == 30:
        send_message()
        time.sleep(60 * 60 * 24)
    else:
        time.sleep(60)
