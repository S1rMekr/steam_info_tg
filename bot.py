import asyncio
import logging

from aiogram import Bot, Dispatcher

from app import handlers
from config import Config, load_config

logger = logging.getLogger(__name__)

async def main():

    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )

    logger.info('Starting Bot')

    config: Config = load_config()

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()


    dp.include_router(handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())