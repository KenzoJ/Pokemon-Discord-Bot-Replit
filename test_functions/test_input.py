import requests
from replit import db

def input_checker():
  
  #dictionaries for reference
  dict = {}
  all_natures = [
    "Bashful", "Docile", "Hardy", "Quirky", "Serious", "Adamant", "Brave", "Lonely", "Naughty", "Bold", "Impish", "Lax", "Relaxed", "Modest", "Mild", "Quiet", "Rash", "Calm","Careful", "Gentle", "Sassy", "Hasty", "Jolly", "Naive", "Timid",
  ]
  stats = ["Atk", "HP","Def","SpA","SpD","Spe"]
  iv_dict = {
    "s"	:	"30"	,
    "a+"	:	"28"	,
    "a"	:	"26"	,
    "a-"	:	"24"	,
    "b+"	:	"22"	,
    "b"	:	"20"	,
    "b-"	:	"18"	,
    "c+"	:	"16"	,
    "c"	:	"14"	,
    "c-"	:	"12"	,
    "d+"	:	"10"	,
    "d"	:	"8"	,
    "d-"	:	"6"	,
    "e+"	:	"4"	,
    "e"	:	"2"	,
    "e-"	:	"0"	
  }
  
  #Nickname, poke, level?
  nick = input("Nickname?")
  poke_lvl = input("Pokemon and level?")
  poke_lvl = poke_lvl.split()
  
  #Nature loop
  while True:
    add_nat = input("Nature?")
    if add_nat in all_natures:
      break

  #stat checker
  flag = 1
  while flag: 
    temp_stats = []
    add_stats = input("How was it trained?")
    add_stats = add_stats.split()
    flag = 0

    for x in add_stats:
      if x not in stats:
        flag = 1
  temp_stats.append(add_stats)
  #Ability checker
  
  while True:
    get_ability = input("Ability?")
    with open("list_of_abilities.txt") as file:
      contents = file.read()
      if get_ability in contents:
        break
  
  #Move checker
  temp_moves = []
  while True:
    if len(temp_moves) == 4:
      break
    add_moves = input("\nMoves learned?\n")
    with open("list_of_moves.txt") as file:
      contents = file.read()
      if add_moves in contents:
        temp_moves.append(add_moves)
        continue
  #IV Input
  temp_iv = []
  while True:
    if len(temp_iv) == 6:
      break
    add_ivs = input("IVs?")
    add_ivs = add_ivs.split()
    if len(add_ivs) == 6:
      for i in add_ivs:
        if i in iv_dict:
          i = iv_dict[i]
          temp_iv.append(i)
      
  #dictionary adder   
  db["CJ"] = {"all_moves": 0, "poke": 0, "name": 0, "lv": 0, "ntr": 0, "stats": 0, "abil": 0, "ivs": 0
  }
  db["CJ"]["all_moves"] = temp_moves
  db["CJ"]["poke"] = poke_lvl[0]
  db["CJ"]["name"] = nick
  db["CJ"]["lv"] = poke_lvl[1]
  db["CJ"]["ntr"] = add_nat
  db["CJ"]["stats"] = temp_stats
  db["CJ"]["abil"] = get_ability
  db["CJ"]["ivs"] = temp_iv
  for i in db["CJ"].items():
    print(i)
  
'''
To do:
- Redefining 

'''