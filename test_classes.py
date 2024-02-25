import json
from replit import db

def export_mon(dict_name):
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
  return test_vari
  



'''  #testing page functionality
  

'''

'''#Deleting pokemon 
  #WORK IN PROGRESS
  @bot.tree.command(name="delete_mon")
  async def delete(interaction: discord.Interaction, code: str):
    hello()
    #button = MyButton(label="Are you sure?")
    #view = View() 
    #view.add_item(button)
    #await interaction.send("Done", view=view)    

  class MyButton(Button):
    async def callback(self, interaction):
      await interaction.response.send_message("Hi!")

  @bot.command()
  async def hello(ctx):
    button = MyButton(label="Are you sure?")
    view = View() 
    view.add_item(button)
    await ctx.send("Done", view=view)'''


''' #testing exporting all items 
  #Then move to slash groups
  @bot.tree.command(description = "export all items")
  async def all_items(interaction: discord.Interaction):
    temp_keys = battle_items.keys()
    print(temp_keys)
    #temp_list = []
    #temp_list = battle_items.keys()
    await interaction.response.send_message(f"test",ephemeral = True)
'''