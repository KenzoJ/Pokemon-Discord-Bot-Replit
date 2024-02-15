#Trying to figure out how to add multiple mons

import requests
from replit import db
import sys

def add_mon():
  #dictionaries for reference
  dict = {}
  new_mon = {}
  ni = "Magi 555"
  person = "CJ2"
  temp_moves = "tackle"
  poke = "Magikarp"
  lvl = "60"
  temp_stats = "42"
  add_nat = "bold"
  get_ability = "Flash Fire"
  temp_iv = "2"


 # new_mon[ni] = {"all_moves": 0, "poke": 0, "lv": 0, "ntr": 0, "stats": 0, "abil": 0, "ivs": 0}
# DB   CJ      Nickname:   value:        key         
  CJ = []
  Doug = []
  db["poke"] = [CJ, Doug]
  new_mon = {"ni1": {"all_moves": temp_moves, "poke": poke}} 
  new_mon_2 = {"ni2": {"all_moves": temp_moves, "poke": poke}} 
  db["poke"][0].append(new_mon)
  db["poke"][0].append(new_mon_2)
  
  
  print(db["poke"][0].items())

add_mon()