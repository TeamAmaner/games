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
        await channel.category.delete()
        channel = discord.utils.get(channels, name="Team B")
        await channel.category.delete()

    async def make(self,ctx):
        all_role = ctx.guild.roles
        for rol in all_role:
            if rol.name == "Team A":
                self.bot.system.insider.role.team_a = discord.utils.get(all_role, name="Team A")
            if rol.name == "Team B":
                self.bot.system.insider.role.team_b = discord.utils.get(all_role, name="Team B")


        if not self.bot.system.insider.role.team_a:
            self.bot.system.insider.role.team_a = await ctx.guild.create_role(name="Team A")

        if not self.bot.system.insider.role.team_b:
            self.bot.system.insider.role.team_b = await ctx.guild.create_role(name="Team B")

        category = ctx.channel.category
        chan = await category.create_text_channel("Team A")
        await chan.set_permissions(ctx.author.guild.default_role, read_message_history=False)
        await chan.set_permissions(ctx.author.guild.default_role, read_messages=False)
        await chan.set_permissions(self.bot.system.insider.role.team_a, read_messages=True)
        chan = await category.create_text_channel("Team B")
        await chan.set_permissions(ctx.author.guild.default_role, read_message_history=False)
        await chan.set_permissions(ctx.author.guild.default_role, read_messages=False)
        await chan.set_permissions(self.bot.system.insider.role.team_a, read_messages=True)

        category = await ctx.guild.create_category(name="生存者")
        chan = await category.create_text_channel("会議所")
        await chan.set_permissions(ctx.guild.roles[0],read_messages=False)
        await chan.set_permissions(self.bot.system.role.on,read_messages=True)
        voice = await category.create_voice_channel("会議所")
        await voice.edit(user_limit=50)
        await voice.set_permissions(ctx.guild.roles[0],connect=False,speak=False)

        category = await ctx.guild.create_category(name="役職")
        chan = await category.create_text_channel("人狼")
        await chan.set_permissions(ctx.guild.roles[0],read_messages=False)
        await chan.set_permissions(self.bot.system.role.killed,read_messages=True)
        await chan.set_permissions(self.bot.system.role.no,read_messages=True)

        category = await ctx.guild.create_category(name="死亡者")
        chan = await category.create_text_channel("反省会")
        await chan.set_permissions(ctx.guild.roles[0],read_messages=False)
        await chan.set_permissions(self.bot.system.role.killed,read_messages=True)
        voice = await category.create_voice_channel("反省会")
        await voice.edit(user_limit=50)
        await voice.set_permissions(ctx.guild.roles[0],connect=False)

        category = await ctx.guild.create_category(name="不参加者")
        chan = await category.create_text_channel("観戦")
        await chan.set_permissions(ctx.guild.roles[0],read_messages=False)
        await chan.set_permissions(self.bot.system.role.no,read_messages=True)
        voice = await category.create_voice_channel("観戦中")
        await voice.edit(user_limit=99)
        await voice.set_permissions(ctx.guild.roles[0],connect=False)



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
