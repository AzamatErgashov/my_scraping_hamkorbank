import requests as r
from telebot.types import KeyboardButton,ReplyKeyboardMarkup 
import telebot
from bs4 import BeautifulSoup as bs


TOKEN = "5275549753:AAEME_I2vfSn0hKpsksuiPUZmtlZrsd6PP0"
bot = telebot.TeleBot(TOKEN, parse_mode=None)
kurslar = []

def parsing(id,text=None):
    global kurs
    url = "https://hamkorbank.uz/exchange-rate/"
    res = r.get(url)
    html = bs(res.text,'html.parser')

    for item_2 in html.find_all('div', class_= 'list'):
        for i in item_2.find_all('ul', class_ = 'body'):
            # print(i.get_text())
            for item_a in i.find_all('li'):
                # print(item_a.get_text())
                kurslar.append(item_a.get_text())                                 

    bot.send_message(id,f"Валюта = <strong>{kurslar[0]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Код символа = <strong>{kurslar[1]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Курс ЦБ = <strong>{kurslar[2]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Покупка = <strong>{kurslar[3]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Продажа = <strong>{kurslar[4]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Динамика = <b>{kurslar[5]}</b>",parse_mode="HTML")


def parsing_new(id,text=None):
    global kurslar
    url = "https://hamkorbank.uz/exchange-rate/"
    res = r.get(url)
    html = bs(res.text,'html.parser')

    for item_2 in html.find_all('div', class_= 'list'):
        for i in item_2.find_all('ul', class_ = 'body'):
            # print(i.get_text())
            for item_a in i.find_all('li'):
                # print(item_a.get_text())
                kurslar.append(item_a.get_text())                                 

    bot.send_message(id,f"Валюта = <strong>{kurslar[12]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Код символа = <strong>{kurslar[13]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Курс ЦБ = <strong>{kurslar[14]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Покупка = <strong>{kurslar[15]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Продажа = <strong>{kurslar[16]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Динамика = <b>{kurslar[17]}</b>",parse_mode="HTML")

def parsing_now(id,text=None):
    global kurslar
    url = "https://hamkorbank.uz/exchange-rate/"
    res = r.get(url)
    html = bs(res.text,'html.parser')

    for item_2 in html.find_all('div', class_= 'list'):
        for i in item_2.find_all('ul', class_ = 'body'):
            # print(i.get_text())
            for item_a in i.find_all('li'):
                # print(item_a.get_text())
                kurslar.append(item_a.get_text())                                 

    bot.send_message(id,f"Валюта = <strong>{kurslar[6]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Код символа = <strong>{kurslar[7]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Курс ЦБ = <strong>{kurslar[8]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Покупка = <strong>{kurslar[9]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Продажа = <strong>{kurslar[10]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Динамика = <b>{kurslar[11]}</b>",parse_mode="HTML") 


def parsing_new(id,text=None):
    global kurslar
    url = "https://hamkorbank.uz/exchange-rate/"
    res = r.get(url)
    html = bs(res.text,'html.parser')

    for item_2 in html.find_all('div', class_= 'list'):
        for i in item_2.find_all('ul', class_ = 'body'):
            # print(i.get_text())
            for item_a in i.find_all('li'):
                # print(item_a.get_text())
                kurslar.append(item_a.get_text())                                 

    bot.send_message(id,f"Валюта = <strong>{kurslar[12]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Код символа = <strong>{kurslar[13]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Курс ЦБ = <strong>{kurslar[14]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Покупка = <strong>{kurslar[15]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Продажа = <strong>{kurslar[16]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Динамика = <b>{kurslar[17]}</b>",parse_mode="HTML")

def parsing_con(id,text=None):
    global kurslar
    url = "https://hamkorbank.uz/exchange-rate/"
    res = r.get(url)
    html = bs(res.text,'html.parser')

    for item_2 in html.find_all('div', class_= 'list'):
        for i in item_2.find_all('ul', class_ = 'body'):
            # print(i.get_text())
            for item_a in i.find_all('li'):
                # print(item_a.get_text())
                kurslar.append(item_a.get_text())                                 

    bot.send_message(id,f"Валюта = <strong>{kurslar[18]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Код символа = <strong>{kurslar[19]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Курс ЦБ = <strong>{kurslar[20]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Покупка = <strong>{kurslar[21]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Продажа = <strong>{kurslar[22]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Динамика = <b>{kurslar[23]}</b>",parse_mode="HTML")

def parsing_can(id,text=None):
    global kurslar
    url = "https://hamkorbank.uz/exchange-rate/"
    res = r.get(url)
    html = bs(res.text,'html.parser')

    for item_2 in html.find_all('div', class_= 'list'):
        for i in item_2.find_all('ul', class_ = 'body'):
            # print(i.get_text())
            for item_a in i.find_all('li'):
                # print(item_a.get_text())
                kurslar.append(item_a.get_text())                                 

    bot.send_message(id,f"Валюта = <strong>{kurslar[24]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Код символа = <strong>{kurslar[25]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Курс ЦБ = <strong>{kurslar[26]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Покупка = <strong>{kurslar[27]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Продажа = <strong>{kurslar[28]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Динамика = <b>{kurslar[29]}</b>",parse_mode="HTML")

def parsing_cashn(id,text=None):
    global kurslar
    url = "https://hamkorbank.uz/exchange-rate/"
    res = r.get(url)
    html = bs(res.text,'html.parser')

    for item_2 in html.find_all('div', class_= 'list'):
        for i in item_2.find_all('ul', class_ = 'body'):
            # print(i.get_text())
            for item_a in i.find_all('li'):
                # print(item_a.get_text())
                kurslar.append(item_a.get_text())                                 

    bot.send_message(id,f"Валюта = <strong>{kurslar[30]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Код символа = <strong>{kurslar[31]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Курс ЦБ = <strong>{kurslar[32]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Покупка = <strong>{kurslar[33]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Продажа = <strong>{kurslar[34]}</strong>",parse_mode="HTML")
    bot.send_message(id,f"Динамика = <b>{kurslar[35]}</b>",parse_mode="HTML")

@bot.message_handler(commands=['start'])
def my_func(message):
    print(message)
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    dolllar = KeyboardButton('$ - Dollar')
    rubl = KeyboardButton('₽ - Ruble')
    euro = KeyboardButton('€ - Euro')
    gpb = KeyboardButton('£ - Gbp')
    iena = KeyboardButton('¥ - Iena')
    frank = KeyboardButton('₣ - Shveytsariya franki')
    markup.add(dolllar,rubl,euro,gpb,iena,frank)
    bot.send_message(message.chat.id,f' Salom {message.from_user.first_name} Botimizga hush kelibsiz!', reply_markup=markup)
    bot.send_message(message.chat.id,f"{message.from_user.first_name} -- Bu bot sizga hozirgi mashxur 6ta valyutalarni so'mda qancha qiymatga tengligini ko'rsatadi !")
    bot.send_message(message.chat.id,'Sinash uchun tugmalardan birontasinni bosing')
@bot.message_handler(content_types=['text'])
def my_texts(message):
    if message.text == '$ - Dollar':
        parsing(message.chat.id)
    elif message.text == '₽ - Ruble' :
        parsing_new(message.chat.id)
    elif message.text == '€ - Euro':
        parsing_now(message.chat.id)
    elif message.text == '£ - Gbp':
        parsing_con(message.chat.id)
    elif message.text == '¥ - Iena':
        parsing_can(message.chat.id)
    elif message.text == '₣ - Shveytsariya franki':
        parsing_cashn(message.chat.id)    
bot.polling() 