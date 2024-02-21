import os
from discord import Intents, Client, Message, app_commands
from replit import db
import asyncio
import enum
from re import A
import typing
import discord 
import json
from discord.ext import commands
from references import cheat_database, stats, iv_dict, move_database
from test_classes import export_mon

def main():
#Discord Intent rules
  intents = discord.Intents.all()
  bot = commands.Bot(command_prefix="!",intents=intents)

#gives an intro message confirming it's on
  @bot.event
  async def on_ready():
    print('you in')
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s)")
    
#exporting a mons
  @bot.tree.command(name="export_mons")
  @app_commands.describe(need_mon="Choose a mons.. (ask for /list mons if you need one)")
  async def calc_export(interaction: discord.Interaction, need_mon: str):
    await interaction.response.defer(ephemeral = False)
    await asyncio.sleep(5)
    lst = export_mon(need_mon)
    await interaction.followup.send(f"`\n{lst[0]}\n{lst[1]}\n{lst[2]}\n{lst[3]}\n{lst[4]}\n{lst[5]}\n- {lst[6]}\n- {lst[7]}\n- {lst[8]}\n- {lst[9]}\n`")

#gives you a list of all the mons in the DB
  @bot.tree.command()
  async def list_mons(interaction: discord.Interaction):
    await interaction.response.send_message(f"All the keys: \n{db.keys()}",ephemeral = True)

  '''testing functiona;ity of button
  class InviteButtons(discord.ui.View):
    def __init__(self, inv: str):
        super().__init__()
        self.inv = inv
        self.add_item(discord.ui.Button(label="Invite link", url=self.inv))
    @discord.ui.button(label="Invite", style=discord.ButtonStyle.red)
    async def inviteBtn(self, interaction: discord.Interaction, button: discord.ui.Button):
      await interaction.response.send_message(self.inv)'''

# Cheat code bot
  @bot.tree.command(name="item_cheat")
  @app_commands.describe(code = "what code?")
  async def item_cheat(interaction: discord.Interaction, code: str):
    code = code.title()
    if code in cheat_database: 
      new_code = cheat_database[code]
      new_code = "82024022 " + new_code
    else:
      new_code = "no valid item/hm"
    await interaction.response.send_message(f"\n{code}:\n{new_code}")
    
#Move checker
  @bot.tree.command()
  @app_commands.describe(move = "what move?")
  async def moves(interaction: discord.Interaction, move: str):
    move = move.title()
    if move in move_database: 
      new_move = move_database[move]
    else:
      new_move = "no valid move name"
    await interaction.response.send_message(f"\n{move}:\n{new_move}")

#Deleting pokemon 
  #WORK IN PROGRESS
  @bot.command()
  async def invite(ctx: commands.Context):
    inv = await ctx.channel.create_invite()
    await ctx.send("Are you sure you want to delete? ", view=InviteButtons(str(inv)))

#Adding a mon using discord 
#No checks yet 
  #checking if better wy of adding ivs
  @bot.tree.command()
  @app_commands.describe(moves = "tackle, tackle, tackle, tackle", ev1 = "Currently only accepts two total. You'll have to adjust anything more than 3", iv = 'a a a b b b')
  async def add_mons(interaction: discord.Interaction, person: typing.Literal['sam','doug', 'cj'], poke: str, nick: str, lvl: str, nature: typing.Literal["Bashful", "Docile", "Hardy", "Quirky", "Serious", "Adamant", "Brave", "Lonely", "Naughty", "Bold", "Impish", "Lax", "Relaxed", "Modest", "Mild", "Quiet", "Rash", "Calm","Careful", "Gentle", "Sassy", "Hasty", "Jolly", "Naive", "Timid"], ev1: typing.Literal["Atk", "HP","Def","SpA","SpD","Spe"], ev2: typing.Literal["Atk", "HP","Def","SpA","SpD","Spe"], ability: str, iv: str, test_ivs: str, moves: str):
    moves = moves.title().split(', ')
    temp_iv = iv.split()
    ivs = []
    evs = []
    for i in temp_iv:
      if i in iv_dict:
        add = iv_dict[i]
        ivs.append(add)
    evs = evs.append(ev1)
    evs = evs.append(ev2)
    nick = nick.lower()
    dict_name = person + '_' + nick
    db[dict_name] = {"all_moves": 0, "poke": 0, "name": 0, "lv": 0, "ntr": 0, "stats": 0, "abil": 0, "ivs": 0}
    db[dict_name]["all_moves"] = moves
    db[dict_name]["poke"] = poke
    db[dict_name]["lv"] = lvl
    db[dict_name]["ntr"] = nature
    db[dict_name]["stats"] = evs
    db[dict_name]["abil"] = ability
    db[dict_name]["ivs"] = ivs
  #sends just what you added
    await interaction.response.defer(ephemeral = False)
    await asyncio.sleep(5)
    lst = export_mon(need_mon)
    await interaction.followup.send(f"`\n{lst[0]}\n{lst[1]}\n{lst[2]}\n{lst[3]}\n{lst[4]}\n{lst[5]}\n- {lst[6]}\n- {lst[7]}\n- {lst[8]}\n- {lst[9]}\n`")
  
main()
