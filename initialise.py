# sends test notification
# creates a db table

import os
import sys
import psycopg2
import base64
import telebot

CHAT_ID = os.environ['CHAT_ID']
API_KEY = os.environ['API_KEY']
DATABASE_URL = os.environ['DATABASE_URL']

bot = telebot.TeleBot(API_KEY)
bot.send_message(CHAT_ID, "Test Message from Reconator !")

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()

# to save the result of recon on target
cur.execute('''

create table output (

domain varchar(20),
result varchar(10000000)

);

''')
conn.commit()

# to save targets in queue
cur.execute('''

create table queue (

id varchar(5),
target varchar(50)

);

''')
conn.commit()

cur.close()
conn.close()
