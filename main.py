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
from cheat import cheat_database

stats = ["Atk", "HP","Def","SpA","SpD","Spe"]
iv_dict = {  "s"	:	"30"	,
  "a+"	:	"28"	,
  "a"	:	"26"	,
  "a-"	:	"24"	,
  "b+"	:	"22"	,
  "b"	:	"20"	,
  "b-"	:	"18"	,
  "c+"	:	"16"	,
  "c"	:	"14"	,
  "c-"	:	"12"	,
  "d+"	:	"10"	,
  "d"	:	"8"	,
  "d-"	:	"6"	,
  "e+"	:	"4"	,
  "e"	:	"2"	,
  "e-"	:	"0"	
}

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
    
  @bot.tree.command()
  @app_commands.describe(text_to_send="Simon Says this...")
  #^This gives text above as you are inputting data 
  @app_commands.rename(text_to_send="message")
  async def test_command(interaction: discord.Interaction, text_to_send : str):
    await interaction.response.send_message(f"{text_to_send}")
    
#test of telling what the discord bot to say  
  @bot.tree.command(name="code")
  @app_commands.describe(code = "what code?")
  async def cheat(interaction: discord.Interaction, code: str):
    if code in cheat_database: 
      new_code = cheat_database[code]
      
    else:
      new_code = "no valid item/hm"
    await interaction.response.send_message(f"82024022 {new_code}")

#Adding a mon using discord 
#No checks yet 
  @bot.tree.command()
  @app_commands.describe(moves = "tackle, tackle, tackle, tackle", evs = "HP Atk Def SpA SpD Spe", iv = 'a a a b b b')
  async def add_mons(interaction: discord.Interaction, person: typing.Literal['sam','doug', 'cj'], poke: str, nick: str, lvl: str, nature: str, evs: str, ability: str, iv: str, moves: str):
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
