import asyncio
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
#from tgbot.handlers import router
#token="Your token was replaced with a new one. You can use this token to access HTTP API:
token ='7600730617:AAFsVcwR2GI23MnsturSya50ajaF1IT7lb4'
webhook_url = 'https://simple-tg-bot-aiogram.vercel.app'
router = Router()
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer('/start')
class TGBot:
    def __init__(self, router: Router) -> None:
       #token = config('TOKEN')
       self.bot = Bot(token)
       self.dp = Dispatcher()
       self.dp.include_router(router)
       

    async def update_bot(self, update: dict) -> None:
        await self.dp.feed_raw_update(self.bot, update)
        await self.bot.session.close()

    async def set_webhook(self):
        #webhook_url = config('WEBHOOK_U
        # WEBHOOK_URL = адрес сайта/api/bot
        await self.bot.set_webhook(webhook_url)
        await self.bot.session.close()

tgbot = TGBot(router)
