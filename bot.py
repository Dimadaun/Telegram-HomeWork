import telebot
import datetime
import os
from flask import Flask
from threading import Thread

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise ValueError("❌ Ошибка: TELEGRAM_BOT_TOKEN не найден! Добавь его в Secrets.")

bot = telebot.TeleBot(TOKEN)

# Вставь сюда ID нужного топика
TOPIC_ID = 68829 # <-- поменяй на ID своего топика

app = Flask('')

@app.route('/')
def home():
    return "✅ Бот работает!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_message(message):
    # Проверяем, что сообщение пришло из топика и совпадает ID
    if hasattr(message, 'message_thread_id') and message.message_thread_id == TOPIC_ID:
        text = message.text.strip()
        parts = text.split(" ", 1)

        if len(parts) == 2:
            subject, task = parts
            date_now = datetime.datetime.now().strftime("%d.%m.%Y")

            formatted = (
                f"📅 Дата: {date_now}\n"
                f"📚 Предмет: {subject}\n"
                f"📝 Задача: {task}"
            )

            bot.send_message(message.chat.id, formatted)

            try:
                bot.delete_message(message.chat.id, message.message_id)
            except:
                pass
        else:
            bot.send_message(message.chat.id, "❗Пиши так: предмет + задание\nПример: математика сделать дз")
    else:
        # Игнорируем сообщения из других топиков или общего чата
        pass

print("✅ Бот запущен...")
keep_alive()
bot.polling(none_stop=True)            f"📚 Предмет: {subject}\n"
            f"📝 Задача: {task}"
        )

        bot.send_message(message.chat.id, formatted)

        try:
            bot.delete_message(message.chat.id, message.message_id)
        except:
            pass
    else:
        bot.send_message(message.chat.id, "❗Пиши так: предмет + задание\nПример: математика сделать дз")

print("✅ Бот запущен...")
keep_alive()
bot.polling(none_stop=True)
