#Import
import discord
import asyncio

#From Imports
from discord.ext import commands


#Intents
intents = discord.Intents.all()
intents.members = True
intents.guilds = True
intents.messages = True


bot = commands.Bot(description='Farmer Joe', help_command=None, intents=intents,debug_guild=936761578748002334,auto_sync_commands=True)
cogs = []
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
    asyncio.run(main())
    bot.run("TOKEN")
