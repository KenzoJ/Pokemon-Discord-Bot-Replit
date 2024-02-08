import os
from discord import Intents, Client, Message, app_commands
from replit import db
from responses import get_response
import enum
from re import A
import typing
import discord 
from discord.ext import commands

def main():
  #Discord Intent rules
  intents = discord.Intents.all()
  bot = commands.Bot(command_prefix="!",intents=intents)
  
  #gives an intro message confirming it's on
  @bot.event
  async def on_ready():
    print('you in')
    try:
      synced = await bot.tree.sync()
      print(f"Synced {len(synced)} command(s)")
    except Exception as e:
      print(e)
      
  @bot.tree.command()
  @app_commands.describe(text_to_send="Simon Says this...")
  @app_commands.rename(text_to_send="message")
  async def test_command(interaction: discord.Interaction, text_to_send : str):
    await interaction.response.send_message(f"{text_to_send}", ephermeral=True)
  
  @bot.tree.command(name="say")
  @app_commands.describe(thing_to_say = "what should i say?")
  async def say(interaction: discord.Interaction, thing_to_say: str):
    await interaction.response.send_message(f"{interaction.user.name} said {thing_to_say}")

  @bot.tree.command()
  async def drink(interaction: discord.Interaction, choice: typing.Literal['beer','milk', 'tea']):
    await interaction.response.send_message(f"{choice}")

  @bot.tree.command()
  async def test_export_mon(interaction: discord.Interaction, choice: typing.Literal["CJ",'Doug','Sam']):
    await interaction.response.send_message(f"which mons? {db[na].keys()}")

  bot.run(os.environ['SECRET_BOT_KEY'])
  
def export_mon():
  temp_poke = []
  while True:
    na = input("For Whom?")
    if na == "CJ" or na == "Doug" or na == "Sam":
      break
  print("Current pokemon:")
  #Gives user options of which pokemon
  for i in db[na].keys():
    temp_poke.append(i)
    print(i)
  while True:
    poke = input("\nWhat pokemon do you need? (Enter nickname) \n")
    if poke in temp_poke:
      for x in calc_mon(na, poke):
        print(x)
      break

def calc_mon(na, poke):
  #Printing the calc format
  x = []
  y = []
  x = json.loads(db.get_raw(na)).get(poke).get("stats")[0]
  y = json.loads(db.get_raw(na)).get(poke).get("ivs")
  test_vari = []
  test_vari.append(db[na][poke]["poke"])
  level = f'Level: {db[na][poke]["lv"]}'
  test_vari.append(level)
  test_vari.append(f'{db[na][poke]["ntr"]} {"Nature"}')
  test_vari.append(f'Ability: {db[na][poke]["abil"]}')
  test_vari.append(f'EVs: 252 {x[0]} / 252 {x[1]}')
  test_vari.append(f'IVs: {y[0]} HP / {y[1]} Atk / {y[2]} Def / {y[3]} SpA / {y[4]} SpD / {y[5]} Spe')
  for i in db[na][poke]["all_moves"]:
    test_vari.append(f"-{i}")
  print(test_vari)
  return test_vari

main()
