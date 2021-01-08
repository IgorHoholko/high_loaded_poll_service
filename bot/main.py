import telebot
import requests
import os
import json


URL_NEW_USER = 'http://host.docker.internal:6060/new_user'
URL_CHOOSE_ANSWER = 'http://host.docker.internal:6060/choose_answer'

TOKEN = os.environ['TOKEN']

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Yo wassup bro!")


@bot.message_handler(content_types=['text'])
def process(message):

    # user info collection
    user_id = message.__dict__['from_user'].__dict__['id']
    name = message.__dict__['from_user'].__dict__['first_name']
    username = message.__dict__['from_user'].__dict__['username']
    is_bot = message.__dict__['from_user'].__dict__['is_bot']
    language_code = message.__dict__['from_user'].__dict__['language_code']

    answer = int(message.text)

    person_obj = {"id": user_id, "name": name, "nickname": username, "language_code": language_code, "is_bot": is_bot}
    answer_obj = { "answer_id": answer, "user_id" : user_id}

    # Add new user
    try:
        requests.post(URL_NEW_USER, json=person_obj)
    except:
        pass

    # Add his answer
    requests.post(URL_CHOOSE_ANSWER, json=answer_obj)


bot.polling()