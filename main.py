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
  @bot.tree.command()
  @app_commands.describe(mon="Choose a mons.. (ask for /list mons if you need one)")
  async def export_mon(interaction: discord.Interaction, mon: str):
    #await interaction.response.send_message
    await interaction.response.defer(ephemeral = False)
    await asyncio.sleep(5)
    lst = []
    dict_name = mon
    x = []
    y = []
    x = json.loads(db.get_raw(dict_name)).get("stats")[0:]
    y = json.loads(db.get_raw(dict_name)).get("ivs")
    test_vari = []
    test_vari.append(db[dict_name]["poke"])
    level = f'Level: {db[dict_name]["lv"]}'
    test_vari.append(level)
    test_vari.append(f'{db[dict_name]["ntr"]} Nature')
    test_vari.append(f'Ability: {db[dict_name]["abil"]}')
    test_vari.append(f'EVs: 252 {x[0]} / 252 {x[1]}')
    test_vari.append(f'IVs: {y[0]} HP / {y[1]} Atk / {y[2]} Def / {y[3]} SpA / {y[4]} SpD / {y[5]} Spe')
    for i in db[dict_name]["all_moves"]:
      test_vari.append(f"{i}")
    
    lst = test_vari
    await interaction.followup.send(f"`\n{lst[0]}\n{lst[1]}\n{lst[2]}\n{lst[3]}\n{lst[4]}\n{lst[5]}\n- {lst[6]}\n- {lst[7]}\n- {lst[8]}\n- {lst[9]}\n`")

#gives you a list of all the mons in the DB
  @bot.tree.command()
  async def list_mons(interaction: discord.Interaction):
    await interaction.response.send_message(f"All the keys: \n{db.keys()}",ephemeral = True)

    
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
#Adding a mon using discord 
#No checks yet 
  @bot.tree.command()
  @app_commands.describe(moves = "tackle, tackle, tackle, tackle", evs = "HP Atk Def SpA SpD Spe", iv = 'a a a b b b')
  async def add_mons(interaction: discord.Interaction, person: typing.Literal['sam','doug', 'cj'], poke: str, nick: str, lvl: str, nature: typing.Literal["Bashful", "Docile", "Hardy", "Quirky", "Serious", "Adamant", "Brave", "Lonely", "Naughty", "Bold", "Impish", "Lax", "Relaxed", "Modest", "Mild", "Quiet", "Rash", "Calm","Careful", "Gentle", "Sassy", "Hasty", "Jolly", "Naive", "Timid"], evs: str, ability: str, iv: str, moves: str):
    moves = moves.title().split(', ')
    temp_iv = iv.split()
    ivs = []
    for i in temp_iv:
      if i in iv_dict:
        add = iv_dict[i]
        ivs.append(add)
    evs = evs.split()
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
    await interaction.response.defer(ephemeral = False)
    await asyncio.sleep(5)
    lst = [] 
    x = []
    y = []
    x = json.loads(db.get_raw(dict_name)).get("stats")[0:]
    y = json.loads(db.get_raw(dict_name)).get("ivs")
    test_vari = []
    test_vari.append(db[dict_name]["poke"])
    level = f'Level: {db[dict_name]["lv"]}'
    test_vari.append(level)
    test_vari.append(f'{db[dict_name]["ntr"]} Nature')
    test_vari.append(f'Ability: {db[dict_name]["abil"]}')
    test_vari.append(f'EVs: 252 {x[0]} / 252 {x[1]}')
    test_vari.append(f'IVs: {y[0]} HP / {y[1]} Atk / {y[2]} Def / {y[3]} SpA / {y[4]} SpD / {y[5]} Spe')
    for i in db[dict_name]["all_moves"]:
      test_vari.append(f"{i}")

    lst = test_vari
    await interaction.followup.send(f"`\n{lst[0]}\n{lst[1]}\n{lst[2]}\n{lst[3]}\n{lst[4]}\n{lst[5]}\n- {lst[6]}\n- {lst[7]}\n- {lst[8]}\n- {lst[9]}\n`")
  bot.run(os.environ['SECRET_BOT_KEY'])

  
def export_mon(person):
  dict_name = person
  x = []
  y = []
  x = json.loads(db.get_raw(dict_name)).get("stats")[0:]
  y = json.loads(db.get_raw(dict_name)).get("ivs")
  test_vari = []
  test_vari.append(db[dict_name]["poke"])
  level = f'Level: {db[dict_name]["lv"]}'
  test_vari.append(level)
  test_vari.append(f'{db[dict_name]["ntr"]} Nature')
  test_vari.append(f'Ability: {db[dict_name]["abil"]}')
  test_vari.append(f'EVs: 252 {x[0]} / 252 {x[1]}')
  test_vari.append(f'IVs: {y[0]} HP / {y[1]} Atk / {y[2]} Def / {y[3]} SpA / {y[4]} SpD / {y[5]} Spe')
  for i in db[dict_name]["all_moves"]:
    test_vari.append(f"-{i}")
  return test_vari

main()
