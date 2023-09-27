import telebot
from telebot import types
import itertools

token = "6411147170:AAH-jhd1QRXotV7nf5QUyd7782cHDxfCO1w"
bot = telebot.TeleBot(token, parse_mode="MARKDOWN")

bot1 = telebot.TeleBot("6430933115:AAFX3zEypA4ayW5X9WlksN7njKnFHCpo1OQ", parse_mode="MARKDOWN")
bot2 = telebot.TeleBot('6674876215:AAH-GM7zhieswuS1x1_5VDfnmo8pWrRpV0E', parse_mode="MARKDOWN")
order = []



@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton("Наращивание ресниц👀")
    btn2 = types.KeyboardButton("Маникюр💅")
    markup.row(btn1, btn2)
    bot.send_message(message.chat.id,
                     "Привет, какой услугой хочешь воспользоваться: наращивание ресниц, маникюр, педикюр?",
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def narach_prices(message):
    global order, time
    if message.text == 'Наращивание ресниц👀':
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        btn1 = types.KeyboardButton('Classic')
        btn2 = types.KeyboardButton("2D")
        btn3 = types.KeyboardButton("3D")
        btn4 = types.KeyboardButton("Снятие чужой работы")
        markup.row(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'Выберите вид услуги: classic, 2D, 3D, снятие чужой работы', reply_markup=markup)
        order.append('Наращивание ресниц')
    elif message.text == 'Classic':
        bot.send_message(message.chat.id, 'Стоимость: 1000 рублей')
        order.append(',Classic,')
        order.append(',1000 рублей,')
        a = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id,
                         "Отлично! Давайте определимся с датой🗓. Напишите удобное Вам число и время. Например: 12.03 в 17:00",
                         reply_markup=a)
    elif message.text == '2D':
        bot.send_message(message.chat.id, 'Стомость: 1100 рублей')
        order.append(',2D,')
        order.append(',1100 рублей,')
        a = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id,
                         "Отлично! Давайте определимся с датой🗓. Напишите удобное Вам число и время. Например: 12.03 в 17:00",
                         reply_markup=a)
    elif message.text == '3D':
        bot.send_message(message.chat.id, 'Стоимость: 1300 рублей')
        order.append(',3D,')
        order.append(',1300 рублей,')
        a = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id,
                         "Отлично! Давайте определимся с датой🗓. Напишите удобное Вам число и время. Например: 12.03 в 17:00",
                         reply_markup=a)
    elif message.text == 'Снятие чужой работы':
        bot.send_message(message.chat.id, 'Стоимость: 200 рублей')
        order.append(',Снятие чужой работы,')
        order.append(',200 рублей,')
        a = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id,
                         "Отлично! Давайте определимся с датой🗓. Напишите удобное Вам число и время. Например: 12.03 в 17:00",
                         reply_markup=a)
    elif message.text[:2] in [''.join(i) for i in itertools.product('0123456789', repeat=2) if
                           int(''.join(i)) <= 31] and message.text[3:5] in [''.join(i) for i in
                                                                         itertools.product('0123456789', repeat=2) if
                                                                         int(''.join(i)) <= 31]:
        a = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, "Укажите ваш номер телефона📱.", reply_markup=a)
        time = message.text
        order.append(message.text)
    elif (len(message.text) == 11 or len(message.text) == 12) and order[0] == 'Наращивание ресниц' and (
            '89' in message.text or '+79' in message.text):
        bot.send_message(message.chat.id,
                         'Запись создана и передана мастеру.Ожидайте подтверждения. Если хотите записаться повторно - напишите /start')
        order.append(',' + message.text)
        bot.send_message(message.chat.id, ''.join(order).replace(',,', ',').replace(',', ', ').replace(', ',
                                                                                                    '.\n') + '\n' + 'ID: ' + str(
            message.chat.id))
        bot1.send_message(chat_id=1190679768, text=''.join(order).replace(',,', ',').replace(',', ', ').replace(', ',
                                                                                                                '.\n') + '\n' + 'ID: ' + '`' + str(
            message.chat.id) + '`')
        order = []
    elif (len(message.text) == 11 or len(message.text) == 12) and (
            order[0] == 'Маникюр без покрытия,' or order[0] == 'Маникюр + покрытие,' or order[
        0] == 'Маникюр + покрытие + наращивание,') and ('89' in message.text or '+79' in message.text):
        bot.send_message(message.chat.id,
                         'Запись создана и передана мастеру. Ожидайте подтверждения. Если хотите записаться повторно - напишите /start')
        order.append(',' + message.text)
        order[1] = ''
        bot.send_message(message.chat.id, ''.join(order).replace(',,', ',').replace(',', ', ').replace(', ',
                                                                                                    '.\n') + '\n' + 'ID: ' + str(
            message.chat.id))
        bot2.send_message(chat_id=1190679768, text=''.join(order).replace(',,', ',').replace(',', ', ').replace(', ',
                                                                                                                '.\n') + '\n' + 'ID: ' + '`' + str(
            message.chat.id) + '`')
        order = []
    else:
        if message.text == 'Маникюр💅':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            btn1 = types.KeyboardButton('Маникюр без покрытия')
            btn2 = types.KeyboardButton('Маникюр + покрытие')
            btn3 = types.KeyboardButton("Маникюр + покрытие + наращивание")
            markup.row(btn1, btn2, btn3)
            bot.send_message(message.chat.id,
                             'Выберите вид услуги: маникюр (без покрытия), маникюр + покрытие, маникюр + покрытие + наращивание.',
                             reply_markup=markup)
        elif message.text == 'Маникюр без покрытия':
            order.append('Маникюр без покрытия,')
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            btn1 = types.KeyboardButton('Да')
            btn2 = types.KeyboardButton('Нет')
            markup.row(btn1, btn2)
            order.append('400')
            bot.send_message(message.chat.id,
                             "Вам нужен дизайн или другие опции?", reply_markup=markup)
        elif message.text == 'Маникюр + покрытие':
            order.append('Маникюр + покрытие,')
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            btn1 = types.KeyboardButton('Да')
            btn2 = types.KeyboardButton('Нет')
            markup.row(btn1, btn2)
            order.append('900')
            bot.send_message(message.chat.id,
                             "Вам нужен дизайн или другие опции?", reply_markup=markup)
        elif message.text == 'Маникюр + покрытие + наращивание':
            order.append('Маникюр + покрытие + наращивание,')
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            btn1 = types.KeyboardButton('Да')
            btn2 = types.KeyboardButton('Нет')
            markup.row(btn1, btn2)
            order.append('1300')
            bot.send_message(message.chat.id,
                             "Вам нужен дизайн или другие опции?", reply_markup=markup)
        elif message.text == 'Нет' and order[0] == 'Маникюр без покрытия,':
            bot.send_message(message.chat.id, 'Стоимость всей услуги: 400 рублей')
            order.append(',Стоимость всей услуги: 400 рублей,')
            bot.send_message(message.chat.id,
                             "Отлично! Давайте определимся с датой🗓. Напишите удобное Вам число и время. Например: 12.03 в 17:00🗓")
        elif message.text == 'Нет' and order[0] == 'Маникюр + покрытие,':
            bot.send_message(message.chat.id, 'Стоимость всей услуги: 400 рублей')
            order.append(',Стоимость всей услуги: 900 рублей,')
            bot.send_message(message.chat.id,
                             "Отлично! Давайте определимся с датой🗓. Напишите удобное Вам число и время. Например: 12.03 в 17:00🗓")
        elif message.text == 'Нет' and order[0] == 'Маникюр + покрытие + наращивание,':
            bot.send_message(message.chat.id, 'Стоимость всей услуги: 400 рублей')
            order.append(',Стоимость всей услуги: 1300 рублей,')
            bot.send_message(message.chat.id,
                             "Отлично! Давайте определимся с датой🗓. Напишите удобное Вам число и время. Например: 12.03 в 17:00🗓")
        elif message.text == 'Да':
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            btn1 = types.KeyboardButton('Градиент')
            btn2 = types.KeyboardButton('Френч')
            btn3 = types.KeyboardButton('Простые дизайны')
            markup.row(btn1, btn2, btn3)
            btn4 = types.KeyboardButton('Роспись без деталей')
            btn5 = types.KeyboardButton('Роспись с деталями')
            markup.row(btn4, btn5)
            btn6 = types.KeyboardButton('Моделирование')
            btn7 = types.KeyboardButton('Укрепление')
            markup.row(btn6, btn7)
            bot.send_message(message.chat.id, 'Выберите нужную вам опцию.', reply_markup=markup)
        elif message.text == 'Френч' or message.text == 'Укрепление':
            order.append(',' + message.text + ',')
            a = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, 'Стоимость всей услуги: ' + str(150 + int(order[1])), reply_markup=a)
            order.append(',' + 'Стоимость всей услуги: ' + str(150 + int(order[1])) + ',')
            bot.send_message(message.chat.id,
                             "Отлично! Давайте определимся с датой🗓. Напишите удобное Вам число и время. Например: 12.03 в 17:00🗓")
        elif message.text in (
        'Градиент', 'Простые дизайны', 'Роспись без деталей', 'Роспись с деталями', 'Моделирование', 'Укрепление'):
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            btn1 = types.KeyboardButton('1 ноготь')
            btn2 = types.KeyboardButton('2 ногтя')
            btn3 = types.KeyboardButton('3 ногтя')
            btn4 = types.KeyboardButton('4 ногтя')
            btn5 = types.KeyboardButton('5 ногтей')
            markup.row(btn1, btn2, btn3, btn4, btn5)
            btn6 = types.KeyboardButton('6 ногтей')
            btn7 = types.KeyboardButton('7 ногтей')
            btn8 = types.KeyboardButton('8 ногтей')
            btn9 = types.KeyboardButton('9 ногтей')
            btn10 = types.KeyboardButton('10 ногтей')
            markup.row(btn6, btn7, btn8, btn9, btn10)
            order.append(',' + message.text + ',')
            bot.send_message(message.chat.id, 'Укажите количество ногтей, на которые вам необходима опция.',
                             reply_markup=markup)
        elif order[2] == ',Градиент,' and message.text in (
        '1 ноготь', '2 ногтя', '3 ногтя', '4 ногтя', '5 ногтей', '6 ногтей', '7 ногтей', '8 ногтей', '9 ногтей',
        '10 ногтей'):
            a = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, 'Стоимость всей услуги: ' + str(int(message.text[0]) * 50 + int(order[1])),
                             reply_markup=a)
            order.append(',' + 'Стоимость всей услуги: ' + str(int(message.text[0]) * 50 + int(order[1])) + ',')
            bot.send_message(message.chat.id,
                             "Отлично! Давайте определимся с датой🗓. Напишите удобное Вам число и время. Например: 12.03 в 17:00")
        elif order[2] == ',Простые дизайны,' and message.text in ('1 ноготь', '2 ногтя'):
            a = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, 'Стоимость всей услуги: ' + str(50 + int(order[1])), reply_markup=a)
            order.append(',' + 'Стоимость всей услуги: ' + str(50 + int(order[1])) + ',')
            bot.send_message(message.chat.id,
                             "Отлично! Давайте определимся с датой🗓. Напишите удобное Вам число и время. Например: 12.03 в 17:00")
        elif order[2] == ',Простые дизайны,' and message.text in ('3 ногтя', '4 ногтя', '5 ногтей'):
            a = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, 'Стоимость всей услуги: ' + str(150 + int(order[1])), reply_markup=a)
            order.append(',' + 'Стоимость всей услуги: ' + str(150 + int(order[1])) + ',')
            bot.send_message(message.chat.id,
                             "Отлично! Давайте определимся с датой🗓. Напишите удобное Вам число и время. Например: 12.03 в 17:00")
        elif order[2] == ',Простые дизайны,' and message.text not in (
        '1 ноготь', '2 ногтя', '3 ногтя', '4 ногтя', '5 ногтей'):
            a = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, 'Стоимость всей услуги: ' + str(250 + int(order[1])), reply_markup=a)
            order.append(',' + 'Стоимость всей услуги: ' + str(250 + int(order[1])) + ',')
            bot.send_message(message.chat.id,
                             "Отлично! Давайте определимся с датой🗓. Напишите удобное Вам число и время. Например: 12.03 в 17:00")
        elif order[2] == ',Роспись без деталей,' and message.text in (
        '1 ноготь', '2 ногтя', '3 ногтя', '4 ногтя', '5 ногтей', '6 ногтей', '7 ногтей', '8 ногтей', '9 ногтей',
        '10 ногтей'):
            a = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, 'Стоимость всей услуги: ' + str(300 * int(message.text[:2]) + int(order[1])),
                             reply_markup=a)
            order.append(',' + 'Стоимость всей услуги: ' + str(300 * int(message.text[:2]) + int(order[1])) + ',')
            bot.send_message(message.chat.id,
                             "Отлично! Давайте определимся с датой🗓. Напишите удобное Вам число и время. Например: 12.03 в 17:00")
        elif order[2] == ',Роспись с деталями,' and message.text in (
        '1 ноготь', '2 ногтя', '3 ногтя', '4 ногтя', '5 ногтей', '6 ногтей', '7 ногтей', '8 ногтей', '9 ногтей',
        '10 ногтей'):
            a = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, 'Стоимость всей услуги: ' + str(400 * int(message.text[:2]) + int(order[1])),
                             reply_markup=a)
            order.append(',' + 'Стоимость всей услуги: ' + str(400 * int(message.text[:2]) + int(order[1])) + ',')
            bot.send_message(message.chat.id,
                             "Отлично! Давайте определимся с датой🗓. Напишите удобное Вам число и время. Например: 12.03 в 17:00")
        elif order[2] == ',Моделирование,' and message.text in (
        '1 ноготь', '2 ногтя', '3 ногтя', '4 ногтя', '5 ногтей', '6 ногтей', '7 ногтей', '8 ногтей', '9 ногтей',
        '10 ногтей'):
            a = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, 'Стоимость всей услуги: ' + str(50 * int(message.text[:2]) + int(order[1])),
                             reply_markup=a)
            order.append(',' + 'Стоимость всей услуги: ' + str(50 * int(message.text[:2]) + int(order[1])) + ',')
            bot.send_message(message.chat.id,
                             "Отлично! Давайте определимся с датой🗓. Напишите удобное Вам число и время. Например: 12.03 в 17:00")


bot.infinity_polling()
