import discord
from discord.ext import commands




class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.system = bot.system


    @commands.command()
    async def hello(self,ctx):
        await ctx.send("hello")

    @commands.command()
    async def inside(self,ctx):
        print("start")
        self.system.inside.__init__()

        channels = ctx.guild.voice_channels
        voice_channel = discord.utils.get(channels, name="テストチャンネル")

        channels = ctx.channel.category.text_channels
        a_channel = discord.utils.get(channels, name="Team A")
        b_channel = discord.utils.get(channels, name="Team B")
        if not a_channel or not b_channel:
            await ctx.send("チャンネルを作成します")
            await self.instant.make(ctx)
        self.players = await self.controll.count(ctx,n)
        await ctx.send(self.bot.system.player.all)
        if not self.bot.system.player.all:
            await ctx.send("no one")
            return
        # if len(self.players) <= 3:
        #     await ctx.send("参加を希望したのが3名以下だったため、開始できません。\n停止します...")
        #     return
        # txt = "参加者一覧\n```\n"
        # for user in self.players:
        #     txt += f"・{user.name}\n"
        # await ctx.send(f"{txt}```")
        self.bot.system.guild = ctx.guild
        await self.starting.deploy(ctx)


    @commands.command()
    async def rename(self,ctx,name):
        channel = ctx.author.voice.channel
        await channel.edit(name="テストチャンネル",reason="ゲームの実験に使いたかった")
        await ctx.send("完了")









def setup(bot):
    bot.add_cog(Admin(bot))
