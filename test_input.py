import requests

#dictionaries for reference
dict = {}
nature = [
  "Bashful", "Docile", "Hardy", "Quirky", "Serious", "Adamant", "Brave", "Lonely", "Naughty", "Bold", "Impish", "Lax", "Relaxed", "Modest", "Mild", "Quiet", "Rash", "Calm","Careful", "Gentle", "Sassy", "Hasty", "Jolly", "Naive", "Timid",
]
stats = ["Atk", "HP","Def","SpA","SpD"]
#start of user input

nick = input("Nickname?")
poke_lvl = input("Pokemon and level?")
input1 = input1.split()
while True:
  input2 = input("Nature?")
  
  if input2 in nature:
    while True: 
      input3 = input("How was it trained?")
      input3 = input3.split()
      if input3[0] in stats and input3[1] in stats:

while True:
  input4 = input("\nMoves learned?\n")
  with open("list_of_moves.txt") as file:
    contents = file.read()
    if input4 in contents:
    
      dict["Poke"] = poke_lvl[0]
      dict["Name"] = nick
      dict["Lv"] = poke_lvl[1]
      dict["Ntr"] = input2
      dict["Tra1"] = input3[0]
      dict["Tra2"] = input3[1]
      dict["Ab"] = input2[0]  

      for i in dict.items():
        print(i)
