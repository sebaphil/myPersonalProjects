from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from threading import Timer
from datetime import datetime
import unittest
import datetime as dt
import time
import urllib2

#from telegram.ext import Updater
#from telegram.ext import CommandHandler

#updater = Updater(token='370180173:AAGzxqLGE1PcOy8vJ7sm6sUvjVhgNfUih08')
#dispatcher = updater.dispatcher

#def start(bot, update):
#    bot.sendMessage(chat_id = update.message.chat_id, text="prova")

#start_handler = CommandHandler('start',start)
#dispatcher.add_handler(start_handler)

#updater.start_polling()



def internet_on():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib2.URLError as err: 
        return False

def wait_connection():	
	while(not internet_on()):
		print("Waiting for connection...")
		sleep(5)
