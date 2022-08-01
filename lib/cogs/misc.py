#Import
import time
import asyncio

#From imports
from discord.ext import commands
from discord.ui import Button, View
from discord import SlashCommandGroup, permission
from discord.commands.core import slash_command
from discord.commands import Option

class misc(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @slash_command
    async def help(self, ctx):
        ctx.respond("I ain't helping you for a damn thing")

    @slash_command
    async def changelog(self, ctx):
        response = ctx.respond("Give me a second")
        asyncio.sleep(2)
        response = await ctx.interaction.original_message()
        await response.edit("Seems like I'm too lazy")
        
    @slash_command
    async def credits(self, ctx):
        ctx.respond("It's open source!... *though the main contributor is byggmesterPRO#8206*")

    @slash_command
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        content = f"The current bot latency is `{latency}`ms"
        start = time.time()
        message = await ctx.respond(content)
        message = await ctx.interaction.original_message()
        end = time.time()
        await message.edit(content=(content + f" | Response time: {(end-start)*1000:,.0f}" ))

    @slash_command
    async def invite(self, ctx):
        ctx.respond("https://discord.gg/64f9MtV8Ws")

def setup(bot):
    bot.add_cog(misc(bot))