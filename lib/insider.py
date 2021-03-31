import discord
from discord.ext import commands


class Insider(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.system = bot.system


    async def start(self,ctx):
        await ctx.send("ゲームを開始します")
        await self.send()

    async def send(self):
        channels = self.bot.system.insider.channel
        await channels.team_a.send("Hand in Hand")
        await channels.team_b.send("グリーンライツ・セレナーデ")
