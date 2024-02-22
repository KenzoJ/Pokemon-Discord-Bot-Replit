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
  @bot.command()
  async def members(ctx):
      all_items = battle_items.keys()
      members = [str(m) for m in all_items]
      per_page = 10 # 10 members per page
      pages = math.ceil(len(members) / per_page)
      cur_page = 1
      chunk = members[:per_page]
      linebreak = "\n"
      message = await ctx.send(f"Page {cur_page}/{pages}:\n{linebreak.join(chunk)}")
      await message.add_reaction("◀️")
      await message.add_reaction("▶️")
      active = True

      def check(reaction, user):
          return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
                       # or you can use unicodes, respectively: "\u25c0" or "\u25b6"

      while active:
          try:
              reaction, user = await bot.wait_for("reaction_add", timeout=60, check=check)

              if str(reaction.emoji) == "▶️" and cur_page != pages:
                  cur_page += 1
                  if cur_page != pages:
                      chunk = members[(cur_page-1)*per_page:cur_page*per_page]
                  else:
                      chunk = members[(cur_page-1)*per_page:]
                  await message.edit(content=f"Page {cur_page}/{pages}:\n{linebreak.join(chunk)}")
                  await message.remove_reaction(reaction, user)

              elif str(reaction.emoji) == "◀️" and cur_page > 1:
                  cur_page -= 1
                  chunk = members[(cur_page-1)*per_page:cur_page*per_page]
                  await message.edit(content=f"Page {cur_page}/{pages}:\n{linebreak.join(chunk)}")
                  await message.remove_reaction(reaction, user)
          except asyncio.TimeoutError:
              await message.delete()
              active = False

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