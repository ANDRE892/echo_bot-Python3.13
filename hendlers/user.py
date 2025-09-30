from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command, CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


router_users = Router()


@router_users.message(CommandStart())
async def start(message: Message):
    user_id = message.from_user.id

    await message.answer(f'Ваш user_id ={user_id}')

    keyboard =(
        InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Вперед", callback_data="forward")],
                [InlineKeyboardButton(text="Назад", callback_data="back")]
            ]
        ))

    await message.answer('Пример вывода кнопок', reply_markup=keyboard)

    # await message.answer(
    #     'Пример вывода кнопок',
    #     reply_markup=InlineKeyboardMarkup(
    #         inline_keyboard=[
    #             [InlineKeyboardButton(text="Вперед", callback_data="forward")],
    #             [InlineKeyboardButton(text="Назад", callback_data="back")]
    #         ]
    #     )
    # )


@router_users.callback_query(F.data == "forward")
async def forward(callback: CallbackQuery):
    await callback.message.answer('Вы нажали вперед')


@router_users.callback_query(F.data == "back")
async def back(callback: CallbackQuery):
    await callback.message.answer('Вы нажали назад')
