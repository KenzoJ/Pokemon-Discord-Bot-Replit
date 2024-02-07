import os
from discord import Intents, Client, Message
from replit import db
from responses import check_response

#Discord Intent rules
intents: Intents = Intents.default()
intents.message_content = True #NOQA
client: Client = Client(intents=intents)

#gives an intro message confirming it's on
@client.event
async def on_ready():
  print('you in')

# prevents duplicate loops
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  check_response(message.content)
#  message.channel.send(get_response(message.content)) 
  except ValueError:
    print("Error")
 
client.run(os.environ['SECRET_BOT_KEY'])
