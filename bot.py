
# 6152593183:AAFOdf9b8gYGq2Vsh-OwDPMtR2G_po4I9sE

import telebot
from telebot import types

import config

bot = telebot.TeleBot(config.token)


# Обычный режим
@bot.message_handler(content_types=["text"])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="💥 Антитеррор", callback_data="test")
    keyboard.add(callback_button)
    callback_button = types.InlineKeyboardButton(text="💳 Коррупция", callback_data="test2")
    keyboard.add(callback_button)
    bot.send_message(message.chat.id, "Я – сообщение из обычного режима", reply_markup=keyboard)


# Инлайн-режим с непустым запросом
@bot.inline_handler(lambda query: len(query.query) > 0)
def query_text(query):
    kb = types.InlineKeyboardMarkup()
    # Добавляем колбэк-кнопку с содержимым "test"
    kb.add(types.InlineKeyboardButton(text="Нажми меня", callback_data="test"))
    results = []
    single_msg = types.InlineQueryResultArticle(
        id="1", title="Press me",
        input_message_content=types.InputTextMessageContent(message_text="Я – сообщение из инлайн-режима"),
        reply_markup=kb
    )
    results.append(single_msg)
    bot.answer_inline_query(query.id, results)
    
def query_text(query2):
    kb = types.InlineKeyboardMarkup()
    # Добавляем колбэк-кнопку с содержимым "test"
    kb.add(types.InlineKeyboardButton(text="Нажми меня2", callback_data="test2"))
    results2 = []
    single_msg2 = types.InlineQueryResultArticle(
        id="1", title="Press me2",
        input_message_content=types.InputTextMessageContent(message_text="Я – сообщение из инлайн-режима2"),
        reply_markup=kb
    )
    results2.append(single_msg2)
    bot.answer_inline_query(query2.id, results2)
    

# В большинстве случаев целесообразно разбить этот хэндлер на несколько маленьких
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "test":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Опишите ситуацию, в которой Вы столкнулись с терроризмом")
        if call.data == "test2":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Опишите ситуацию, в которой Вы столкнулись с коррупцией")    
    # Если сообщение из инлайн-режима
    elif call.inline_message_id:
        if call.data == "test":
            bot.edit_message_text(inline_message_id=call.inline_message_id, text="Бдыщь")

if __name__ == '__main__':
    bot.infinity_polling()