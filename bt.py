import telebot
from telebot import types
import random

bot = telebot.TeleBot('6835262207:AAFwciHTQyO1-FHf5KAtsc0KCz1dgaxSvVU')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Barev! {0.first_name}".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton('Top 10 Xaxery')
        btn2 = types.KeyboardButton('Top 10 Filmery')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, ' Inch es uzum nayenq❓', reply_markup=markup) 
            
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Insta🤫', url='https://www.instagram.com/__nar3k._/')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Karas follow ynles esli chto😉", reply_markup = markup)

    elif message.text == 'Top 10 Xaxery':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        bot.send_message(message.from_user.id, f'1.The Withcer 3\n2.Red Dead Redemption 2\n3.God of War: Ragnarök\n4.Одни из нас\n5.The Legend of Zelda: Ocarina of Time \n6.Mass Effect: Legendary Edition\n7.Metal Gear Solid\n8.Grand Theft Auto V\n9.God of War\n10.Uncharted 4: Путь вора ', parse_mode='Markdown' )
        btn1 = types.KeyboardButton('1.The Withcer 3')
        btn2 = types.KeyboardButton('2.Red Dead Redemption 2')
        btn3 = types.KeyboardButton('3.God of War: Ragnarök')
        btn4 = types.KeyboardButton('4.Одни из нас')
        btn5 = types.KeyboardButton('5.The Legend of Zelda: Ocarina of Time')
        btn6 = types.KeyboardButton('6.Mass Effect: Legendary Edition')
        btn7 = types.KeyboardButton('7.Metal Gear Solid')
        btn8 = types.KeyboardButton('8.Grand Theft Auto V')
        btn9 = types.KeyboardButton('9.God of War')
        btn10 = types.KeyboardButton('10.Uncharted 4: Путь вора')
        btn11 = types.KeyboardButton('🔙')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)
        bot.send_message(message.from_user.id, 'Vory hetaqrqrec?', reply_markup= markup)
    
    elif message.text == '1.The Withcer 3':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='hxumy IMDb-ov', url='https://www.imdb.com/title/tt5667286/?ref_=ttls_li_tt')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Aveli shat informacia ", reply_markup = markup)


    elif message.text == '2.Red Dead Redemption 2':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='hxumy IMDb-ov', url='https://www.imdb.com/title/tt6161168/?ref_=ttls_li_tt')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Aveli shat informacia ", reply_markup = markup)
        
    elif message.text == '3.God of War: Ragnarök':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='hxumy IMDb-ov', url='https://www.imdb.com/title/tt13119450/?ref_=ttls_li_tt')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Aveli shat informacia ", reply_markup = markup)

    elif message.text == '4.Одни из нас':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='hxumy IMDb-ov', url='https://www.imdb.com/title/tt2140553/?ref_=ttls_li_tt')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Aveli shat informacia ", reply_markup = markup)

    elif message.text == '5.The Legend of Zelda: Ocarina of Time':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='hxumy IMDb-ov', url='https://www.imdb.com/title/tt0184666/?ref_=ttls_li_tt')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Aveli shat informacia ", reply_markup = markup)

    elif message.text == '6.Mass Effect: Legendary Edition':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='hxumy IMDb-ov', url='https://www.imdb.com/title/tt14849728/?ref_=ttls_li_tt')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Aveli shat informacia ", reply_markup = markup)
    
    elif message.text == '7.Metal Gear Solid':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='hxumy IMDb-ov', url='https://www.imdb.com/title/tt0180825/?ref_=ttls_li_tt')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Aveli shat informacia ", reply_markup = markup)

    elif message.text == '8.Grand Theft Auto V':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='hxumy IMDb-ov', url='https://www.imdb.com/title/tt2103188/?ref_=ttls_li_tt')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Aveli shat informacia ", reply_markup = markup)
    
    elif message.text == '9.God of War':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='hxumy IMDb-ov', url='https://www.imdb.com/title/tt5838588/?ref_=ttls_li_tt')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Aveli shat informacia ", reply_markup = markup)
    
    elif message.text == '10.Uncharted 4: Путь вора':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='hxumy IMDb-ov', url='https://www.imdb.com/title/tt3334704/?ref_=ttls_li_tt')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Aveli shat informacia ", reply_markup = markup)

    elif message.text == '🔙':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton('Top 10 Xaxery')
        btn2 = types.KeyboardButton('Top 10 Filmery')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, '🔙', reply_markup= markup)
        
    elif message.text == 'Top 10 Filmery':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        bot.send_message(message.from_user.id, f'1.Побег из Шоушенка\n2.Крестный отец\n3.Тёмный рыцарь\n4.Крестный отец 2\n5.12 разгневанных мужчин \n6.Список Шиндлера\n7.Властелин колец: Возвращение короля\n8.Криминальное чтиво\n9.Властелин колец: Братство кольца\n10.Хороший, плохой, злой ', parse_mode='Markdown' )
        btn1 = types.KeyboardButton('1.Побег из Шоушенка')
        btn2 = types.KeyboardButton('2.Крестный отец')
        btn3 = types.KeyboardButton('3.Тёмный рыцарь')
        btn4 = types.KeyboardButton('4.Крестный отец 2')
        btn5 = types.KeyboardButton('5.12 разгневанных мужчин')
        btn6 = types.KeyboardButton('6.Список Шиндлера')
        btn7 = types.KeyboardButton('7.Властелин колец: Возвращение короля')
        btn8 = types.KeyboardButton('8.Криминальное чтиво')
        btn9 = types.KeyboardButton('9.Властелин колец: Братство кольца')
        btn10 = types.KeyboardButton('10.Хороший, плохой, злой')
        btn11 = types.KeyboardButton('🔙')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)
        bot.send_message(message.from_user.id, 'Vory hetaqrqrec?', reply_markup= markup)
    
    elif message.text == '1.Побег из Шоушенка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='hxumy IMDb-ov', url='https://www.imdb.com/title/tt0111161/?ref_=chttp_t_1')
        bot.send_message(message.from_user.id, "Aveli shat informacia ", reply_markup = markup)


    elif message.text == '2.Крестный отец':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='hxumy IMDb-ov', url='https://www.imdb.com/title/tt0068646/?ref_=chttp_t_2')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Aveli shat informacia ", reply_markup = markup)
        
    elif message.text == '3.Тёмный рыцарь':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='hxumy IMDb-ov', url='https://www.imdb.com/title/tt0468569/?ref_=chttp_t_3')
        markup.add(btn1)
        
        bot.send_message(message.from_user.id, "Aveli shat informacia ", reply_markup = markup)

    elif message.text == '4.Крестный отец 2':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='hxumy IMDb-ov', url='https://www.imdb.com/title/tt0071562/?ref_=chttp_t_4')
        markup.add(btn1)
        
        bot.send_message(message.from_user.id, "Aveli shat informacia ", reply_markup = markup)

    elif message.text == '5.12 разгневанных мужчин':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='hxumy IMDb-ov', url='https://www.imdb.com/title/tt0050083/?ref_=chttp_t_5')
        markup.add(btn1)
        
        bot.send_message(message.from_user.id, "Aveli shat informacia ", reply_markup = markup)

    elif message.text == '6.Список Шиндлера':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='hxumy IMDb-ov', url='https://www.imdb.com/title/tt0108052/?ref_=chttp_t_6')
        markup.add(btn1)
        
        bot.send_message(message.from_user.id, "Aveli shat informacia ", reply_markup = markup)
    
    elif message.text == '7.Властелин колец: Возвращение короля':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='hxumy IMDb-ov', url='https://www.imdb.com/title/tt0167260/?ref_=chttp_t_7')
        markup.add(btn1)
        
        bot.send_message(message.from_user.id, "Aveli shat informacia ", reply_markup = markup)

    elif message.text == '8.Криминальное чтиво':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='hxumy IMDb-ov', url='https://www.imdb.com/title/tt0110912/?ref_=chttp_t_8')
        markup.add(btn1)
        
        bot.send_message(message.from_user.id, "Aveli shat informacia ", reply_markup = markup)
    
    elif message.text == '9.Властелин колец: Братство кольца':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='hxumy IMDb-ov', url='https://www.imdb.com/title/tt0120737/?ref_=chttp_t_9')
        markup.add(btn1)
        
        bot.send_message(message.from_user.id, "Aveli shat informacia ", reply_markup = markup)
    
    elif message.text == '10.Хороший, плохой, злой':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='hxumy IMDb-ov', url='https://www.imdb.com/title/tt0060196/?ref_=chttp_t_10')
        markup.add(btn1)
        
        bot.send_message(message.from_user.id, "Aveli shat informacia ", reply_markup = markup)

    
bot.polling(none_stop=True, interval=0) 