# @alexey_vorozhcov_bot

import logging
from aiogram import Bot, Dispatcher, executor, types
from config_reader import config

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Для записей с типом Secret* необходимо
# вызывать метод get_secret_value(),
# чтобы получить настоящее содержимое вместо '*******'
API_TOKEN = config.bot_token.get_secret_value()

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

#Явно указываем в декораторе, на какую команду реагируем.
@dp.message_handler(commands=['start'])  
async def send_welcome(message: types.Message):
   await message.reply("Привет!\nЯ Эхо-бот от Skillbox!\nОтправь мне любое сообщение, а я тебе обязательно отвечу.") 
   #Так как код работает асинхронно, то обязательно пишем await.
   
   
# Создаём новое событие, которое запускается в ответ на любой текст, введённый пользователем.
@dp.message_handler()
# Создаём функцию с простой задачей — отправить обратно тот же текст, что ввёл пользователь.
async def echo(message: types.Message):
   await message.answer(message.text)


@dp.message(commands=["test"])
async def any_message(message: types.Message):
    await message.answer("Hello, <b>world</b>!", parse_mode="HTML")
    await message.answer("Hello, *world*\!", parse_mode="MarkdownV2")


if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)
