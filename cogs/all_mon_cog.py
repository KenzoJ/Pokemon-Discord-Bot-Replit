import discord
from discord.ext import commands
from discord import app_commands

class all_mon_cog(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client

#3: gives you a list of all the mons in the DB
    @app_commands.command(name="List_all_mons")
    async def list_mons(self, interaction: discord.Interaction):
      await interaction.response.send_message(f"All the keys: \n{db.keys()}",ephemeral = True)

async def setup(client:commands.Bot) -> None:
  await client.add_cog(all_mon_cog(client))