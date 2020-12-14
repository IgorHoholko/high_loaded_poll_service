import random
import telebot
import os
import requests


URL = 'http://localhost:5000/new_user'
TOKEN = os.environ['TOKEN']

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Yo wassup bro!")


@bot.message_handler(content_types=['text'])
def process(message):
    myobj = {"id": random.randint(10, 555555), "name": "Tel", "nickname": f"{random.randint(10, 555555)}", "language_code": "ru", "is_bot": 1}
    x = requests.post(URL, data=myobj)


bot.polling()