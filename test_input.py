import requests




def input_checker():
  
  #dictionaries for reference
  dict = {}
  all_natures = [
    "Bashful", "Docile", "Hardy", "Quirky", "Serious", "Adamant", "Brave", "Lonely", "Naughty", "Bold", "Impish", "Lax", "Relaxed", "Modest", "Mild", "Quiet", "Rash", "Calm","Careful", "Gentle", "Sassy", "Hasty", "Jolly", "Naive", "Timid",
  ]
  stats = ["Atk", "HP","Def","SpA","SpD","Spe"]
  
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
      
  #dictionary adder            
  db["CJ"["all_moves"]] = temp_moves
  db["CJ"["poke"]] = poke_lvl[0]
  db["CJ"["name"]] = nick
  db["CJ"["lv"]] = poke_lvl[1]
  db["CJ"["ntr"]] = add_nat
  db["CJ"["tra1"]] = add_stats[0]
  db["CJ"["tra2"]] = add_stats[1]
  db["CJ"["abil"]] = get_ability
  for i in db["CJ"].items():
    print(i)
  
'''
To do:
- Redefining 

'''