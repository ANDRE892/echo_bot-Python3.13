import asyncio
from config import bot, dp
from hendlers.user import router_users

Allowed_updates = ['message', 'edited_message', 'callback_query']

async def main():
    dp.include_routers(router_users)
    print("Роутер подключены")
    print("Бот запущен и сообщения пропущены")
    await dp.start_polling(bot, allowed_updates=Allowed_updates)

if __name__ == "__main__":
    asyncio.run(main())
