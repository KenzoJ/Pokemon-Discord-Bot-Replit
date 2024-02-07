#This asks who is looking for the pokemon, then the pokemon name, then the 
from replit import db
import json

def export_mon():
  while True:
    na = input("For whom?")
    if na == "CJ" or na == "Doug" or na == "Sam":
      break
  print("Current pokemon:")
  temp_poke = []
  for i in db[na].keys():
    temp_poke.append(i)
    print(i)
  while True:
    poke = input("\nWhat pokemon do you need? (Enter nickname) \n")
    if poke in temp_poke:
      break
  #Printing the calc format
  x = []
  y = []
  x = json.loads(db.get_raw(na)).get(poke).get("stats")[0]
  y = json.loads(db.get_raw(na)).get(poke).get("ivs")
  print(db[na][poke]["poke"])
  print("Level:", db[na][poke]["lv"])
  print(db[na][poke]["ntr"],"Nature")
  print("Ability:",db[na][poke]["abil"])
  print("EVs: 252",x[0],"/","252",x[1])
  print("IVs:",y[0],"HP /",y[1],"Atk /",y[2],"Def /",y[3],"SpA /",y[4],"SpD","/",y[5],"Spe")
  for i in db[na][poke]["all_moves"]:
    print("-",i)



if __name__ == "__export_mon__":
  export_mon()

'''
Adding the functionality of 3 ways it's trained
'''
