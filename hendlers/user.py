from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command, CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


router_users = Router()

# Словарь для хранения количества скринов от каждого пользователя
user_screenshots = {}


@router_users.message(CommandStart())
async def start(message: Message):
    # Сбрасываем счетчик скринов при /start
    user_screenshots[message.from_user.id] = 0
    await message.answer("Приветик, я могу подарить подарок за 400 ⭐️, осталось 68 штучек ✌️Но есть задание")
    await message.answer('''<b>1. Лайкни и напиши "спасибо" под комментарием с которого узнали обо мне!</b> - только не забудь!⚡️

<b>2. Напиши под 10 любых видео этот текст👇</b> 

<code>капец @НАЗВАНИЕБОТА всем по подарку дарит😌</code>

<b>‼️ОБЯЗАТЕЛЬНО ЛАЙКНИ ВСЕ СВОИ КОММЕНТЫ‼️</b>

Когда будет готово не забудь скинуть скрины!!!''', parse_mode='HTML')


@router_users.message(F.photo)
async def handle_screenshots(message: Message):
    user_id = message.from_user.id
    
    # Инициализируем счетчик если пользователь новый
    if user_id not in user_screenshots:
        user_screenshots[user_id] = 0
    
    # Увеличиваем счетчик скринов
    user_screenshots[user_id] += 1
    
    # Проверяем количество скринов
    if user_screenshots[user_id] < 10:
        await message.answer(f"Получено скринов: {user_screenshots[user_id]}/10")
    elif user_screenshots[user_id] == 10:
        await message.answer("<b>3. И последнее, подпишись на Всех спонсоров, а то у меня не будет денег на твой подарок 💰</b> \n\nУ тебя есть 15 часов!!! после чего я начну проверять и дарить. 🎁", parse_mode='HTML')
        await message.answer(
            "Вот тут спонсоры -> @НАЗВАНИЕБОТА ❤️\n\n"
            "Добавь их в архив и выключить звук, чтобы не мешали!\n\n"
            "<b>Вернись и напиши когда будет готово!! ✅ Скрины не надо, я сам увижу когда буду проверять</b>\n\n"
            "<b>‼️Среди тех кто выполнит условия я сегодня дополнительно разыграю 15 премок на год</b>", parse_mode='HTML'
        )
