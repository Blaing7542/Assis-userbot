import random
import asyncio
import time
from pyrogram import Client, filters

api_id = 'apiid'
api_hash = 'apihash'

app = Client("my_userbot", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.command("help", prefixes="."))
async def help_command(client, message):
    await message.edit_text("**Команды:**\n`.bull` - буллинг\n`.info` - инфо о юб\n`.doubletext` - удваивает текст. пример: *ппррииввеетт!*\n`.ping` - показывает пинг юб\n`.new` - показывает изменения в юб")

@app.on_message(filters.command("bull", prefixes="."))
async def bull_command(client, message):
    bull_variants = [
        "СОСИ ЯЙЦА",
        "Я твою маму бум бум",
        "Терпилу обосанного не спрашивали",
        "Маме будешь так говорить",
        "Пошёл нахуй",
        "Слышь ты, черкаш обосанный, мамку свою проверил? Она в мой сперме)",
        "Помнишь, тебе девушка не отвечала целый месяц? Она всё время сосала мой хуй, и мы ебались с ней)",
        "Ты чё как Борис Рыжий? Он хоть-бы изменился, а ты за ним повторяешь - хуй сосёшь))",
        "Чума волосатая, тебя мама в детстве била, что ты такой злой?",
        "Мы твою маму ебали всей группой, радуйся))",
        "Мне кажется, когда тебя спросили *вилкой в глаз или в попу раз?*, ты выбрал второе))",
        "Мы с твоим отцом маму ебали. Она так приятно сосёт))",
        "Ты блять, сын фермера, ты как с отчимом разговариваешь?"
        "Мне твой папа сказал, что когда они ебались, то презик порвался))"
    ]

    await message.edit_text(random.choice(bull_variants))

@app.on_message(filters.command("info", prefixes="."))
async def info_command(client, message):
    await message.delete()  # Удаляем сообщение пользователя
    await app.send_photo(
        chat_id=message.chat.id,
        photo="путь к фото",
        caption="**✨Assis by Blaing**\n__🔧Version: 1.1__\nNew: command `.new`"
    )

@app.on_message(filters.command("ping", prefixes="."))
def ping_pong(client, message):
    start_time = time.time()
    pong_message = message.reply_text("Понг!")
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000, 1)
    message.delete()
    pong_message.edit_text(f"Понг! Пинг: {ping_time}ms")

@app.on_message(filters.command("doubletext", prefixes="."))
async def animtext_command(client, message):
    text = message.text.split(".doubletext ", 1)[1]
    animated_text = ""
    for char in text:
        animated_text += char + char
    await message.edit_text(animated_text)

@app.on_message(filters.command("new", prefixes="."))
async def new_command(client, message):
    await message.edit_text("Что нового в версии 1.1:\nКуча прикольных слов в .bull\nНовые команды: .doubletext, .new\nДоработана команда .ping\nИзменён дизайн")

app.run()