from telebot import types
KANALLAR = [
    "@murodbek_rashidov"
]
def check_subscription(bot, user_id):
    for kanal in KANALLAR:
        try:
            user = bot.get_chat_member(kanal, user_id)
            if user.status in ["left", "kicked"]:
                return False
        except:
            return False
    return True
def subscription_buttons():
    markup = types.InlineKeyboardMarkup()
    for kanal in KANALLAR:
        btn = types.InlineKeyboardButton(
            text=f"➕ {kanal}",
            url=f"https://t.me/{kanal.replace('@', '')}"
        )
        markup.add(btn)
    check_btn = types.InlineKeyboardButton(
        text="✅ Obuna bo'ldim",
        callback_data="check_sub"
    )
    markup.add(check_btn)
    return markup