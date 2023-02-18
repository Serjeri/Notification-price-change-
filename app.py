import json
from DataAsses.DataBase import Database
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
from ConfigFile.urlConfig import URL, TOKEN
from product import get_product

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dispatcher = Dispatcher(bot)
db = Database()


@dispatcher.message_handler(commands="start")
async def start(message: types.Message):
    user_id = [message.chat.id][0]

    if db.search_user(user_id) is None:
        db.add_user(user_id)

    start_buttons = ["Смотрим цену ноутбуков Apple"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Hello", reply_markup=keyboard)


@dispatcher.message_handler(Text(equals="Смотрим цену ноутбуков Apple"))
async def get_discount(message: types.Message):
    user_id = [message.chat.id][0]
    await message.answer("Please waiting...")
    
    get_product(URL, user_id)

    data = db.show_product_user(user_id)

    for item in data:
        card = f"{hlink(item[1], item[2])}\n"\
            f"{hbold('Старая цена: ')} {item[3]} RSD\n"\
            f"{hbold('Новая Цена: ')} {item[4]} RSD\n"\
            f"{hbold('Скидка: ')} -{item[5]}% \n"\

        await message.answer(card)


def main():
    executor.start_polling(dispatcher)


if __name__ == "__main__":
    main()
