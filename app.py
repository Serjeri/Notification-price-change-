from businessLogic import test
from DataAsses.dataBase import Database
from aiogram import Bot, Dispatcher, executor, types
from ConfigFile.urlConfig import TOKEN
import time
import asyncio
import aioschedule

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dispatcher = Dispatcher(bot)
db = Database()


@dispatcher.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["/notices"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Hello", reply_markup=keyboard)


@dispatcher.message_handler(commands="notices")
async def get_price(message: types.Message):
    user_id = [message.chat.id][0]
    await message.answer("Please waiting...")

    await message.answer(test(user_id))
#     await timer("notices")


# async def timer(message):
#     aioschedule.every(15).seconds.do(
#         get_price, message)
#     while True:
#         await aioschedule.run_pending()
#         await asyncio.sleep(1)


def main():
    executor.start_polling(dispatcher)


if __name__ == "__main__":
    main()
