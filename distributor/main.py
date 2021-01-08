import random
import telebot
import os
import requests
import os
import subprocess
import json



URL = 'high_load_analyzer_1:5000/new_user'
TOKEN = os.environ['TOKEN']

bot = telebot.TeleBot(TOKEN)


# process = subprocess.Popen(['curl', '--header', '"Content-Type: application/json"',
#                             '--request', 'POST', ' --data', f'\'{json.dumps(myobj)}\'', URL ],
#                      stdout=subprocess.PIPE,
#                      stderr=subprocess.PIPE)
# stdout, stderr = process.communicate()
# print(stdout, '\n', stderr)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Yo wassup bro!")


@bot.message_handler(content_types=['text'])
def process(message):
    print(message)
    myobj = {"id": random.randint(10, 555555), "name": "Tel", "nickname": f"{random.randint(10, 555555)}", "language_code": "ru", "is_bot": True}
    os.system( f"""  curl --header "Content-Type: application/json"   --request POST   --data '{json.dumps(myobj)}' {URL}""")


bot.polling()