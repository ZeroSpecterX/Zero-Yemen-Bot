import os
import telebot
import threading  # هذه اللي كانت ناقصة وسببت المشكلة!
from flask import Flask

# التوكن الخاص بك
TOKEN = '8636560889:AAFS3r9WqQe-xvqyASYD8XGj-4zhnBXFirk'
bot = telebot.TeleBot(TOKEN)

# إنشاء سيرفر Flask عشان Render يظل شغال
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    welcome_msg = (
        "🕵️‍♂️ **مرحباً بك في رادار Zero-Yemen!**\n\n"
        "أنا بوتك الاستخباراتي السحابي. أرسل لي الآن:\n"
        "1️⃣ **إيميل** لفحص حساباته المسجلة.\n"
        "2️⃣ **رقم هاتف** للبحث عن هوية صاحبه.\n\n"
        "🚀 الحالة: متصل بالسحاب 24/7"
    )
    bot.reply_to(message, welcome_msg, parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def handle_search(message):
    query = message.text
    bot.reply_to(message, f"🔎 جاري فحص `{query}` في قواعد البيانات... انتظر ثواني.")
    
    # هنا محاكاة ذكية للنتائج (سأعلمك ربط الـ API الحقيقي في الخطوة القادمة)
    result = (
        f"📊 **نتائج الاستعلام عن:** `{query}`\n\n"
        "✅ الحسابات المرتبطة: (Instagram, Facebook, WhatsApp)\n"
        "🔓 حالة التسريبات: لا يوجد تسريبات خطيرة حالياً.\n"
        "📍 المنطقة المتوقعة: اليمن 🇾🇪"
    )
    bot.send_message(message.chat.id, result, parse_mode='Markdown')

@app.route("/")
def index():
    return "Zero-Yemen Bot is Running!", 200

def run_telebot():
    bot.infinity_polling()

if __name__ == "__main__":
    # تشغيل البوت في مسار منفصل (Thread)
    threading.Thread(target=run_telebot).start()
    # تشغيل السيرفر على المنفذ المطلوب لـ Render
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)
