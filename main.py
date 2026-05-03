import telebot
from telebot import types
import os

# Yangi tokenni olingan manbadan qo'yamiz
TOKEN = '8686631877:AAGPYph1O86lpNHhf_dwjtvQtCQqFFMaF94'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    # Web App manzilingiz
    webapp_url = "https://t.me/Oyinlar_Pro_bot/Tetris" 
    btn = types.InlineKeyboardButton("O'yinni boshlash 🎮", url=webapp_url)
    markup.add(btn)
    
    welcome_text = (
        f"Salom, {message.from_user.first_name}! 👋\n\n"
        "🌟 Bu botda xohlagan o'yiningizni o'ynab ko'ring!\n\n"
        "Hozircha botda Tetris o'yini mavjud. 🚀"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode="Markdown")

# Serverda bot doimiy yoniq turishi uchun
if __name__ == "__main__":
    print("Bot serverda ishga tushdi...")
    bot.infinity_polling()
  
