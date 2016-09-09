from telebot import util
import telebot
import sys
import urllib2
import json
import logging
import random
import urllib
import time
import logging
import subprocess
import requests
import os
reload(sys)
from telebot import types
sys.setdefaultencoding("utf-8")

bot = telebot.TeleBot('276815499:AAEDX6l__u4iObZE1BFBGSq1oOJNEOpbPBU')

@bot.message_handler(func=lambda message: True)
def m(m):
    if m.text == '/boobs':
        cid = m.chat.id
        req = urllib2.Request("http://api.oboobs.ru/noise/1")
        opener = urllib2.build_opener()
        f = opener.open(req)
        parsed_json = json.loads(f.read())
        rrrr = parsed_json[0]['preview']
        rrrrr = "http://media.oboobs.ru/{}".format(rrrr)
        urllib.urlretrieve (rrrrr, "boobs.jpg")
        photo = open('boobs.jpg', 'rb')
        bot.send_photo(cid, photo)
        bot.send_photo(cid, "FILEID")
    if m.text == '/butts':
        cid = m.chat.id
        req = urllib2.Request("http://api.obutts.ru/noise/1")
        opener = urllib2.build_opener()
        f = opener.open(req)
        parsed_json = json.loads(f.read())
        rrrr = parsed_json[0]['preview']
        rrrrr = "http://media.obutts.ru/{}".format(rrrr)
        urllib.urlretrieve (rrrrr, "butts.jpg")
        photo = open('butts.jpg', 'rb')
        bot.send_photo(cid, photo)
        bot.send_photo(cid, "FILEID")
    if m.text == '/leave':
        bot.leave_chat(m.chat.id)
        print 'command leave'
        print '{}'.format(m.from_user.first_name)
        print '{}'.format(m.from_user.username)
@bot.message_handler(commands=['boobs'])
def handler(m):
    cid = m.chat.id
    req = urllib2.Request("http://api.oboobs.ru/noise/1")
    opener = urllib2.build_opener()
    f = opener.open(req)
    parsed_json = json.loads(f.read())
    rrrr = parsed_json[0]['preview']
    rrrrr = "http://media.oboobs.ru/{}".format(rrrr)
    urllib.urlretrieve (rrrrr, "boobs.jpg")
    photo = open('boobs.jpg', 'rb')
    bot.send_photo(cid, photo)
    bot.send_photo(cid, "FILEID")


bot.polling(none_stop=True, timeout=20)
