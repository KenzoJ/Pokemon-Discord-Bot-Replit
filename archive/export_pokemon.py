#This asks who is looking for the pokemon, then the pokemon name, then the 
from replit import db
import json


def main():
  x = input("add mon? calc? del mon?")
  while True: 
    if x == "add mon":
      add_mon()
      break
    if x == "calc":
      calc()
      break
    if x == "del mon":
      del_mon()
      break


def add_mon():
  while True:
    dict_name = input("For CJ, Doug, or Sam?")
    if dict_name == "CJ" or dict_name == "Doug" or dict_name == "Sam":
      break
    else:


  ni = input("Nickname?")
  while True:
    poke_lvl = input("Pokemon and level. ex.'mon' '##' \n")
    poke_lvl = poke_lvl.split()
    if len(poke_lvl) == 2:
      break

  #Nature loop
  while True:
    add_nat = input("Nature?")
    if add_nat in all_natures:
      break

  #stat checker
  flag = 1
  while flag: 
    temp_stats = []
    add_stats = input("How was it trained? ex. HP Def" "(Can only take two inputs for now)\n")
    add_stats = add_stats.split()
    flag = 0

    for x in add_stats:
      if x not in stats:
        flag = 1
  temp_stats.append(add_stats)

#Ability checker
  while True:
    get_ability = input("Ability?\n")
    with open("list_of_abilities.txt") as file:
      contents = file.read()
      if get_ability in contents:
        break
      elif get_ability == "not in list":
        break
  temp_moves = []
  #Move checker
  while True:
    if len(temp_moves) == 4:
      break
    add_moves = input("Moves learned?\n")
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
      print(add_ivs)
      for i in add_ivs:
        if i in iv_dict:
          i = iv_dict[i]
          temp_iv.append(i)
  #dictionary adder
  new_mon = {ni: {"all_moves": 0, "poke": 0, "name": 0, "lv": 0, "ntr": 0, "stats": 0, "abil": 0, "ivs": 0}
  }
  new_mon[ni]["all_moves"] = temp_moves
  new_mon[ni]["poke"] = poke_lvl[0]
  new_mon[ni]["lv"] = poke_lvl[1]
  new_mon[ni]["ntr"] = add_nat
  new_mon[ni]["stats"] = temp_stats
  new_mon[ni]["abil"] = get_ability
  new_mon[ni]["ivs"] = temp_iv
  db[dict_name] = new_mon
  db[dict_name].
  print("Successfully added!")

if __name__ == "__main__":
  export_mon()

'''
Adding the functionality of 3 ways it's trained
for x in test_vari:
  print(x)
'''
