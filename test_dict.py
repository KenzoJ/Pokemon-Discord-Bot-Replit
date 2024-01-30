#the goal of the dictionary when creating it
di = {
  "CJ": { "Name": "Henry",
          "Poke": "Rattata",
          "Lv":"50",
          "Ntr":"Hasty",
          "Tra1":"HP",
          "Tra2": "Spd",
          "Ab": "Runaway",
          "Mv1": "Acid Spray",
          "Mv2": "Aromatherapy",
          "Mv3": "Burning Jealousy",
          "Mv4": "Behemoth Bash",
          "IVs":
        ["10","11","12","13","14"]
       }
}

#a loop to ask who needs a pokemon stat sheet
while True:
  p = input("Person?")
  if p == "CJ":
      while True:
        poke = input("What pokemon do you need?")
#The stat sheet output for Pokemon Unbound Damage Calc specifically
        if poke == di[p]["Poke"]:
          print(di[p]["Poke"])
          print("Level:", di[p]["Lv"])
          print(di[p]["Ntr"],"Nature")
          print("Ability:",di[p]["Ab"])
          print("EVs: 252",di[p]["Tra1"],"/","252",di[p]["Tra2"])
          print("IVs:",di[p]["IVs"][0],"HP /",di[p]["IVs"][1],"Atk /",di[p]["IVs"][2],"Def /",di[p]["IVs"][3],"SpA /",di[p]["IVs"][4],"SpD")
          print("-",di[p]["Mv1"])
          print("-",di[p]["Mv2"])
          print("-",di[p]["Mv3"])
          print("-",di[p]["Mv4"])
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