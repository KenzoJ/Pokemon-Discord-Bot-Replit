import os
from discord import Intents, Client, Message
from replit import db
from responses import get_response

import enum
from re import A
import typing
import settings
import discord 
from discord.ext import commands
from discord import app_commands

#Discord Intent rules
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!",intents=intents)

#gives an intro message confirming it's on
@bot.event
async def on_ready():
  bot.tree.copy_global_to(guild=settings.GUILDS_ID)
  await bot.tree.sync(guild=settings.GUILDS_ID)
  print('you in')

bot.run(os.environ['SECRET_BOT_KEY'])

GUILDS_ID = discord.Object(id=int(os.environ("GUILD")))
'''
older code:
@client.event
async def on_message(message):
  try:
    if message.author == client.user:
      return
    await message.channel.send(get_response(message.content)) 
  except ValueError:
    print("Error")



'''