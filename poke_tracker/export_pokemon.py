#This asks who is looking for the pokemon, then the pokemon name, then the 
from replit import db
import json

def export_mon():
  temp_poke = []
  while True:
    na = input("For Whom?")
    if na == "CJ" or na == "Doug" or na == "Sam":
      break
  print("Current pokemon:")
  #Gives user options of which pokemon
  for i in db[na].keys():
    temp_poke.append(i)
    print(i)
  while True:
    poke = input("\nWhat pokemon do you need? (Enter nickname) \n")
    if poke in temp_poke:
      for x in calc_mon(na, poke):
        print(x)
      break
    
def calc_mon(na, poke):
  #Printing the calc format
  x = []
  y = []
  x = json.loads(db.get_raw(na)).get(poke).get("stats")[0]
  y = json.loads(db.get_raw(na)).get(poke).get("ivs")
  '''
#old formatting using print vs fstrings
  print(db[na][poke]["poke"])
  print("Level:", db[na][poke]["lv"])
  print(db[na][poke]["ntr"],"Nature")
  print("Ability:",db[na][poke]["abil"])
  print("EVs: 252",x[0],"/","252",x[1])
  print("IVs:",y[0],"HP /",y[1],"Atk /",y[2],"Def /",y[3],"SpA /",y[4],"SpD","/",y[5],"Spe")
  for i in db[na][poke]["all_moves"]:
    print("-",i)
    '''
#newer storing data in a single variable for easier testing
  test_vari = []
  test_vari.append(db[na][poke]["poke"])
  level = f'Level: {db[na][poke]["lv"]}'
  test_vari.append(level)
  test_vari.append(f'{db[na][poke]["ntr"]} {"Nature"}')
  test_vari.append(f'Ability: {db[na][poke]["abil"]}')
  test_vari.append(f'EVs: 252 {x[0]} / 252 {x[1]}')
  test_vari.append(f'IVs: {y[0]} HP / {y[1]} Atk / {y[2]} Def / {y[3]} SpA / {y[4]} SpD / {y[5]} Spe')
  for i in db[na][poke]["all_moves"]:
    test_vari.append(f"-{i}")
  print(test_vari)
  return test_vari
  
if __name__ == "__main__":
  export_mon()

'''
Adding the functionality of 3 ways it's trained
for x in test_vari:
  print(x)
'''
