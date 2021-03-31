import discord
from discord.ext import commands

from lib.instant import Instant
from lib.insider import Insider


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.system = bot.system
        self.instant = Instant(bot)
        self.insider = Insider(bot)


    @commands.command()
    async def hello(self,ctx):
        await ctx.send("hello")

    @commands.command()
    async def inside(self,ctx):

        if ctx.author != self.bot.get_user(653785595075887104):
            await ctx.send("あなたには使用する権限がありません。 \nYou don't have the privilege to use this.")
            return

        print("start")
        self.system.inside.__init__()

        channels = ctx.guild.voice_channels
        voice_channel = discord.utils.get(channels, name="テストチャンネル")

        await ctx.send("チャンネルを作成します")
        await self.instant.make(ctx)

        self.system.insider.player.all = voice_channel.members
        await ctx.send(self.bot.system.player.all)
        if not self.system.insider.player.all:
            await ctx.send("no one")
            return
        # if len(self.players) <= 5:
        #     await ctx.send("参加を希望したのが3名以下だったため、開始できません。\n停止します...")
        #     return
        # txt = "参加者一覧\n```\n"
        # for user in self.players:
        #     txt += f"・{user.name}\n"
        # await ctx.send(f"{txt}```")
        self.system.insider.guild = ctx.guild
        await self.insider.start(ctx)


    @commands.command()
    async def rename(self,ctx,name):

        if ctx.author != self.bot.get_user(653785595075887104):
            await ctx.send("あなたには使用する権限がありません。 \nYou don't have the privilege to use this.")
            return

        channel = ctx.author.voice.channel
        await channel.edit(name=name,reason="ゲームの実験に使いたかった")
        await ctx.send("完了")









def setup(bot):
    bot.add_cog(Admin(bot))
