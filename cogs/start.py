import discord
from discord.ext import commands

from pymongo import MongoClient

from lib.instant import Instant_Inside, Instant_NGword
from lib.insider import Insider

import setting

MONGO_URL = setting.MONGO


class Insider(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.system = bot.system
        self.instant = Instant_Inside(bot)
        self.insider = Insider(bot)



    @commands.command()
    async def inside(self,ctx):

        # if ctx.author != self.bot.get_user(653785595075887104):
        #     await ctx.send("あなたには使用する権限がありません。 \nYou don't have the privilege to use this.")
        #     return

        print("start")
        self.system.insider.__init__()

        channels = ctx.guild.voice_channels
        voice_channel = discord.utils.get(channels, name="テストチャンネル")

        await ctx.send("チャンネルを作成します")
        await self.instant.make(ctx)

        self.system.insider.player.all = voice_channel.members
        await ctx.send(self.bot.system.insider.player.all)
        if not self.system.insider.player.all:
            await ctx.send("no one")
            # return
        # if len(self.players) <= 5:
        #     await ctx.send("参加を希望したのが3名以下だったため、開始できません。\n停止します...")
        #     return
        # txt = "参加者一覧\n```\n"
        # for user in self.players:
        #     txt += f"・{user.name}\n"
        # await ctx.send(f"{txt}```")
        self.system.insider.guild = ctx.guild
        await self.insider.start(ctx)




class NGword(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.system = bot.system
        self.com_list = ["add","setup"]
        self.instant = Instant_NGword(bot)


    async def setup(self) -> asyncpg.Connection:
        client = MongoClient(MONGO_URL)
        self.db = client.users.user_id
        return self.db


    @commands.command()
    async def ng(self,ctx,main,sub*):


        if main not in self.com_list:
            return await ctx.send(f"{main}: 用語 '{main}' は、\
            コマンドレット、関数、スクリプト ファイル、\
            または操作可能なプログラムの名前として認識されません。\
            名前が正しく記述されていることを確認し、再試行してください。")

        if main == "add":
            db = self.db or await self.setup()

            data = db.find_one({"channel_id":ctx.channel.id})
            if not data:
                post = {"name":ctx.channel.name,"channel_id":ctx.channel.id,"words": []}
                db.insert_one(post)


            db.update_one({"channel_id":ctx.channel.id}, {"$set": {"words": data["words"].append(sub[1])}})
            await ctx.send(f"{ctx.channel.name} のNGワードに __**{sub[1]}**__ が追加されました")
            return

        if main == "setup":
            await self.instant.make(ctx)
            await ctx.send("セットアップが完了しました")







def setup(bot):
    bot.add_cog(Insider(bot))
    bot.add_cog(NGword(bot))
