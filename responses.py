from replit import db
from cheat import moves

def get_response(user_input):
  response: str = user_input.lower()
  if response == "help":
    return "You can:\n -add mons\n -calc\n -del mon\n -erase all\n"
  if response.startswith("cheat"):
    response = response.split()
    response = " ".join(response[1:])
    code = moves(response)
    return code
  else:
    return "no valid input"
'''
from test_input import input_checker
from test_dict import calc_export
from replit import db
import sys

def main():
  x = input("Task? (
  if x == "add mon":
    add_mon()
  if x == "calc":
    calc_export()
  if x == "erase all":
    if "Sam" in db.keys():
      del db["Sam"]
    if "Doug" in db.keys():
      del db["Doug"]
    if "CJ" in db.keys():
      del db["CJ"]
    else:
      print("Bitch empty")
      sys.exit
      
  if x == "del mon":
    while True:
      try:
        person = input("For whom?\n")
        for i in db[person].keys():
          print(i)
        delete_mon = input("\nWhich mon\n")
        if delete_mon in db[person].keys():
          del db[person][delete_mon]
          print("It's gone")
          break
      except KeyError:
        continue
        "try again"
   '''