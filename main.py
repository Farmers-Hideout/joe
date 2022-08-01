#Import
import discord
import asyncio
import json
import os
import asyncio
import asyncpg

#From Imports
from discord.ext import commands
from dotenv import load_dotenv

#Opening and loading config json variables with function for soft coding optimalization ;)
def readJson(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data
def writeJson(file_path, new_data):
    with open(file_path, "w") as f:
        data = json.dump(new_data,f)
    return data

#Defining
config_variables = readJson("lib/json/config.json")
debug_guild = config_variables['debug_guild']
cogs = config_variables['cogs']

#Defining hidden .env with secret variables like token through .env
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

TOKEN = os.environ.get("TOKEN")
HOST = os.environ.get("HOST")
DB_PW = os.environ.get("DB_PW")

#Intents
intents = discord.Intents.all()
intents.members = True
intents.guilds = True
intents.messages = True

#Initializing a database pool into a bot class variable
async def create_db_pool():
    bot.db = await asyncpg.create_pool(database="joe", user="einar", host=HOST, password=DB_PW)

#Defines the bot
bot = commands.Bot(description='Farmer Joe', help_command=None, intents=intents,debug_guild=debug_guild,auto_sync_commands=True)

for f in cogs:
    try:
        bot.load_extension(f'lib.cogs.{f}')
        print(f'Loaded {f} cog')
    except Exception as e:
        print(e)
        bot.load_extension(f'lib.cogs.{f}')
        print(f'Loaded {f} cog')


#Run Loops etc
async def main():
    print("main")
if __name__ == "__main__":
    db_loop = asyncio.get_event_loop()
    db_loop.run_until_complete(create_db_pool())
    asyncio.run(main())
    bot.run(TOKEN)
