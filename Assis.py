import random
import asyncio
import time
import tgcrypto
import pyrogram
from pyrogram import Client, filters
from pytube import YouTube

api_id = 'апи ид'
api_hash = 'апи хеш'  # Api ID и Api Hash находятся на https://my.telegram.org/apps.

app = Client("my_bot", api_id=api_id, api_hash=api_hash)

blacklist = []

open("bldb.txt", "a").close()

with open("bldb.txt", "r") as file:
    for line in file:
        user_id = int(line.strip())
        blacklist.append(user_id)

@app.on_message(filters.command("help", prefixes="."))
async def help_command(_, message):
    await message.edit_text("**Команды:**\n`.bull` - буллинг\n`.info` - инфо о юб\n`.doubletext` - удваивает текст. пример: *ппррииввеетт!*\n`.ping` - показывает пинг юб\n`.caz` - делает ставку на что-угодно. пример: *.caz 2 доллара*\n`.downvid` - скачивает видео с YouTube по запросу пользователя\n`.addbl` - добавить пользователя в чёрный список. Он не сможет пользоваться командами вашего юб.\n`.delbl` - удалить пользователя из чёрного списка.\n`.animtext` - анимирует текст.")

@app.on_message(filters.command("bull", prefixes="."))
async def bull_command(_, message):
    if message.from_user.id in blacklist:
        await message.reply_text("Вы находитесь в чёрном списке.")
        return

    bull_variants = [
        "Полируй мои яйца, олух.",
        "Я твою маму бум бум",
        "Терпилу обосанного не спрашивали",
        "Маме будешь так говорить",
        "Пошёл нахуй",
        "Слышь ты, черкаш обосанный, мамку свою проверил? Она в мой сперме)",
        "Помнишь, тебе девушка не отвечала целый месяц? Она всё время сосала мой хуй, и мы ебались с ней)",
        "Ты чё как твоя мать? Она хоть-бы изменилась, а ты за ней повторяешь - хуй сосёшь))",
        "Чума волосатая, тебя мама в детстве била, что ты такой злой?",
        "Мы твою маму ебали всей группой, радуйся))",
        "Мне кажется, когда тебя спросили *вилкой в глаз или в попу раз?*, ты выбрал второе))",
        "Мы с твоим отцом маму ебали. Она так приятно сосёт))",
        "Ты блять, сын фермера, ты как с отчимом разговариваешь?",
        "Мне твой папа сказал, что когда они ебались, то презик порвался))",
        "А чего ты ещё в сети? Мама же сказала выключать",
        "Эй ты, шлюха, полировать яйца когда будешь?",
        "Писюнчик ещё не дорос до таких оскорблений",
        "Когда ты уже вспомнишь, что мне хуй сосал?",
        "Ты мой секс раб, а я твой владелец. Быстро соси мне хуй!"
    ]

    await message.edit_text(random.choice(bull_variants))

@app.on_message(filters.command("info", prefixes="."))
async def info_command(_, message):
    await message.delete()
    await app.send_photo(
        chat_id=message.chat.id,
        photo="https://user-images.githubusercontent.com/127663348/259346080-504b2ac5-9182-4151-aed6-8f5a99fcac13.png",
        caption="**✨Assis by Blaing**\n__🔧Version: 1.2__\nSource: https://github.com/Blaing7542/Assis-userbot\n**Version for user❤**"
    )

@app.on_message(filters.command("ping", prefixes="."))
async def ping_pong(_, message):
    start_time = time.time()
    pong_message = await message.reply_text("Понг!")
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000, 1)
    await message.delete()
    await pong_message.edit_text(f"Понг! Пинг: {ping_time}ms")

@app.on_message(filters.command("doubletext", prefixes="."))
async def animtext_command(_, message):
    text = message.text.split(".doubletext ", 1)[1]
    animated_text = ""
    for char in text:
        animated_text += char + char
    await message.edit_text(animated_text)

