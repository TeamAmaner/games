import discord
from discord.ext import commands

from lib.instant import Instant_Inside
from lib.insider import Insider


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.system = bot.system
        self.instant = Instant_Inside(bot)
        self.insider = Insider(bot)


    @commands.command()
    async def hello(self,ctx):
        await ctx.send("hello")


    @commands.command()
    async def team_a(self,ctx):

        # if ctx.author != self.bot.get_user(653785595075887104):
        #     await ctx.send("あなたには使用する権限がありません。 \nYou don't have the privilege to use this.")
        #     return

        await ctx.author.add_roles(self.bot.system.insider.role.team_a)



    @commands.command()
    async def team_b(self,ctx):

        # if ctx.author != self.bot.get_user(653785595075887104):
        #     await ctx.send("あなたには使用する権限がありません。 \nYou don't have the privilege to use this.")
        #     return

        await ctx.author.add_roles(self.bot.system.insider.role.team_b)


    @commands.command()
    async def open(self,ctx):

        chan = self.bot.system.insider.channel.team_a
        await chan.set_permissions(ctx.author.guild.default_role, read_messages=True)

        chan = self.bot.system.insider.channel.team_b
        await chan.set_permissions(ctx.author.guild.default_role, read_messages=True)


    @commands.command()
    async def open(self,ctx):

        chan = self.bot.system.insider.channel.team_a
        await chan.set_permissions(ctx.author.guild.default_role, read_messages=False)

        chan = self.bot.system.insider.channel.team_b
        await chan.set_permissions(ctx.author.guild.default_role, read_messages=False)












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
