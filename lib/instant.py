import discord
from discord.ext import commands

from typing import Any
from pymongo import MongoClient

import setting

MONGO_URL = setting.MONGO



class Instant_Inside():
    def __init__(self, bot: Any):
        self.bot = bot


    async def dele(self,ctx):
        all_role = ctx.guild.roles
        for rol in all_role:
            try:
                if rol.name == "Team A":
                    await rol.delete()
                if rol.name == "Team B":
                    await rol.delete()
            except:
                a = "a"

        channels = ctx.channel.category.text_channels
        channel = discord.utils.get(channels, name="Team A")
        await channel.delete()
        channel = discord.utils.get(channels, name="Team B")
        await channel.delete()


    async def make(self,ctx):
        all_role = ctx.guild.roles
        for rol in all_role:
            if rol.name == "Team A":
                await rol.delete()
            if rol.name == "Team B":
                await rol.delete()


        self.bot.system.insider.role.team_a = await ctx.guild.create_role(name="Team A")

        self.bot.system.insider.role.team_b = await ctx.guild.create_role(name="Team B")

        category = ctx.channel.category
        for chan in category.text_channels:
            if chan.name == "Team A":
                await chan.delete()
            if chan.name == "Team B":
                await chan.delete()

        self.bot.system.insider.channel.team_a = await category.create_text_channel("Team A")
        self.bot.system.insider.channel.team_b = await category.create_text_channel("Team B")


        await self.bot.system.insider.channel.team_a.set_permissions(ctx.author.guild.default_role, read_messages=False)
        await self.bot.system.insider.channel.team_a.set_permissions(ctx.author.guild.default_role, read_message_history=False)
        await self.bot.system.insider.channel.team_b.set_permissions(ctx.author.guild.default_role, read_messages=False)
        await self.bot.system.insider.channel.team_b.set_permissions(ctx.author.guild.default_role, read_message_history=False)

        await self.bot.system.insider.channel.team_a.set_permissions(self.bot.system.insider.role.team_a, read_messages=True)
        await self.bot.system.insider.channel.team_a.set_permissions(self.bot.system.insider.role.team_a, read_message_history=True)
        await self.bot.system.insider.channel.team_b.set_permissions(self.bot.system.insider.role.team_b, read_messages=True)
        await self.bot.system.insider.channel.team_b.set_permissions(self.bot.system.insider.role.team_b, read_message_history=True)


class Instant_NGword():
    def __init__(self,bot):
        self.bot = bot

    async def make(self,ctx):
        client = MongoClient(MONGO_URL)
        db = client.users
        db.drop_collection(db.user_id)
        guild_roles = ctx.guild.roles
        role = discord.utils.get(guild_roles, name="NGword")
        if not role:
            await ctx.guild.create_role(name="NGword")
