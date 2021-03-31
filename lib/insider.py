import discord
from discord.ext import commands


class Insider(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.system = bot.system


    async def start(self,ctx):
        await ctx.send("ゲームを開始します")
        await self.send()
