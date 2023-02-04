from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
from ConfigFile.config import URL,TOKEN
from product import get_product
import json

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Ноутбуки","Телефоны"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Hello", reply_markup=keyboard)


@dispatcher.message_handler(Text(equals="Ноутбуки"))
async def get_discount(message: types.Message):
    await message.answer("Please waiting...")

    get_product(url=URL)

    with open("ProductResult/product.json", encoding='utf-8') as file:
        data = json.load(file)

    for item in data:
        card = f"{hlink(item.get('name'), item.get('url'))}\n"\
            f"{hbold('Цена: ')} {item.get('price')}\n"\

        await message.answer(card)


def main():
    executor.start_polling(dispatcher)


if __name__ == "__main__":
    main()
