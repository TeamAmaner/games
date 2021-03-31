# start.py

import discord
from discord.ext import commands

from typing import Any



class Instant():
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



    async def add(self):
        channel = discord.utils.get(self.bot.system.guild.text_channels, name='人狼')
        category = channel.category
        for p in self.bot.system.player.all:
            role = p.role
            if role == "人狼":
                continue

            chan = discord.utils.get(self.bot.system.guild.text_channels, name=role)
            if not chan:
                chan = await category.create_text_channel(role)
            await chan.set_permissions(self.bot.system.guild.roles[0],read_messages=False)
            await chan.set_permissions(self.bot.system.role.killed,read_messages=True)
            await chan.set_permissions(self.bot.system.role.no,read_messages=True)
