import telebot


bot = telebot.TeleBot("6411147170:AAH-jhd1QRXotV7nf5QUyd7782cHDxfCO1w", parse_mode=None)
bot2 = telebot.TeleBot('6674876215:AAH-GM7zhieswuS1x1_5VDfnmo8pWrRpV0E', parse_mode="MARKDOWN")

@bot2.message_handler(content_types=['text'])
def apply_orders(message):
    global time
    if message.text[-1] == '✅':
        bot2.send_message(message.chat.id, message.text[:-1] + ' Подтвержден')
        bot.send_message(chat_id=int(message.text[:-1]), text='Ваша запись подтверждена☑\n Буду рада видеть вас у себя в студии, по адресу 22 Апреля 38к8, 3 этаж, офис 310.\n Мой номер для связи 89045868486📱\n Если что-то изменится , предупредите пожалуйста заранее 💓\n Хорошего дня 🌸')
    elif message.text[-1] == '❌':
        bot2.send_message(message.chat.id, message.text[:-1] + ' Отклонен. Надо перезвонить!')
        bot.send_message(chat_id=int(message.text[:-1]),
                         text='Данное время занято. Ожидайте. В ближайшее время с вами свяжется мастер.')


bot2.infinity_polling()