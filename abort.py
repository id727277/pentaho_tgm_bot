import telebot
from credentials import my_token, chat_id

tb = telebot.TeleBot(my_token)

tb.send_message(chat_id, 'The job aborted')