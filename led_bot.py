!pip install adafruit-io
!pip install python-telegram-bot
import os  
x=os.getenv('x') 
y=os.getenv('y')
from Adafruit_IO import Client, Feed
aio = Client(x,y)
feed=Feed(name='m_bot')
result = aio.create_feed(feed)
from telegram.ext import Updater,CommandHandler
from Adafruit_IO import Data
import requests
def get_url():
    contents= requests.get('https://io.adafruit.com/Gagana_N/feeds/bot/woof')
    url = contents['url']
    return url
def on(bot,update):
    url=get_url()
    chat_id= update.message.chat_id
    value=Data(value=1)
    value_send = aio.create_data('bot',value)
    bot.send_value(chat_id,value=url)
def off(bot,update):
    url=get_url()
    chat_id= update.message.chat_id
    value=Data(value=0)
    value_send = aio.create_data('bot',value)
    bot.send_value(chat_id,value=url)
api_updater = Updater('1369964976:AAH6AgEZzaW7ddFqo3LDhXLNszQ2r_RahGU')
dispatch = api_updater.dispatcher
dispatch.add_handler(CommandHandler('on',on))
api_updater.start_polling()
api_updater.idle()