@app.on_message(filters.command("caz", prefixes="."))
async def caz_command(_, message):
    await asyncio.sleep(4)
    bet = message.text.split(".caz ", 1)[1]
    try:
        bet_amount, bet_text = bet.split(maxsplit=1)
        bet_amount = int(bet_amount)
        if bet_amount <= 0:
            await message.reply_text("Ставка должна быть положительным числом!")
            return
    except (ValueError, IndexError):
        await message.reply_text("Некорректная ставка!")
        return

    result = random.choice([0, 1])
    if result == 0:
        loss_amount = bet_amount
        await message.reply_text(f"Проигрыш! Вы проиграли {loss_amount} {bet_text}")
    else:
        win_amount = bet_amount * 2
        await message.reply_text(f"Выигрыш! Вы выиграли {win_amount} {bet_text}")

@app.on_message(filters.command("ping_all", prefixes="."))
async def ping_all_command(_, message):
    if message.from_user.id == your_id:  # Здесь необходим ваш ID телеграма.
        await message.reply_text("**вырезано и перенесено в https://github.com/Blaing7542/Ping-all-userbot**")
    else:
        await message.reply_text("У вас нет разрешения на использование этой команды.")

@app.on_message(filters.command("nuke", prefixes="."))
async def nuke_command(_, message):
    if message.from_user.id == your_id:  # Здесь необходим ваш ID телеграма.
        await message.reply_text("**вырезано и перенесено в https://github.com/Blaing7542/Ping-all-userbot**")
    else:
        await message.reply_text("У вас нет разрешения на использование этой команды.")

@app.on_message(filters.command("addbl", prefixes="."))
async def add_blacklist_command(_, message):
    if message.from_user.id == your_id:  # Здесь необходим ваш ID телеграма.
        user_id = message.reply_to_message.from_user.id
        if user_id not in blacklist:
            blacklist.append(user_id)
            with open("bldb.txt", "a") as file:
                file.write(str(user_id) + "\n")
            await message.reply_text("Пользователь добавлен в чёрный список. Теперь пользователь не может использовать все команды вашего юб.")
        else:
            await message.reply_text("Пользователь уже находится в чёрном списке.")
    else:
        await message.reply_text("У вас нет разрешения на использование этой команды.")

@app.on_message(filters.command("delbl", prefixes="."))
async def remove_blacklist_command(_, message):
    if message.from_user.id == your_id:  # Здесь необходим ваш ID телеграма.
        user_id = message.reply_to_message.from_user.id
        if user_id in blacklist:
            blacklist.remove(user_id)
            with open("bldb.txt", "w") as file:
                for id in blacklist:
                    file.write(str(id) + "\n")
            await message.reply_text("Пользователь удален из чёрного списка.")
        else:
            await message.reply_text("Пользователь не найден в чёрном списке.")
    else:
        await message.reply_text("У вас нет разрешения на использование этой команды.")

@app.on_message(filters.command("downvid", prefixes="."))
async def download_video_command(_, message):
    query = message.text.split(".downvid ", 1)[1]
    try:
        video = YouTube(query)
        video.streams.get_highest_resolution().download()
        await app.send_video(
            chat_id=message.chat.id,
            video="video.mp4",
            caption="Видео скачано успешно!"
        )
    except Exception as e:
        await message.reply_text(f"Видео установлено! Загляните в папку, где находится код")

@app.on_message(filters.command("animtext", prefixes='.') & filters.me)
async def animtext_command(_, message):
    input_text = message.text.split(".animtext ", maxsplit=1)[1]
    temp_text = input_text
    edited_text = ""
    typing_symbol = "█"

    while edited_text != input_text:
        try:
            await message.edit(edited_text + typing_symbol)
            time.sleep(0.1)
            edited_text = edited_text + temp_text[0]
            temp_text = temp_text[1:]
            await message.edit(edited_text)
            time.sleep(0.1)
        except FloodWait:
            print("что")

app.run()
