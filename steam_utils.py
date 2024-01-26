import json

from steam import Steam

from config import Config, load_config

config:Config = load_config()

steam = Steam(config.tg_bot.steam_token)

async def get_game_list(steam_id):
    game_list = steam.users.get_user_recently_played_games(steam_id)["games"]
    return game_list

