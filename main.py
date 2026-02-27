import os
import telebot
from holehe import core
import asyncio
import threading
from flask import Flask

TOKEN = '8636560889:AAFS3r9WqQe-xvqyASYD8XGj-4zhnBXFirk'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

async def check_email(email):
    # أداة holehe الحقيقية للبحث عن الإيميل في أكثر من 120 موقع
    out = []
    modules = core.import_submodules("holehe.modules")
    websites = core.get_functions(modules)
    for website in websites:
        try:
            await core.perform_instanciation(website, email, out)
        except:
            pass
    return out

@bot.message_handler(func=lambda message: "@" in message.text)
def handle_email(message):
    email = message.text.strip()
    bot.reply_to(message, f"🔎 جاري فحص الإيميل {email} في أكثر من 120 موقع (حسابات حقيقية)...")
    
    # تشغيل البحث الحقيقي
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    results = loop.run_until_complete(check_email(email))
    
    found = [res["name"] for res in results if res["exists"]]
    
    if found:
        response = "✅ **تم إيجاد حسابات مرتبطة في:**\n\n" + "\n".join(f"- {name}" for name in found)
    else:
        response = "❌ لم يتم العثور على حسابات مشهورة مرتبطة بهذا الإيميل."
    
    bot.send_message(message.chat.id, response, parse_mode='Markdown')

@app.route("/")
def index(): return "Bot is Live!", 200

if __name__ == "__main__":
    threading.Thread(target=lambda: bot.infinity_polling()).start()
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
