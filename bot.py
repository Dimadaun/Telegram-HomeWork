import telebot
import datetime

TOKEN = "8333569336:AAEnRfkvPqODM_HqYdhMfrH_2qtdf68bXxc"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_message(message):
    text = message.text.strip()
    parts = text.split(" ", 1)

    if len(parts) == 2:
        subject, task = parts
        # Берём текущую дату в формате ДД.ММ.ГГГГ
        date_now = datetime.datetime.now().strftime("%d.%m.%Y")

        formatted = (
            f"📅 Дата: {date_now}\n"
            f"📚 Предмет: {subject}\n"
            f"📝 Задача: {task}"
        )

        bot.send_message(message.chat.id, formatted)

        # Удаляем исходное сообщение
        try:
            bot.delete_message(message.chat.id, message.message_id)
        except:
            pass
    else:
        bot.send_message(message.chat.id, "❗Пиши так: предмет + задание\nПример: математика сделать дз")

print("Бот запущен...")
bot.polling(none_stop=True)
