import os
from discord import Intents, Client, Message

#Discord Intent rules
intents: Intents = Intents.default()
intents.message_content = True #NOQA
client: Client = Client(intents=intents)

@client.event
async def test_multiple(input):
  await message.channel.send(input) 
