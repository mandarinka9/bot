import telebot
from telebot import types
import random

bot = telebot.TeleBot("6443005340:AAH50hoExFn6eROQt12-SoWJDv9EWxUtr8g")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Что делает бот?")
    btn2 = types.KeyboardButton("цитата или фраза")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}!".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Что делает бот?"):
        bot.send_message(message.chat.id, text="Он может прислать тебе фразу или цитатку)")
    elif(message.text == "цитата или фраза"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("цитата")
        btn2 = types.KeyboardButton("фраза")
        back = types.KeyboardButton("вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="выбери", reply_markup=markup)
    elif (message.text == "фраза"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("грустная фраза")
        btn2 = types.KeyboardButton("веселая фраза")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text="выбери", reply_markup=markup)
    elif (message.text == "грустная фраза"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = types.KeyboardButton("еще одну грустную фразу")
        btn4 = types.KeyboardButton("вернуться в главное меню")
        markup.add(btn3, btn4)
        bot.send_message(message.chat.id, text=random.choice(grfr), reply_markup=markup)
    elif (message.text == "еще одну грустную фразу"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = types.KeyboardButton("еще одну грустную фразу")
        btn4 = types.KeyboardButton("вернуться в главное меню")
        markup.add(btn3, btn4)
        bot.send_message(message.chat.id, text=random.choice(grfr), reply_markup=markup)
    elif (message.text == "веселая фраза"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = types.KeyboardButton("еще одну веселую фразу")
        btn4 = types.KeyboardButton("вернуться в главное меню")
        markup.add(btn3, btn4)
        bot.send_message(message.chat.id, text=random.choice(vsfr), reply_markup=markup)
    elif (message.text == "еще одну веселую фразу"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = types.KeyboardButton("еще одну веселую фразу")
        btn4 = types.KeyboardButton("вернуться в главное меню")
        markup.add(btn3, btn4)
        bot.send_message(message.chat.id, text=random.choice(vsfr), reply_markup=markup)
    elif (message.text == "цитата"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("грустная цитата")
        btn2 = types.KeyboardButton("веселая цитата")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text="выбери", reply_markup=markup)
    elif (message.text == "грустная цитата"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = types.KeyboardButton("еще одну грустную цитату")
        btn4 = types.KeyboardButton("вернуться в главное меню")
        markup.add(btn3, btn4)
        bot.send_message(message.chat.id, text=random.choice(grcit), reply_markup=markup)
    elif (message.text == "еще одну грустную цитату"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = types.KeyboardButton("еще одну грустную цитату")
        btn4 = types.KeyboardButton("вернуться в главное меню")
        markup.add(btn3, btn4)
        bot.send_message(message.chat.id, text=random.choice(grcit), reply_markup=markup)
    elif (message.text == "веселая цитата"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = types.KeyboardButton("еще одну веселую цитату")
        btn4 = types.KeyboardButton("вернуться в главное меню")
        markup.add(btn3, btn4)
        bot.send_message(message.chat.id, text=random.choice(vscit), reply_markup=markup)
    elif (message.text == "еще одну веселую цитату"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = types.KeyboardButton("еще одну веселую цитату")
        btn4 = types.KeyboardButton("вернуться в главное меню")
        markup.add(btn3, btn4)
        bot.send_message(message.chat.id, text=random.choice(vscit), reply_markup=markup)
    elif (message.text == "вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Что делает бот?")
        button2 = types.KeyboardButton("цитата или фраза")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован.")


grfr = ["Весь мир может быть тебе не нужен. Если ты не нужен одному единственному человеку.", "Мы постоянно тратим себя не на то, не на тех.", "Плата за индивидуальность — одиночество.", "Сложнее всего забывать тех людей, с которыми ты забывал обо всём.", "Мы стараемся забыть, зная, что всегда будем помнить.", "Люди становятся близкими постепенно, чужими – мгновенно."]
vsfr = ["Курить вредно, пить противно, а умирать здоровым обидно.", "Удача улыбается смелым.", "Берегите ум — не раскидывайте мозгами.", "Если меня не заставлять, меня не надо уговаривать.", "Помним то, что было, ценим то, что есть."]
grcit = ["Люди еще больший яд, чем алкоголь или табак. ©Эрих Мария Ремарк", "От трудов праведных не наживёшь палат каменных. ©Русские пословицы", "Я люблю и любима. Увы, это не один и тот же человек. ©Янина Ипохорская", "Новый Год — это грустное расставание со старыми иллюзиями и радостная встреча с новыми. ©Фаина Раневская", "Я был готов любить весь мир, - меня никто не понял: и я выучился ненавидеть. ©Михаил Лермонтов"]
vscit = ["Вдохновение – это не селедка, которую можно засолить на многие годы. ©Гёте", "У кого есть кошка, тот может не бояться одиночества. ©Даниель Дефо", "Жизнь добрых людей – вечная молодость. ©Нодье", "Ключи от счастья – это мечты, воплотившиеся в жизнь. ©Николас Спаркс", "Нет причин не идти на зов своего сердца. ©Стив Джобс"]

bot.polling(none_stop=True)