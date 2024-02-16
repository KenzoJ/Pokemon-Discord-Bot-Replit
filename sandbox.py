#THIS IS A SANDBOX FOR TESTING. FEEL FREE TO DELETE.
from references import cheat_database

'''
@bot.tree.command(name="code")
@app_commands.describe(code = "what code?")
async def cheat(interaction: discord.Interaction, code: str):
'''
code = input("item?")
if code in cheat_database: 
  new_code = cheat_database[code]
  print(f"82024022 {new_code}")
else:
  new_code = "no valid item/hm"
  print(new_code)


'''
below might be useful for later
@bot.tree.command()
@app_commands.describe(text_to_send="Simon Says this...")
 @app_commands.rename(text_to_send="message")  async def test_command(interaction: discord.Interaction, text_to_send : str):
  await interaction.response.send_message(f"{text_to_send}")
'''