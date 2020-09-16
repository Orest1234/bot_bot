from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN

import random
import emoji
from db import films
from emj import *

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
f_films = []




@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(f"Привіт!{fun_face}\nВикористовуй ці команди щоб зрозуміти що я вмію{wink_face}\n/help , /random")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(f"Випадковий фільм!{hand_face} /random!")

@dp.message_handler(commands=['random'])
async def process_random_command(message: types.Message):
    g = random.choice(films)
    print(g)
    # if g not in f_films:
    #     await message.reply(f'{white_circle}Назва фільму:\n{g[1]}\n{white_circle}Опис фільму:\n{g[2]}\n{white_circle}Жанр: {g[3]}\n{white_circle}Дата випуску: {g[4]} ',reply=False)
    #     f_films.append(g)
    #
    # elif g in f_films:
    #     await process_random_command(message)
    if len(films) != len(f_films):
        if g not in f_films:
            await message.reply(f'{white_circle}Назва фільму:\n{g[1]}\n{white_circle}Опис фільму:\n{g[2]}\n{white_circle}Жанр: {g[3]}\n{white_circle}Дата випуску: {g[4]} ',reply=False)
            f_films.append(g)

        elif g in f_films:
            await process_random_command(message)
    else:
        await message.reply('Я не маю варіантів', reply=False)


# elif len(f_films) == len(films):
    #     await message.reply('Я не маю варіантів', reply=False)




        # if len(films) == 0:
    #     await message.reply('Я не маю варіантів',reply = False)
    # else:
    #     g = (random.choice(films))
    #     b = films.index(g)
    #     films.pop(b)




        # await message.reply(f'{white_circle}Назва фільму:\n{g[1]}\n{white_circle}Опис фільму:\n{g[2]}\n{white_circle}Жанр: {g[3]}\n{white_circle}Дата випуску: {g[4]} ',reply = False)


if __name__ == '__main__':
    executor.start_polling(dp)
