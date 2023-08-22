import random
import asyncio
import time
import tgcrypto
import pyrogram
from pyrogram import Client, filters
from pytube import YouTube

api_id = ''
api_hash = ''  # Api_id и Api_hash находятся на сайте https://my.telegram.org/apps.

app = Client("my_bot", api_id=api_id, api_hash=api_hash)
userid_telegram = 123456789  # Здесь должен быть ваш ID аккаунта.
blacklist = []

open("bldb.txt", "a").close()

with open("bldb.txt", "r") as file:
    for line in file:
        user_id = int(line.strip())
        blacklist.append(user_id)

@app.on_message(filters.command("help", prefixes="."))
async def help_command(_, message):
    await message.edit_text("**Команды:**\n`.bull` - буллинг\n`.info` - инфо о юб\n`.doubletext` - удваивает текст. пример: *ппррииввеетт!*\n`.ping` - показывает пинг юб\n`.caz` - делает ставку на что-угодно. пример: *.caz 2 доллара*\n`.downvid` - скачивает видео с YouTube по запросу пользователя\n`.addbl` - добавить пользователя в чёрный список. Он не сможет пользоваться командами вашего юб.\n`.delbl` - удалить пользователя из чёрного списка.\n`.animtext` - анимирует текст.\n`.ab` - автоматический буллинг\n`delab` - убрать из автоматического булла.\n`.who` - выбирает рандомного чела, и пишет кто он.")

@app.on_message(filters.command("bull", prefixes="."))
async def bull_command(_, message):
    if message.from_user.id in blacklist:
        await message.reply_text("Вы находитесь в чёрном списке.")
        return

    bull_variants = [
        "СОСИ ЯЙЦА",
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
        "Ты мой секс раб, а я твой владелец. Быстро соси мне хуй!",
        "Жди своего отчима дома. Он хочет тебя выебать в рот))",
        "Пошёл нахуй черкаш ебанный",
        "Даун, иди вскройся",
        "Альтушка ебанная, иди дрочи к-поперам",
        "Бля, я твою мать камазом перехуярил",
        "ты ахуел чмо ебаное",
        "Иди нахуй ебло тупое тебя в подворотне я изнасилую",
        "ТВОЙ ПИЗДЕЖ БЕЗ ДОКАЗАТЕЛЬСТВ НЕ ИМЕЕТ ВЕСА",
        "ПОШЁЛ НАХУЙ СЫН ШЛЮХИ. ТЫ КТО ТАКОЙ БЛЯТЬ ЧТОБЫ ПИСАТЬ ПРО СВОЮ МАТЬ? ОНА ЕБАННАЯ ШЛЮХА, И ВСЁ ЭТО ЗНАЮТ",
        "ТВОЯ МАТЬ И ОТЕЦ ПРОСИЛИ ПЕРЕДАТЬ ЧТО ТЫ ЕБАНАТ",
        "ВЫ ВСЕ КОНЧЕННЫЕ ДОЛБОЕБЫ",
        "подкидыш ебаный наверни говнища да побольше",
        "пошла нахуй женщина ебаная сдохни через минуту уебан",
        "рот закрой гнида обоссаная про плач и хуи только и говорит уебан конченый",
        "бля ты как будто у зеркала стоишь - тупо стрелки метаешь",
        "В социуме меня считают гением а тебя воспринимают как за лоха который доедает за мной",
        "Иди нахуй моё поколение самое умное а ты тупое создание завидуй молчи",
        "Иди нахуй альтушка иди блять умойся",
        "Ты раб этого достаточно а теперь живо за работу",
        "Посмеялись а теперь в поле пахать будешь",
        "У тебя нет хуя ты раб тупой сколько раз тебе объяснять чмо ебливое",
        "Мнение таджика не учитывается",
        "Ахаххаах ебать ты нищ клоун чмо ебливое надеюсь в подворотне тебя таджики выебут",
        "чмо молчать нахуй"
    ]

    await message.edit_text(random.choice(bull_variants))

@app.on_message(filters.command("info", prefixes="."))
async def info_command(_, message):
    start_time = time.time()
    await message.delete()
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000, 1)
    await app.send_photo(
        chat_id=message.chat.id,
        photo="https://user-images.githubusercontent.com/127663348/259819077-e4efea31-d07d-4d82-88c7-ba86fea5a36e.jpg",
        caption=f"**✨Assis by Blaing**\n__🔧Version: 1.3__\nSource: [https://github.com/Blaing7542/Assis-userbot](https://github.com/Blaing7542/Assis-userbot)\n**Version for user❤**\n**Ping: {ping_time}ms**"
    )

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

