import discord
from discord.ext import commands

from pymongo import MongoClient

import setting

MONGO_URL = setting.MONGO

class Check_NGword(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.log = bot.logging
        self.system = bot.system
        self.db = None


    async def setup(self):
        client = MongoClient(MONGO_URL)
        self.db = client.users.user_id
        return self.db


    @commands.Cog.listener()
    async def on_message(self, message):

        mem_roles = message.author.roles
        guild_roles = message.guild.roles
        role = discord.utils.get(guild_roles, name="NGword")

        if role not in mem_roles:
            return

        db = self.db or await self.setup()
        data = db.find_one({"channel_id":message.channel.id})
        if not data:
            return
        if not data["words"]:
            return
        bad_word = data["words"]
        for bw in bad_word:
            if bw in message.content:
                await message.reply(f"NGワードを確認\nNGワード：{bw}")
        return



def setup(bot):
    bot.add_cog(Check_NGword(bot))
