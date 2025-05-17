import asyncio
from aiogram import Bot, Dispatcher, Router
from tgbot.handlers import router

class TGBot:
    def __init__(self, router: Router) -> None:
       token = config('TOKEN')
       self.bot = Bot(token)
       self.dp = Dispatcher()
       self.dp.include_router(router)
       if not config('DEBUG', default=False):
           loop = asyncio.get_event_loop()
           loop.run_until_complete(self.set_commands())
           loop.run_until_complete(self.set_webhook())

    async def update_bot(self, update: dict) -> None:
        await self.dp.feed_raw_update(self.bot, update)
        await self.bot.session.close()

    async def set_webhook(self):
        webhook_url = config('WEBHOOK_URL')
        # WEBHOOK_URL = адрес сайта/api/bot
        await self.bot.set_webhook(webhook_url)
        await self.bot.session.close()

tgbot = TGBot(router)
