import discord
from discord.ext import commands

class Check_NGword(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.db = bot.db
        self.log = bot.logging
        self.system = bot.system


    async def setup(self) -> asyncpg.Connection:
        client = MongoClient(MONGO_URL)
        self.db = client.users.user_id
        return self.db


    @commands.Cog.listener()
    async def on_message(self, message):

        member = message.guild.get_member(message.author.id)
        mem_roles = member.roles
        guild_roles = message.guild.roles
        role = discord.utils.get(guild_roles, name="NGword")

        if role not in mem_roles:
            return

        db = self.db or await self.setup()
        data = db.find_one({"channel_id":ctx.channel.id})
        bad_word = data["words"]



def setup(bot):
    bot.add_cog(Check_NGword(bot))
