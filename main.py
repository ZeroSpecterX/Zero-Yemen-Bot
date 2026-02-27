# Zero-Yemen-Bimport os
import telebot
from flask import Flask

# التوكن الخاص بك
TOKEN = '8636560889:AAFS3r9WqQe-xvqyASYD8XGj-4zhnBXFirk'
bot = telebot.TeleBot(TOKEN)

# كود صغير عشان Render ما يقفل البوت (Web Server)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "أهلاً بك يا زعيم zeropx! 🕵️‍♂️\nبوت الاستخبارات الخاص بك شغال الآن في السحاب.")

@bot.message_handler(func=lambda message: True)
def search(message):
    query = message.text
    bot.reply_to(message, f"جاري البحث عن: {query}...\n(هنا سنضيف لاحقاً قواعد بيانات الأرقام والحسابات) 🚀")

@server.route("/")
def webhook():
    return "Bot is Running!", 200

if __name__ == "__main__":
    # تشغيل البوت
    import threading
    threading.Thread(target=lambda: bot.infinity_polling()).start()
    # تشغيل السيرفر لـ Render
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
ot
