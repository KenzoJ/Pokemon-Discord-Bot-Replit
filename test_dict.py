#the goal of the dictionary when creating it
'''
di = {
  "CJ": { "Name": "Henry",
          "Poke": "Rattata",
          "Lv":"50",
          "Ntr":"Hasty",
          "stats": ["HP","Spd", "Spe"],
          "Ab": "Runaway",
          "all_moves": ["Acid Spray", "Aromatherapy","Burning Jealousy", "Behemoth Bash"]
          "IVs":
        ["10","11","12","13","14"]
       }
}
'''

def calc_export():
  while True:
    p = input("Person?")
    if p == "CJ":
        while True:
          poke = input("What pokemon do you need?")
  #The stat sheet output for Pokemon Unbound Damage Calc specifically
          if poke == db["CJ"]["Poke"]:
            print(db["CJ"]["Poke"])
            print("Level:", db["CJ"]["Lv"])
            print(db["CJ"]["Ntr"],"Nature")
            print("Ability:",db["CJ"]["Ab"])
            #change the ability for 3.. EVs: 128 HP / 128 Atk / 252 SpD
            if len(db["CJ"]["EVs"]) == 3:
              print("EVs: 252",,db["CJ"]["stats"[0]],"/","126",db["CJ"]["stats"[1]],"/","126",db["CJ"]["stats"[2]])
            else:
              print("EVs: 252",db["CJ"]["stats"[0]],"/","252",db["CJ"]["stats"[1]])
            print("IVs:",db["CJ"]["IVs"][0],"HP /",db["CJ"]["IVs"][1],"Atk /",db["CJ"]["IVs"][2],"Def /",db["CJ"]["IVs"][3],"SpA /",db["CJ"]["IVs"][4],"SpD")
            print("-",db["CJ"]["Mv1"])
            print("-",db["CJ"]["Mv2"])
            print("-",db["CJ"]["Mv3"])
            print("-",db["CJ"]["Mv4"])
            break
          else:
            print("try again")
            continue
    
'''
#Glossary 
d.get(<key>[, <default>])
d.clear()
d.items() Returns a list of key-value pairs in a dictionary.
d.pop(<key>[, <default>]) Removes a key from a dictionary, if it is present, and returns its value.

'''