@app.on_message(filters.command("addbl", prefixes="."))
async def add_blacklist_command(_, message):
    if message.from_user.id == userid_telegram:
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
    if message.from_user.id == userid_telegram:
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
            print("Превышен лимит сообщений в секунду. Подождите...")

ab_variants = [
        "СОСИ ЯЙЦА",
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
        "Ты мой секс раб, а я твой владелец. Быстро соси мне хуй!",
        "Жди своего отчима дома. Он хочет тебя выебать в рот))",
        "Пошёл нахуй черкаш ебанный",
        "Даун, иди вскройся",
        "Альтушка ебанная, иди дрочи к-поперам",
        "Бля, я твою мать камазом перехуярил",
        "ты ахуел чмо ебаное",
        "Иди нахуй ебло тупое тебя в подворотне я изнасилую",
        "ТВОЙ ПИЗДЕЖ БЕЗ ДОКАЗАТЕЛЬСТВ НЕ ИМЕЕТ ВЕСА",
        "ПОШЁЛ НАХУЙ СЫН ШЛЮХИ. ТЫ КТО ТАКОЙ БЛЯТЬ ЧТОБЫ ПИСАТЬ ПРО СВОЮ МАТЬ? ОНА ЕБАННАЯ ШЛЮХА, И ВСЁ ЭТО ЗНАЮТ",
        "ТВОЯ МАТЬ И ОТЕЦ ПРОСИЛИ ПЕРЕДАТЬ ЧТО ТЫ ЕБАНАТ",
        "ВЫ ВСЕ КОНЧЕННЫЕ ДОЛБОЕБЫ",
        "подкидыш ебаный наверни говнища да побольше",
        "пошла нахуй женщина ебаная сдохни через минуту уебан",
        "рот закрой гнида обоссаная про плач и хуи только и говорит уебан конченый",
        "бля ты как будто у зеркала стоишь - тупо стрелки метаешь",
        "В социуме меня считают гением а тебя воспринимают как за лоха который доедает за мной",
        "Иди нахуй моё поколение самое умное а ты тупое создание завидуй молчи",
        "Иди нахуй альтушка иди блять умойся",
        "Ты раб этого достаточно а теперь живо за работу",
        "Посмеялись а теперь в поле пахать будешь",
        "У тебя нет хуя ты раб тупой сколько раз тебе объяснять чмо ебливое",
        "Мнение таджика не учитывается",
        "Ахаххаах ебать ты нищ клоун чмо ебливое надеюсь в подворотне тебя таджики выебут",
        "чмо молчать нахуй"
    ]

@app.on_message(filters.command("ab", prefixes="."))
def autobull_command(client, message):
    replied_user_id = message.reply_to_message.from_user.id

    with open("ab.txt", "a") as file:
        file.write(str(replied_user_id) + "\n")

    random_variant = random.choice(ab_variants)
    message.reply_text("**Автобулл включен.**")

@app.on_message(filters.command("delab", prefixes="."))
def delab_command(client, message):
    user_id_to_remove = message.reply_to_message.from_user.id

    with open("ab.txt", "r") as file:
        user_ids = file.read().splitlines()

    user_ids = [user_id for user_id in user_ids if user_id != str(user_id_to_remove)]

    with open("ab.txt", "w") as file:
        file.write("\n".join(user_ids))

    message.reply_text("**Пользователь удален из списка автобулл.**")


@app.on_message(filters.command("who", prefixes="."))
def who_command(client, message):
    args = message.text.split()[1:]

    if args:
        members_count = client.get_chat_members_count(message.chat.id)

        members = client.get_chat_members(message.chat.id, limit=members_count)

        random_user = random.choice(list(members)).user

        response = f"@{random_user.username} {' '.join(args)}"
    else:
        response = "Неверно написано. Пример:\n`.who милый`"

    client.send_message(message.chat.id, response)


@app.on_message()
def handle_messages(client, message):
    with open("ab.txt", "r") as file:
        user_ids = file.read().splitlines()

    if str(message.from_user.id) in user_ids:
        random_variant = random.choice(ab_variants)
        message.reply_text(random_variant)

app.run()
