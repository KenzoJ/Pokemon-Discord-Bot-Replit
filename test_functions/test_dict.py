#This asks who is looking for the pokemon, then the pokemon name, then the 
from replit import db
import json

def calc_export():
  while True:
    p = input("Person?")
    if p == "CJ":
      print("Current pokemon:",db["CJ"]["poke"])
      x = []
      y = []
      x = json.loads(db.get_raw("CJ")).get("stats")[0]
      y = (json.loads(db.get_raw("CJ")).get("ivs"))
      while True:
        poke = input("What pokemon do you need?")
#The stat sheet output for Pokemon Unbound Damage Calc specifically
        if poke == db["CJ"]["poke"]:
          print(db["CJ"]["poke"])
          print("Level:", db["CJ"]["lv"])
          print(db["CJ"]["ntr"],"Nature")
          print("Ability:",db["CJ"]["abil"])
          print("EVs: 252",x[0],"/","252",x[1])
          print("IVs:",y[0],"HP /",y[1],"Atk /",y[2],"Def /",y[3],"SpA /",y[4],"SpD","/",y[5],"Spe")
          for i in db["CJ"]["all_moves"]:
            print("-",i)
          break
      break



'''
#BUG - EV's - Problem with this is that we cannot check the length of db["CJ"]["stats"] because the actual length is 1, no matter the list. the database here saves the items in an observed list. 
ObservedList(value=[ObservedList(value=['HP', 'HP'])])

So what needs to be done is converting the Json to a list then checking the length. 

#IMPROVE - adding the set.raw to the input so that it automatically, theoretically, converts the list into a list instead of  Json notation...
'''
