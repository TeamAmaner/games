import discord
from discord.ext import commands

from pymongo import MongoClient

from lib.instant import Instant_Inside, Instant_NGword
from lib.insider import Insider

import setting

MONGO_URL = setting.MONGO


class Inside(commands.Cog):
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
        self.com_list = ["setup","add","delete","join","remove","list"]
        self.instant = Instant_NGword(bot)
        self.db = None


    async def setup(self):
        client = MongoClient(MONGO_URL)
        self.db = client.users.user_id
        return self.db


    @commands.command()
    async def ng(self,ctx,main,*sub):


        if main not in self.com_list:
            await ctx.send(f"{main}: 用語 '{main}' は、\
            コマンドレット、関数、スクリプト ファイル、\
            または操作可能なプログラムの名前として認識されません。\
            名前が正しく記述されていることを確認し、再試行してください。")
            return


        if main == "setup":
            await self.instant.make(ctx)
            await ctx.send("セットアップが完了しました")
            return

        if main == "add":
            db = self.db or await self.setup()

            data = db.find_one({"channel_id":ctx.channel.id})
            if not data:
                post = {"name":ctx.channel.name,"channel_id":ctx.channel.id,"words": [f"{sub[0]}"]}
                db.insert_one(post)
                await ctx.send(f"{ctx.channel.name} のNGワードに __**{sub[0]}**__ が追加されました")
                return
            db.update_one({"channel_id":ctx.channel.id}, {"$set": {"words": data["words"].append(sub[0])}})
            await ctx.send(f"{ctx.channel.name} のNGワードに __**{sub[0]}**__ が追加されました")
            return

        if main == "delete":
            db = self.db or await self.setup()

            data = db.find_one({"channel_id":ctx.channel.id})
            if not data:
                await ctx.send("このチャンネルのNGワードリストが存在しません。")
                return

            try:
                db.update_one({"channel_id":ctx.channel.id}, {"$set": {"words": data["words"].remove(sub[0])}})
            except ValueError:
                await ctx.send(f"NGワードlistの中に {sub[0]} は存在しません。")
                return

            await ctx.send(f"ワード {sub[0]} はリストから正常に削除されました。")
            return

        if main == "join":
            guild_roles = ctx.guild.roles
            role = discord.utils.get(guild_roles, name="NGword")
            await ctx.author.add_roles(role,reason="NGワードゲームへの参加")
            await ctx.send(f"{ctx.author.name} がNGワードゲームに参加しました。")
            return

        if main == "remove":
            guild_roles = ctx.guild.roles
            role = discord.utils.get(guild_roles, name="NGword")
            await ctx.author.remove_roles(role,reason="NGワードゲームからの脱退")
            await ctx.send(f"{ctx.author.name} がNGワードゲームから脱退しました。")
            return

        if main == "list":
            db = self.db or await self.setup()

            data = db.find_one({"channel_id":ctx.channel.id})
            if not data["words"]:
                await ctx.send("このチャンネルにNGはありません。")
                return
            txt = "```\n"
            for d in data["words"]:
                txt += f"{d}\n"
            txt += "```"
            await ctx.send(txt)
            return





def setup(bot):
    bot.add_cog(Insider(bot))
    bot.add_cog(NGword(bot))
