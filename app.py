from DataAsses.DataBase import Database
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
from ConfigFile.urlConfig import URL, TOKEN
from product import Product
import time
import asyncio
import aioschedule

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dispatcher = Dispatcher(bot)
db = Database()
product = Product()


@dispatcher.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = [
        "Смотрим цену ноутбука и подписаться на уведомления"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Hello", reply_markup=keyboard)


@dispatcher.message_handler(Text(equals="Смотрим цену ноутбука и подписаться на уведомления"))
async def get_discount(message: types.Message):
    user_id = [message.chat.id][0]
    await message.answer("Please waiting...")

    product.get_product(URL, user_id)

    data = db.show_product_user(user_id)

    for item in data:
        if product.result_product['price'] == item[2]:
            card = f"{hlink(item[0], item[1])}\n"\
                f"{hbold('Цена: ')} {item[2]} RSD\n"\

            await message.answer(card)
        else:
            for item in data:
                card = f"{hlink(item[0], item[1])}\n"\
                    f"{hbold('Цена изминилась: ')} {item[2]} RSD\n"\

                await message.answer(card)
    await timer("Смотрим цену ноутбука и подписаться на уведомления")


async def timer(message):
    aioschedule.every(5).seconds.do(
        get_discount, message)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(10)


def main():
    executor.start_polling(dispatcher)


if __name__ == "__main__":
    main()
