from telebot import TeleBot, types
from tg import check_subscription, subscription_buttons
TOKEN = "8651315250:AAGZgRj9jBOGKxe1dS5u07D5GO1ldRACmb8"
bot = TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if not check_subscription(bot, user_id):
        bot.send_message(
            message.chat.id,
            "❌ Botdan foydalanish uchun kanalga obuna bo'ling",
            reply_markup=subscription_buttons()
        )
        return
    ism = message.from_user.first_name
    familiya = message.from_user.last_name
    if ism and familiya:
        user = f"{ism} {familiya}"
    elif ism:
        user = ism
    elif familiya:
        user = familiya
    else:
        user = "Foydalanuvchi"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1-telefon raqamim")
    btn2 = types.KeyboardButton("2-telefon raqamim")
    btn3 = types.KeyboardButton("Instagramdan yozish")
    btn4 = types.KeyboardButton("Telegramdan yozish")
    btn5 = types.KeyboardButton("Murodbek haqida to'liq ma'lumot")
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    markup.row(btn5)
    bot.send_message(
        message.chat.id,
        f"Assalomu alaykum xush kelibsiz {user}",
        reply_markup=markup
    )
@bot.callback_query_handler(func=lambda call: call.data == "check_sub")
def check_sub(call):
    user_id = call.from_user.id
    if check_subscription(bot, user_id):
        bot.answer_callback_query(
            call.id,
            "✅ Obuna tasdiqlandi"
        )
        start(call.message)
    else:
        bot.answer_callback_query(
            call.id,
            "❌ Hali kanalga obuna bo'lmagansiz",
            show_alert=True
        )
# 1-raqam
@bot.message_handler(func=lambda message: message.text == "1-telefon raqamim")
def phone1(message):
    markup = types.InlineKeyboardMarkup()
    contact = types.InlineKeyboardButton(
        "📱 Kontaktga qo'shish",
        url="https://t.me/+998882220310"
    )
    markup.add(contact)
    bot.send_message(
        message.chat.id,
        "📞 +998 88 222 03 10",
        reply_markup=markup
    )
# 2-raqam
@bot.message_handler(func=lambda message: message.text == "2-telefon raqamim")
def phone2(message):
    markup = types.InlineKeyboardMarkup()
    contact = types.InlineKeyboardButton(
        "📞 Kontaktga qo'shish",
        url="https://t.me/+998874710310"
    )
    markup.add(contact)
    bot.send_message(
        message.chat.id,
        "📱 +998 87 471 03 10",
        reply_markup=markup
    )
# Instagram
@bot.message_handler(func=lambda message: message.text == "Instagramdan yozish")
def instagram(message):
    bot.send_message(
        message.chat.id,
        "💻 https://www.instagram.com/murodbe_k_uz/"
    )
# Telegram
@bot.message_handler(func=lambda message: message.text == "Telegramdan yozish")
def telegram(message):
    bot.send_message(
        message.chat.id,
        "📝 @Rash1d0v"
    )
# To'liq ma'lumot
@bot.message_handler(
    func=lambda message: message.text == "Murodbek haqida to'liq ma'lumot"
)
def toliqmalumot(message):
    bot.send_message(
        message.chat.id,
        """👤 Murodbek Rashidov haqida
📅 2011-yil 10-martda tug‘ilganman
💻 Hozirda Python dasturlash tilida
"Back End" yo‘nalishida o‘qiyman
👨‍🏫 Ustozim:
Umarov Abduaziz
📱 Telegram:
@umarov_group_of
📞 +998 88 278 11 99
👨‍👩‍👦 Oilada bitta o‘g‘ilman
💍 Uylanmaganman
👨 Dadam:
Abduvohid Malopov
📱 @Malopov
📞 +998 99 755 59 73
✉️ Kerak bo‘lib qolsam:
Instagram va Telegram orqali yozishingiz mumkin."""
    )
bot.infinity_polling()