stats = ["Atk", "HP","Def","SpA","SpD","Spe"]

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

print("Success")