import telebot
from telebot.types import InlineKeyboardMarkup


bot = telebot.TeleBot("6411147170:AAH-jhd1QRXotV7nf5QUyd7782cHDxfCO1w", parse_mode=None)
bot1 = telebot.TeleBot("6430933115:AAFX3zEypA4ayW5X9WlksN7njKnFHCpo1OQ", parse_mode=None)


@bot1.message_handler(content_types=['text'])
def apply_orders(message):
    global time
    if message.text[-1] == '✅':
        bot1.send_message(message.chat.id, message.text[:-1] + ' Подтвержден')
        bot.send_message(chat_id=int(message.text[:-1]), text='Ваша запись подтверждена☑\nБуду рада видеть вас у себя в студии, по адресу 22 Апреля 38к8, 3 этаж, офис 310.\nМой номер для связи 89045868486📱\nЕсли что-то изменится , предупредите пожалуйста заранее 💓\nХорошего дня 🌸')
    elif message.text[-1] == '❌':
        bot1.send_message(message.chat.id, message.text[:-1] + ' Отклонен. Надо перезвонить!')
        bot.send_message(chat_id=int(message.text[:-1]),
                         text='Данное время занято. Ожидайте. В ближайшее время с вами свяжется мастер.')


bot1.infinity_polling()