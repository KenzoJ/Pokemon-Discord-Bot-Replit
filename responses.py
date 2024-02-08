from replit import db
from cheat import moves
from poke_tracker.add_pokemon import add_mon
from poke_tracker.export_pokemon import export_mon
from test_multiple import test_multiple
import sys

def get_response(user_input):
  response: str = user_input.lower()
  if response == "help":
    return "You can:\n -add mons\n -export\n -del mon\n -erase all\n"
  if response.startswith("cheat"):
    response = response.split()
    response = " ".join(response[1:])
    code = moves(response)
    return code
  if response == "add mon":
    add_mon()
  if response == "export":
    export_mon()
  if response == "test":
    x = test_multiple(response)
    return x
  else:
    return "no valid input"
