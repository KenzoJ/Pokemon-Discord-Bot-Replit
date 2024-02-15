import re
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
  person = "CJ"
  #nickname
  ni = "Magi4"
  dict_name = person + '_' + ni
  print(dict_name)
  #level
  lvl = "50"
  #poke
  poke = "Magikarp"
  #Nature
  nature = "Bold"
  #EV training
  evs = ["HP", "Spe"]
  #Ability checker
  ability = "Bold"
  #moves
  moves = ["Tackle","Tackle","Tackle","Tackle"]
  
  #IV Input
  iv = ["3","4","2","1","5","7"]

  db[dict_name] = {"all_moves": 0, "poke": 0, "name": 0, "lv": 0, "ntr": 0, "stats": 0, "abil": 0, "ivs": 0}
  
  db[dict_name]["all_moves"] = moves
  db[dict_name]["poke"] = poke
  db[dict_name]["lv"] = lvl
  db[dict_name]["ntr"] = nature
  db[dict_name]["stats"] = evs
  db[dict_name]["abil"] = ability
  db[dict_name]["ivs"] = iv
  print("Successfully added!")
  print(json.loads(db.get_raw(dict_name)))
  keys = db.keys()
  for i in keys:
      print(i,":",json.loads(db.get_raw(i)))
      

 
'''
  =for later
        x = []
        y = []
        x = json.loads(db.get_raw(dict_name)).get(ni).get("stats")[0:]
        y = json.loads(db.get_raw(dict_name)).get(ni).get("ivs")

        test_vari = []
        test_vari.append(db[dict_name][ni]["poke"])
        level = f'Level: {db[dict_name][ni]["lv"]}'
        test_vari.append(level)
        test_vari.append(f'{db[dict_name][ni]["ntr"]} Nature')
        test_vari.append(f'Ability: {db[dict_name][ni]["abil"]}')
        test_vari.append(f'EVs: 252 {x[0]} / 252 {x[1]}')
        test_vari.append(f'IVs: {y[0]} HP / {y[1]} Atk / {y[2]} Def / {y[3]} SpA / {y[4]} SpD / {y[5]} Spe')
        for i in db[dict_name][ni]["all_moves"]:
          test_vari.append(f"-{i}")
        for z in test_vari:
          print(z)

def del_mon():
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
  try:
    person = input("For whom?\n")
    for i in db[person].keys():
      print(i)
    delete_mon = input("\nWhich mon\n")
    if delete_mon in db[person].keys():
      del db[person][delete_mon]
      print("It's gone")
      sys.exit()
  except KeyError:
    sys.exit()
    "try again"
 #dictionary test
      with open(f"CJ.txt", "w") as file:
        file.write(f"\n\nStart\n{ni}\n{poke}\nLevel: {lvl}\n{nature} Nature\nAbility: {ability}\nEVs: {evs[0]} / {evs[1]}\nIVs: {iv[0]} HP / {iv[1]} Atk / {iv[2]} Def/ {iv[3]} SpA / {iv[4]} SpD / {iv[5]} Spe\n- {moves[0]}\n- {moves[1]}\n- {moves[2]}\n- {moves[3]}\nEnd\n")


'''
if __name__ == "__main__":
    add_mon() 