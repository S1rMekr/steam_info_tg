from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram import Bot, Router, F

from steam_utils import get_game_list

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Hello!")

@router.message()
async def echo(message: Message):
    game_list = await get_game_list(76561198053863572)
    for game in game_list:
        await message.answer_photo(
            photo=f"https://cdn.cloudflare.steamstatic.com/steam/apps/{game['appid']}/header.jpg",
            caption=f"Игра: {game['name']}\nСыграно за последние 2 недели: {round(game['playtime_2weeks']/60, 2)} часов\nСыграно всего: {round(game['playtime_forever']/60,2)} часов"
        )
